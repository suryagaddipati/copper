from typing import Dict, List, Any
from src.parser.antlr_parser import ParsedNode, NodeType


class SQLGenerator:
    
    def __init__(self, parsed_result: Dict[str, Any]):
        self.models = {model.name: model for model in parsed_result.get('models', [])}
        self.views = {view.name: view for view in parsed_result.get('views', [])}
    
    def generate_view_sql(self, view_name: str) -> str:
        if view_name not in self.views:
            raise ValueError(f"View '{view_name}' not found")
        
        view = self.views[view_name]
        base_model_name = view.properties.get('from')
        
        if not base_model_name:
            raise ValueError(f"View '{view_name}' has no 'from' property")
        
        if base_model_name not in self.models:
            raise ValueError(f"Model '{base_model_name}' not found")
        
        base_model = self.models[base_model_name]
        fields = self._get_model_fields(base_model)
        select_clause = self._build_select_clause(fields, base_model_name)
        from_clause = self._build_from_clause(base_model_name)
        
        return f"{select_clause}\n{from_clause}"
    
    def _get_model_fields(self, model: ParsedNode) -> List[Dict[str, str]]:
        fields = []
        
        for child in model.children:
            if child.type == NodeType.DIMENSION:
                fields.append({
                    'name': child.name,
                    'type': 'dimension',
                    'sql_type': child.properties.get('type', 'string')
                })
            elif child.type == NodeType.MEASURE:
                fields.append({
                    'name': child.name,
                    'type': 'measure',
                    'sql_type': child.properties.get('type', 'number'),
                    'expression': child.properties.get('expression', '')
                })
        
        return fields
    
    def _build_select_clause(self, fields: List[Dict[str, str]], table_name: str) -> str:
        select_items = []
        
        for field in fields:
            if field['type'] in ['dimension', 'measure']:
                select_items.append(f"  {table_name}.{field['name']}")
        
        return f"SELECT\n{',\\n'.join(select_items)}"
    
    def _build_from_clause(self, table_name: str) -> str:
        return f"FROM {table_name}"