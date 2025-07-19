from typing import Dict, List, Optional
from pydantic import BaseModel
from .datasource import DataSource
from .dimension import Dimension
from .measure import Measure
class Model(BaseModel):
    """Model containing dimensions and measures."""
    
    name: str
    description: Optional[str] = None
    datasources: Dict[str, DataSource] = {}
    dimensions: Dict[str, Dimension] = {}
    measures: Dict[str, Measure] = {}


class SemanticModel(BaseModel):
    """Top-level semantic model container."""
    
    name: str
    description: Optional[str] = None
    models: List[Model] = []
    
    @classmethod
    def load(cls, models: List[Model], name: str = "semantic_model", description: str = None) -> "SemanticModel":
        """Load semantic model from list of models."""
        return cls(
            name=name,
            description=description,
            models=models
        )