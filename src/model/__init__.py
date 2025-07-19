"""
New simplified model architecture for Copper.

Implements the 4-class design from docs/model.md:
- DataSource: Data source metadata
- Dimension: Dimension with expression  
- Measure: Measure with calculate() method
- Model: Container for dimensions and measures
- SemanticModel: Top-level with load() method
"""

from .datasource import DataSource
from .dimension import Dimension, DataType
from .measure import Measure
from .semantic import Model, SemanticModel
from .loader import ModelLoader, load_model

__all__ = [
    'DataSource',
    'Dimension', 
    'DataType',
    'Measure',
    'Model',
    'SemanticModel', 
    'ModelLoader',
    'load_model'
]