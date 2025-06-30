#!/usr/bin/env python3
"""
SQL Generator for Copper Semantic Layer

Converts Copper expressions and queries into executable SQL.
"""

from typing import Dict, List, Any, Optional
try:
    from ..semantic.schema import SemanticModel, Dimension, Measure
    from ..parser.ast_nodes import ASTNode, ColumnReference, FunctionCall, BinaryOperation, CaseExpression
except ImportError:
    from semantic.schema import SemanticModel, Dimension, Measure
    from parser.ast_nodes import ASTNode, ColumnReference, FunctionCall, BinaryOperation, CaseExpression


class SQLGenerator:
    
    def __init__(self, semantic_model: SemanticModel, dialect: str = "standard"):
        self.semantic_model = semantic_model
        self.dialect = dialect.lower()
        self.table_aliases = {}
        
    def generate(self, query) -> str:
        select_clause = self._build_select_clause(query)
        from_clause = self._build_from_clause(query)
        where_clause = self._build_where_clause(query)
        group_by_clause = self._build_group_by_clause(query)
        
        sql_parts = [
            "SELECT",
            select_clause,
            "FROM",
            from_clause
        ]
        
        if where_clause:
            sql_parts.extend(["WHERE", where_clause])
            
        if group_by_clause:
            sql_parts.extend(["GROUP BY", group_by_clause])
            
        return "\n".join(sql_parts)
    
    def _build_select_clause(self, query) -> str:
        select_items = []
        
        for dim_name in query._dimensions:
            dimension = self.semantic_model.get_dimension(dim_name)
            if dimension:
                sql_expr = self._convert_expression_to_sql(dimension.expression)
                select_items.append(f"  {sql_expr} AS {dim_name}")
        
        for measure_name in query._measures:
            measure = self.semantic_model.get_measure(measure_name)
            if measure:
                sql_expr = self._convert_expression_to_sql(measure.expression)
                select_items.append(f"  {sql_expr} AS {measure_name}")
        
        return ",\n".join(select_items)
    
    def _build_from_clause(self, query) -> str:
        required_tables = self._get_required_tables(query)
        
        if not required_tables:
            return ""
            
        main_table = required_tables[0]
        datasource = self.semantic_model.get_datasource(main_table)
        
        if not datasource:
            return f"  {main_table}"
            
        table_ref = self._build_table_reference(main_table, datasource)
        from_parts = [f"  {table_ref}"]
        
        for table_name in required_tables[1:]:
            join_clause = self._build_join_clause(main_table, table_name)
            if join_clause:
                from_parts.append(join_clause)
        
        return "\n".join(from_parts)
    
    def _build_table_reference(self, table_name: str, datasource) -> str:
        parts = []
        
        if datasource.database:
            parts.append(datasource.database)
        if datasource.schema:
            parts.append(datasource.schema)
        
        table_part = datasource.table if datasource.table else table_name
        parts.append(table_part)
        
        full_name = ".".join(parts)
        
        if table_name != table_part:
            self.table_aliases[table_name] = table_name
            return f"{full_name} AS {table_name}"
        else:
            return full_name
    
    def _build_join_clause(self, main_table: str, join_table: str) -> Optional[str]:
        relationships = self.semantic_model.relationships
        
        for rel in relationships:
            if ((rel.from_table == main_table and rel.to_table == join_table) or
                (rel.from_table == join_table and rel.to_table == main_table)):
                
                join_datasource = self.semantic_model.get_datasource(join_table)
                if join_datasource:
                    table_ref = self._build_table_reference(join_table, join_datasource)
                    
                    if rel.from_table == main_table:
                        join_condition = f"{rel.from_table}.{rel.from_column} = {rel.to_table}.{rel.to_column}"
                    else:
                        join_condition = f"{rel.to_table}.{rel.to_column} = {rel.from_table}.{rel.from_column}"
                    
                    return f"  LEFT JOIN {table_ref}\n    ON {join_condition}"
        
        return None
    
    def _build_where_clause(self, query) -> Optional[str]:
        if not query._filters:
            return None
            
        filter_conditions = []
        for filter_expr in query._filters:
            sql_condition = self._convert_expression_to_sql(filter_expr)
            filter_conditions.append(f"  {sql_condition}")
        
        return "\n  AND ".join(filter_conditions)
    
    def _build_group_by_clause(self, query) -> Optional[str]:
        if not query._dimensions or not query._measures:
            return None
            
        group_items = []
        for dim_name in query._dimensions:
            dimension = self.semantic_model.get_dimension(dim_name)
            if dimension:
                sql_expr = self._convert_expression_to_sql(dimension.expression)
                group_items.append(f"  {sql_expr}")
        
        return ",\n".join(group_items)
    
    def _convert_expression_to_sql(self, expression: str) -> str:
        sql_expr = expression
        
        function_mappings = {
            "COUNT": "COUNT",
            "SUM": "SUM", 
            "AVG": "AVG",
            "MIN": "MIN",
            "MAX": "MAX",
            "YEAR": "EXTRACT(YEAR FROM",
            "MONTH": "EXTRACT(MONTH FROM",
            "DAY": "EXTRACT(DAY FROM"
        }
        
        for copper_func, sql_func in function_mappings.items():
            if copper_func == "YEAR" or copper_func == "MONTH" or copper_func == "DAY":
                import re
                pattern = f"{copper_func}\\(([^)]+)\\)"
                replacement = f"{sql_func} \\1)"
                sql_expr = re.sub(pattern, replacement, sql_expr)
            else:
                sql_expr = sql_expr.replace(copper_func, sql_func)
        
        sql_expr = sql_expr.replace("CASE WHEN", "CASE\n    WHEN")
        sql_expr = sql_expr.replace(" THEN ", " THEN\n      ")
        sql_expr = sql_expr.replace(" ELSE ", "\n    ELSE\n      ")
        sql_expr = sql_expr.replace(" END", "\n  END")
        
        return sql_expr
    
    def _get_required_tables(self, query) -> List[str]:
        required_tables = set()
        
        for dim_name in query._dimensions:
            dimension = self.semantic_model.get_dimension(dim_name)
            if dimension:
                tables = self._extract_table_names_from_expression(dimension.expression)
                required_tables.update(tables)
        
        for measure_name in query._measures:
            measure = self.semantic_model.get_measure(measure_name)
            if measure:
                tables = self._extract_table_names_from_expression(measure.expression)
                required_tables.update(tables)
        
        for filter_expr in query._filters:
            tables = self._extract_table_names_from_expression(filter_expr)
            required_tables.update(tables)
        
        return list(required_tables)
    
    def _extract_table_names_from_expression(self, expression: str) -> List[str]:
        import re
        
        pattern = r'\b([a-zA-Z_][a-zA-Z0-9_]*)\.[a-zA-Z_][a-zA-Z0-9_]*'
        matches = re.findall(pattern, expression)
        
        return list(set(matches))


def generate_sql(query, dialect: str = "standard") -> str:
    generator = SQLGenerator(query.semantic_model, dialect)
    return generator.generate(query)