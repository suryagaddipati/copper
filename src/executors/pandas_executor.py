import pandas as pd
from typing import Dict, Any, List, Optional
from semantic.schema import SemanticModel, Dimension, Measure
from parser.antlr_parser import CopperParser
from parser.ast_nodes import *


class PandasCodeGenerator(ASTVisitor):
    """Generates Pandas code from AST nodes."""
    
    def __init__(self, dataframes: Dict[str, pd.DataFrame]):
        self.dataframes = dataframes
        self.current_df_name = None
    
    def visit_literal(self, node: Literal) -> str:
        """Generate code for literal values."""
        if node.type == 'string':
            return f"'{node.value}'"
        elif node.type == 'null':
            return 'None'
        else:
            return str(node.value)
    
    def visit_identifier(self, node: Identifier) -> str:
        """Generate code for identifiers."""
        return node.name
    
    def visit_column_reference(self, node: ColumnReference) -> str:
        """Generate code for column references."""
        if node.table:
            return f"{node.table}['{node.column}']"
        else:
            # Use current dataframe context
            return f"df['{node.column}']"
    
    def visit_binary_operation(self, node: BinaryOperation) -> str:
        """Generate code for binary operations."""
        left = node.left.accept(self)
        right = node.right.accept(self)
        
        operator_map = {
            '=': '==',
            '<>': '!=',
            '!=': '!=',
            'AND': '&',
            'OR': '|',
        }
        
        op = operator_map.get(node.operator, node.operator)
        
        # Wrap in parentheses for logical operations
        if op in ['&', '|']:
            return f"({left}) {op} ({right})"
        else:
            return f"{left} {op} {right}"
    
    def visit_unary_operation(self, node: UnaryOperation) -> str:
        """Generate code for unary operations."""
        operand = node.operand.accept(self)
        
        if node.operator == 'NOT':
            return f"~({operand})"
        elif node.operator == '-':
            return f"-({operand})"
        else:
            return f"{node.operator}({operand})"
    
    def visit_function_call(self, node: FunctionCall) -> str:
        """Generate code for function calls."""
        func_name = node.function_name.upper()
        args = [arg.accept(self) for arg in node.arguments]
        
        if func_name == 'SUM':
            return f"({args[0]}).sum()"
        elif func_name == 'COUNT':
            return f"({args[0]}).count()"
        elif func_name == 'AVG':
            return f"({args[0]}).mean()"
        elif func_name == 'MIN':
            return f"({args[0]}).min()"
        elif func_name == 'MAX':
            return f"({args[0]}).max()"
        elif func_name == 'COALESCE':
            # Use pandas fillna for coalesce
            result = args[0]
            for arg in args[1:]:
                result = f"({result}).fillna({arg})"
            return result
        else:
            # Generic function call
            args_str = ', '.join(args)
            return f"{func_name.lower()}({args_str})"
    
    def visit_if_expression(self, node: IfExpression) -> str:
        """Generate code for IF expressions."""
        condition = node.condition.accept(self)
        true_val = node.true_value.accept(self)
        false_val = node.false_value.accept(self)
        
        return f"np.where({condition}, {true_val}, {false_val})"
    
    def visit_switch_expression(self, node: SwitchExpression) -> str:
        """Generate code for SWITCH expressions."""
        # Use nested np.where for SWITCH
        expr = node.expression.accept(self)
        
        result = None
        if node.default_value:
            result = node.default_value.accept(self)
        else:
            result = "None"
        
        # Build from the end backwards
        for case in reversed(node.cases):
            condition = f"({expr}) == ({case.condition.accept(self)})"
            value = case.value.accept(self)
            result = f"np.where({condition}, {value}, {result})"
        
        return result
    
    def visit_case_expression(self, node: CaseExpression) -> str:
        """Generate code for CASE expressions."""
        result = None
        if node.else_value:
            result = node.else_value.accept(self)
        else:
            result = "None"
        
        # Build from the end backwards
        for when_clause in reversed(node.when_clauses):
            condition = when_clause.condition.accept(self)
            value = when_clause.value.accept(self)
            result = f"np.where({condition}, {value}, {result})"
        
        return result


class PandasExecutor:
    """Executes Copper queries using Pandas."""
    
    def __init__(self, semantic_model: SemanticModel):
        self.semantic_model = semantic_model
        self.parser = CopperParser()
    
    def execute(self, query, data_source: Optional[Dict[str, pd.DataFrame]] = None) -> pd.DataFrame:
        """Execute a query and return a Pandas DataFrame."""
        
        # Use provided data or create mock data
        if data_source is None:
            data_source = self._create_mock_data()
        
        # Validate query
        errors = query.validate()
        if errors:
            raise ValueError(f"Query validation failed: {errors}")
        
        # Start with the base dataframes
        dataframes = data_source.copy()
        
        # Apply joins based on relationships and required tables
        main_df = self._build_joined_dataframe(query, dataframes)
        
        # Apply filters
        if query._filters:
            main_df = self._apply_filters(main_df, query._filters, dataframes)
        
        # Build select columns
        select_columns = {}
        
        # Add dimensions
        for dim_name in query._dimensions:
            dimension = self.semantic_model.get_dimension(dim_name)
            if dimension.sql:
                # For now, assume simple column reference
                column_expr = self._parse_sql_to_pandas(dimension.sql, main_df, dataframes)
            elif dimension.expression:
                ast = self.parser.parse(dimension.expression)
                generator = PandasCodeGenerator(dataframes)
                column_expr = ast.accept(generator)
            else:
                raise ValueError(f"Dimension '{dim_name}' has no SQL or expression")
            
            select_columns[dim_name] = column_expr
        
        # Add measures (will be aggregated)
        measure_expressions = {}
        for measure_name in query._measures:
            measure = self.semantic_model.get_measure(measure_name)
            ast = self.parser.parse(measure.expression)
            generator = PandasCodeGenerator(dataframes)
            measure_expressions[measure_name] = ast.accept(generator)
        
        # Group by dimensions if we have both dimensions and measures
        if query._dimensions and query._measures:
            # Group by dimensions
            groupby_cols = list(select_columns.keys())
            
            # Add dimension columns to main_df
            for dim_name, expr in select_columns.items():
                try:
                    main_df[dim_name] = eval(expr.replace('df', 'main_df'))
                except:
                    # Fallback: assume it's a simple column name
                    if dim_name in main_df.columns:
                        main_df[dim_name] = main_df[dim_name]
                    else:
                        raise ValueError(f"Could not evaluate dimension expression: {expr}")
            
            # Group and aggregate
            grouped = main_df.groupby(groupby_cols)
            
            result_data = {}
            # Add grouped dimensions
            for dim_name in groupby_cols:
                result_data[dim_name] = grouped[dim_name].first()
            
            # Add aggregated measures
            for measure_name, expr in measure_expressions.items():
                try:
                    # Evaluate measure expression in grouped context
                    # This is simplified - in practice you'd need more sophisticated handling
                    if 'sum()' in expr.lower():
                        col_ref = expr.split('.sum()')[0].replace('(', '').replace(')', '')
                        if 'main_df[' in col_ref:
                            col_name = col_ref.split("'")[1]
                            result_data[measure_name] = grouped[col_name].sum()
                        else:
                            result_data[measure_name] = grouped.apply(lambda x: eval(expr.replace('main_df', 'x')))
                    else:
                        result_data[measure_name] = grouped.apply(lambda x: eval(expr.replace('main_df', 'x')))
                except Exception as e:
                    raise ValueError(f"Could not evaluate measure expression '{expr}': {e}")
            
            result_df = pd.DataFrame(result_data).reset_index(drop=True)
        
        else:
            # No grouping needed
            result_data = {}
            
            # Add dimensions
            for dim_name, expr in select_columns.items():
                try:
                    result_data[dim_name] = eval(expr.replace('df', 'main_df'))
                except:
                    if dim_name in main_df.columns:
                        result_data[dim_name] = main_df[dim_name]
                    else:
                        raise ValueError(f"Could not evaluate dimension expression: {expr}")
            
            # Add measures
            for measure_name, expr in measure_expressions.items():
                try:
                    result_data[measure_name] = eval(expr.replace('df', 'main_df'))
                except Exception as e:
                    raise ValueError(f"Could not evaluate measure expression '{expr}': {e}")
            
            result_df = pd.DataFrame(result_data)
        
        # Apply ordering
        if query._order_by:
            # Parse order by specifications
            sort_columns = []
            sort_ascending = []
            for order_spec in query._order_by:
                parts = order_spec.split()
                col_name = parts[0]
                direction = parts[1] if len(parts) > 1 else 'ASC'
                sort_columns.append(col_name)
                sort_ascending.append(direction.upper() == 'ASC')
            
            result_df = result_df.sort_values(sort_columns, ascending=sort_ascending)
        
        # Apply limit
        if query._limit:
            result_df = result_df.head(query._limit)
        
        return result_df
    
    def _create_mock_data(self) -> Dict[str, pd.DataFrame]:
        """Create mock data for testing."""
        # This would be replaced with actual data loading logic
        orders = pd.DataFrame({
            'id': [1, 2, 3, 4, 5],
            'customer_id': [1, 2, 1, 3, 2],
            'total_amount': [100.0, 250.0, 75.0, 500.0, 125.0],
            'status': ['shipped', 'pending', 'shipped', 'shipped', 'cancelled'],
            'order_date': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'])
        })
        
        customers = pd.DataFrame({
            'id': [1, 2, 3],
            'name': ['Alice', 'Bob', 'Charlie'],
            'region': ['West', 'East', 'West'],
            'tier': ['Gold', 'Silver', 'Gold'],
            'age': [25, 35, 45]
        })
        
        return {'Orders': orders, 'Customers': customers}
    
    def _build_joined_dataframe(self, query, dataframes: Dict[str, pd.DataFrame]) -> pd.DataFrame:
        """Build the main dataframe with necessary joins."""
        required_tables = query.get_required_tables()
        
        if not required_tables:
            # Default to first available table
            table_name = list(dataframes.keys())[0]
            return dataframes[table_name].copy()
        
        # Start with the first required table
        main_table = required_tables[0]
        main_df = dataframes[main_table].copy()
        
        # Apply joins for other required tables
        for table_name in required_tables[1:]:
            if table_name in dataframes:
                # Find relationship between main table and this table
                relationships = self.semantic_model.get_relationships_for_table(table_name)
                
                for rel in relationships:
                    if (rel.from_table == main_table and rel.to_table == table_name) or \
                       (rel.from_table == table_name and rel.to_table == main_table):
                        
                        # Perform the join
                        if rel.from_table == main_table:
                            main_df = main_df.merge(
                                dataframes[table_name],
                                left_on=rel.from_column,
                                right_on=rel.to_column,
                                how='left',
                                suffixes=('', f'_{table_name}')
                            )
                        else:
                            main_df = main_df.merge(
                                dataframes[table_name],
                                left_on=rel.to_column,
                                right_on=rel.from_column,
                                how='left',
                                suffixes=('', f'_{table_name}')
                            )
                        break
        
        return main_df
    
    def _apply_filters(self, df: pd.DataFrame, filters: List[str], dataframes: Dict[str, pd.DataFrame]) -> pd.DataFrame:
        """Apply filter expressions to the dataframe."""
        result_df = df.copy()
        
        for filter_expr in filters:
            try:
                ast = self.parser.parse(filter_expr)
                generator = PandasCodeGenerator(dataframes)
                pandas_expr = ast.accept(generator)
                
                # Apply the filter
                mask = eval(pandas_expr.replace('df', 'result_df'))
                result_df = result_df[mask]
            except Exception as e:
                raise ValueError(f"Could not apply filter '{filter_expr}': {e}")
        
        return result_df
    
    def _parse_sql_to_pandas(self, sql: str, df: pd.DataFrame, dataframes: Dict[str, pd.DataFrame]) -> str:
        if '.' in sql:
            parts = sql.split('.')
            table = parts[0]
            column = parts[1]
            return f"df['{column}']"
        else:
            return f"df['{sql}']"