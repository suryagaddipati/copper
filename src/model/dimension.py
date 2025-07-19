from typing import Optional
from pydantic import BaseModel
from enum import Enum


class DataType(str, Enum):
    STRING = "string"
    NUMBER = "number"
    BOOLEAN = "boolean"
    DATE = "date"


class Dimension(BaseModel):
    """Dimension with expression and metadata."""
    
    expression: str
    type: DataType = DataType.STRING
    label: Optional[str] = None
    description: Optional[str] = None