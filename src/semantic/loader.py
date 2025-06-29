import yaml
from pathlib import Path
from typing import Union, Dict, Any
from .schema import SemanticModel, Dimension, Measure, DataSource, Relationship


class SemanticModelLoader:
    """Loads and validates semantic models from YAML files."""
    
    @staticmethod
    def load_from_file(file_path: Union[str, Path]) -> SemanticModel:
        """Load a semantic model from a YAML file."""
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"Semantic model file not found: {file_path}")
        
        with open(path, 'r') as f:
            data = yaml.safe_load(f)
        
        return SemanticModelLoader.load_from_dict(data)
    
    @staticmethod
    def load_from_dict(data: Dict[str, Any]) -> SemanticModel:
        """Load a semantic model from a dictionary."""
        
        # Parse datasources (and tables for backward compatibility)
        datasources = {}
        tables = {}
        
        if 'datasources' in data:
            for source_name, source_def in data['datasources'].items():
                datasources[source_name] = DataSource(**source_def)
                
        if 'tables' in data:
            for table_name, table_def in data['tables'].items():
                # Ensure table_def has a type field for DataSource compatibility
                if 'type' not in table_def:
                    table_def['type'] = 'table'
                tables[table_name] = DataSource(**table_def)
        
        # Parse dimensions
        dimensions = {}
        if 'dimensions' in data:
            for dim_name, dim_def in data['dimensions'].items():
                dimensions[dim_name] = Dimension(**dim_def)
        
        # Parse measures
        measures = {}
        if 'measures' in data:
            for measure_name, measure_def in data['measures'].items():
                measures[measure_name] = Measure(**measure_def)
        
        # Parse relationships
        relationships = []
        if 'relationships' in data:
            for rel_def in data['relationships']:
                if isinstance(rel_def, str):
                    # Parse string format: "Orders.customer_id → Customers.id"
                    relationships.append(SemanticModelLoader._parse_relationship_string(rel_def))
                else:
                    # Parse dict format
                    relationships.append(Relationship(**rel_def))
        
        return SemanticModel(
            name=data.get('name', 'unnamed'),
            description=data.get('description'),
            datasources=datasources,
            tables=tables,
            dimensions=dimensions,
            measures=measures,
            relationships=relationships,
            includes=data.get('includes')
        )
    
    @staticmethod
    def _parse_relationship_string(rel_str: str) -> Relationship:
        """Parse relationship string format: 'Orders.customer_id → Customers.id'"""
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


def load(file_path: Union[str, Path]) -> SemanticModel:
    """Convenience function to load a semantic model."""
    return SemanticModelLoader.load_from_file(file_path)