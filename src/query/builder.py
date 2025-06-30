from typing import List, Dict, Optional, Any
from semantic.schema import SemanticModel
from parser.antlr_parser import CopperParser
from parser.ast_nodes import ASTNode


class Query:
    
    def __init__(self, semantic_model: SemanticModel):
        self.semantic_model = semantic_model
        self.parser = CopperParser()
        self._dimensions: List[str] = []
        self._measures: List[str] = []
        self._filters: List[str] = []
        self._limit: Optional[int] = None
        self._order_by: List[str] = []
    
    def dimensions(self, dimension_names: List[str]) -> 'Query':
        for dim_name in dimension_names:
            if not self.semantic_model.get_dimension(dim_name):
                raise ValueError(f"Dimension '{dim_name}' not found in semantic model")
        
        self._dimensions.extend(dimension_names)
        return self
    
    def measures(self, measure_names: List[str]) -> 'Query':
        for measure_name in measure_names:
            if not self.semantic_model.get_measure(measure_name):
                raise ValueError(f"Measure '{measure_name}' not found in semantic model")
        
        self._measures.extend(measure_names)
        return self
    
    def filters(self, filter_expressions: List[str]) -> 'Query':
        for filter_expr in filter_expressions:
            try:
                self.parser.parse(filter_expr)
            except Exception as e:
                raise ValueError(f"Invalid filter expression '{filter_expr}': {e}")
        
        self._filters.extend(filter_expressions)
        return self
    
    def limit(self, count: int) -> 'Query':
        if count <= 0:
            raise ValueError("Limit must be positive")
        self._limit = count
        return self
    
    def order_by(self, columns: List[str], ascending: bool = True) -> 'Query':
        direction = "ASC" if ascending else "DESC"
        order_specs = [f"{col} {direction}" for col in columns]
        self._order_by.extend(order_specs)
        return self
    
    def to_pandas(self, data_source: Optional[Dict[str, Any]] = None):
        from executors.pandas_executor import PandasExecutor
        
        executor = PandasExecutor(self.semantic_model)
        return executor.execute(self, data_source)
    
    def to_sql(self, dialect: str = "standard") -> str:
        try:
            from ..executors.sql_generator import SQLGenerator
        except ImportError:
            from executors.sql_generator import SQLGenerator
        
        generator = SQLGenerator(self.semantic_model, dialect)
        return generator.generate(self)
    
    
    def get_required_tables(self) -> List[str]:
        required_tables = set()
        
        for dim_name in self._dimensions:
            dimension = self.semantic_model.get_dimension(dim_name)
            if dimension and dimension.sql:
                required_tables.update(self._extract_table_names(dimension.sql))
        
        for measure_name in self._measures:
            measure = self.semantic_model.get_measure(measure_name)
            if measure and measure.expression:
                ast = self.parser.parse(measure.expression)
                required_tables.update(self._extract_tables_from_ast(ast))
        
        for filter_expr in self._filters:
            ast = self.parser.parse(filter_expr)
            required_tables.update(self._extract_tables_from_ast(ast))
        
        return list(required_tables)
    
    def _extract_table_names(self, sql: str) -> List[str]:
        words = sql.split()
        tables = []
        for i, word in enumerate(words):
            if '.' in word and not word.startswith("'") and not word.startswith('"'):
                table_part = word.split('.')[0]
                if table_part.isidentifier():
                    tables.append(table_part)
        return tables
    
    def _extract_tables_from_ast(self, ast: ASTNode) -> List[str]:
        from parser.ast_nodes import ColumnReference
        
        tables = []
        
        def visit_node(node):
            if isinstance(node, ColumnReference) and node.table:
                tables.append(node.table)
            
            for attr_name in dir(node):
                attr = getattr(node, attr_name)
                if isinstance(attr, ASTNode):
                    visit_node(attr)
                elif isinstance(attr, list):
                    for item in attr:
                        if isinstance(item, ASTNode):
                            visit_node(item)
        
        visit_node(ast)
        return tables
    
    def validate(self) -> List[str]:
        errors = []
        
        if not self._dimensions and not self._measures:
            errors.append("Query must include at least one dimension or measure")
        
        for dim_name in self._dimensions:
            if not self.semantic_model.get_dimension(dim_name):
                errors.append(f"Dimension '{dim_name}' not found")
        
        for measure_name in self._measures:
            if not self.semantic_model.get_measure(measure_name):
                errors.append(f"Measure '{measure_name}' not found")
        
        for filter_expr in self._filters:
            try:
                self.parser.parse(filter_expr)
            except Exception as e:
                errors.append(f"Invalid filter expression '{filter_expr}': {e}")
        
        return errors
    
    def __repr__(self) -> str:
        parts = []
        if self._dimensions:
            parts.append(f"dimensions={self._dimensions}")
        if self._measures:
            parts.append(f"measures={self._measures}")
        if self._filters:
            parts.append(f"filters={self._filters}")
        if self._limit:
            parts.append(f"limit={self._limit}")
        if self._order_by:
            parts.append(f"order_by={self._order_by}")
        
        return f"Query({', '.join(parts)})"