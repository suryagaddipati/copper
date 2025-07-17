import yaml
from pathlib import Path
from typing import Union, Dict, Any
from .schema import SemanticModel, Dimension, Measure, DataSource, Relationship, Connection, Table, Model


class SemanticModelLoader:
    
    @staticmethod
    def load_from_file(file_path: Union[str, Path]) -> SemanticModel:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"Semantic model file not found: {file_path}")
        
        with open(path, 'r') as f:
            data = yaml.safe_load(f)
        
        return SemanticModelLoader.load_from_dict(data, base_path=path.parent)
    
    @staticmethod
    def load_from_dict(data: Dict[str, Any], base_path: Path = None) -> SemanticModel:
        # Process includes first
        if 'include' in data and base_path:
            data = SemanticModelLoader._process_includes(data, base_path)
        
        datasources = {}
        tables = {}
        
        if 'datasources' in data:
            for source_name, source_def in data['datasources'].items():
                datasources[source_name] = DataSource(**source_def)
                
        if 'tables' in data:
            for table_name, table_def in data['tables'].items():
                if 'type' not in table_def:
                    table_def['type'] = 'table'
                tables[table_name] = DataSource(**table_def)
        
        dimensions = {}
        if 'dimensions' in data:
            for dim_name, dim_def in data['dimensions'].items():
                dimensions[dim_name] = Dimension(**dim_def)
        
        measures = {}
        if 'measures' in data:
            for measure_name, measure_def in data['measures'].items():
                measures[measure_name] = Measure(**measure_def)
        
        relationships = []
        if 'relationships' in data:
            for rel_def in data['relationships']:
                if isinstance(rel_def, str):
                    relationships.append(SemanticModelLoader._parse_relationship_string(rel_def))
                else:
                    relationships.append(Relationship(**rel_def))
        
        return SemanticModel(
            name=data.get('name', 'unnamed'),
            description=data.get('description'),
            datasources=datasources,
            tables=tables,
            dimensions=dimensions,
            measures=measures,
            relationships=relationships
        )
    
    @staticmethod
    def _process_includes(data: Dict[str, Any], base_path: Path) -> Dict[str, Any]:
        """Process include directives in the semantic model data."""
        include_spec = data.get('include')
        if not include_spec:
            return data
        
        # Support both single include and list of includes
        if isinstance(include_spec, str):
            include_files = [include_spec]
        elif isinstance(include_spec, list):
            include_files = include_spec
        else:
            raise ValueError(f"Invalid include format: {include_spec}")
        
        # Load and merge included files
        merged_data = data.copy()
        
        for include_file in include_files:
            include_path = base_path / include_file
            if not include_path.exists():
                raise FileNotFoundError(f"Include file not found: {include_path}")
            
            with open(include_path, 'r') as f:
                include_data = yaml.safe_load(f)
            
            # Merge the included data
            merged_data = SemanticModelLoader._merge_data(merged_data, include_data)
        
        # Remove the include directive from the final data
        if 'include' in merged_data:
            del merged_data['include']
        
        return merged_data
    
    @staticmethod
    def _merge_data(base_data: Dict[str, Any], include_data: Dict[str, Any]) -> Dict[str, Any]:
        """Merge included data into base data."""
        merged = base_data.copy()
        
        # Define sections that should be merged (not overwritten)
        merge_sections = ['datasources', 'tables', 'dimensions', 'measures', 'relationships']
        
        for key, value in include_data.items():
            if key in merge_sections and key in merged:
                # Merge dictionaries
                if isinstance(merged[key], dict) and isinstance(value, dict):
                    merged[key] = {**value, **merged[key]}  # Base data takes precedence
                # Merge lists
                elif isinstance(merged[key], list) and isinstance(value, list):
                    merged[key] = value + merged[key]  # Base data takes precedence
                else:
                    # Keep base data if types don't match
                    pass
            elif key not in merged:
                # Add new keys from included file
                merged[key] = value
            # If key exists in base but not in merge_sections, keep base value
        
        return merged
    
    @staticmethod
    def _parse_relationship_string(rel_str: str) -> Relationship:
        try:
            left, right = rel_str.split('→')
            left = left.strip()
            right = right.strip()
            
            from_table, from_column = left.split('.')
            to_table, to_column = right.split('.')
            
            return Relationship(
                from_table=from_table.strip(),
                to_table=to_table.strip(), 
                from_column=from_column.strip(),
                to_column=to_column.strip()
            )
        except ValueError:
            raise ValueError(f"Invalid relationship format: {rel_str}. Expected format: 'Table1.column1 → Table2.column2'")


    @staticmethod
    def load_connection_from_dict(data: Dict[str, Any]) -> Connection:
        return Connection(**data)
    
    @staticmethod
    def load_table_from_dict(data: Dict[str, Any]) -> Table:
        return Table(**data)
    
    @staticmethod
    def load_model_from_dict(data: Dict[str, Any]) -> Model:
        dimensions = {}
        if 'dimensions' in data:
            for dim_name, dim_def in data['dimensions'].items():
                dimensions[dim_name] = Dimension(**dim_def)
        
        measures = {}
        if 'measures' in data:
            for measure_name, measure_def in data['measures'].items():
                measures[measure_name] = Measure(**measure_def)
        
        relationships = []
        if 'relationships' in data:
            for rel_def in data['relationships']:
                if isinstance(rel_def, str):
                    relationships.append(SemanticModelLoader._parse_relationship_string(rel_def))
                else:
                    relationships.append(Relationship(**rel_def))
        
        return Model(
            name=data.get('name', 'unnamed'),
            description=data.get('description'),
            tables=data.get('tables', []),
            models=data.get('models', []),
            dimensions=dimensions,
            measures=measures,
            relationships=relationships
        )


def load(file_path: Union[str, Path]) -> SemanticModel:
    return SemanticModelLoader.load_from_file(file_path)