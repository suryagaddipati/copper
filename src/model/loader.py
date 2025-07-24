import yaml
from pathlib import Path
from typing import Union, Dict, Any
from .datasource import DataSource
from .dimension import Dimension, DataType
from .measure import Measure
from .semantic import Model, SemanticModel


class ModelLoader:
    
    @staticmethod
    def load_from_file(file_path: Union[str, Path]) -> Model:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"Model file not found: {file_path}")
        
        with open(path, 'r') as f:
            data = yaml.safe_load(f)
        
        return ModelLoader.load_from_dict(data, base_path=path.parent)
    
    @staticmethod
    def load_from_dict(data: Dict[str, Any], base_path: Path = None) -> Model:
        if 'include' in data and base_path:
            data = ModelLoader._process_includes(data, base_path)
        
        datasources = {}
        if 'datasources' in data:
            for name, ds_def in data['datasources'].items():
                datasources[name] = DataSource(**ds_def)
        
        dimensions = {}
        if 'dimensions' in data:
            for name, dim_def in data['dimensions'].items():
                if 'type' in dim_def:
                    dim_def['type'] = DataType(dim_def['type'])
                dimensions[name] = Dimension(**dim_def)
        
        measures = {}
        if 'measures' in data:
            for name, measure_def in data['measures'].items():
                if 'type' in measure_def:
                    measure_def['type'] = DataType(measure_def['type'])
                measures[name] = Measure(**measure_def)
        
        return Model(
            name=data.get('name', 'unnamed'),
            description=data.get('description'),
            datasources=datasources,
            dimensions=dimensions,
            measures=measures
        )
    
    @staticmethod
    def _process_includes(data: Dict[str, Any], base_path: Path) -> Dict[str, Any]:
        include_spec = data.get('include')
        if not include_spec:
            return data
        
        if isinstance(include_spec, str):
            include_files = [include_spec]
        elif isinstance(include_spec, list):
            include_files = include_spec
        else:
            raise ValueError(f"Invalid include format: {include_spec}")
        
        merged_data = data.copy()
        
        for include_file in include_files:
            include_path = base_path / include_file
            if not include_path.exists():
                raise FileNotFoundError(f"Include file not found: {include_path}")
            
            with open(include_path, 'r') as f:
                include_data = yaml.safe_load(f)
            
            merged_data = ModelLoader._merge_data(merged_data, include_data)
        
        if 'include' in merged_data:
            del merged_data['include']
        
        return merged_data
    
    @staticmethod
    def _merge_data(base_data: Dict[str, Any], include_data: Dict[str, Any]) -> Dict[str, Any]:
        merged = base_data.copy()
        
        merge_sections = ['datasources', 'dimensions', 'measures']
        
        for key, value in include_data.items():
            if key in merge_sections and key in merged:
                if isinstance(merged[key], dict) and isinstance(value, dict):
                    merged[key] = {**value, **merged[key]}
                else:
                    pass
                    pass
            elif key not in merged:
                merged[key] = value
        
        return merged


def load_model(file_path: Union[str, Path]) -> Model:
    return ModelLoader.load_from_file(file_path)