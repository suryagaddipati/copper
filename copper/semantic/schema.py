from typing import Dict, List, Optional, Union, Any
from pydantic import BaseModel, Field, validator
from enum import Enum


class DataType(str, Enum):
    STRING = "string"
    NUMBER = "number"
    BOOLEAN = "boolean"
    DATE = "date"
    CURRENCY = "currency"


class AggregationType(str, Enum):
    SUM = "sum"
    COUNT = "count"
    AVG = "avg"
    MIN = "min"
    MAX = "max"


class Dimension(BaseModel):
    """Represents a dimension in the semantic model."""
    
    sql: Optional[str] = None
    expression: Optional[str] = None
    type: DataType = DataType.STRING
    description: Optional[str] = None
    label: Optional[str] = None
    
    @validator('sql', 'expression')
    def sql_or_expression_required(cls, v, values):
        if not v and not values.get('sql') and not values.get('expression'):
            raise ValueError('Either sql or expression must be provided')
        return v


class Measure(BaseModel):
    """Represents a measure in the semantic model."""
    
    expression: str
    type: DataType = DataType.NUMBER
    aggregation: Optional[AggregationType] = None
    description: Optional[str] = None
    label: Optional[str] = None
    format: Optional[str] = None


class Relationship(BaseModel):
    """Represents a relationship between tables."""
    
    from_table: str = Field(..., alias="from")
    to_table: str = Field(..., alias="to")
    from_column: str
    to_column: str
    cardinality: str = "many_to_one"  # one_to_one, one_to_many, many_to_one, many_to_many
    
    class Config:
        allow_population_by_field_name = True


class Table(BaseModel):
    """Represents a table in the semantic model."""
    
    sql: Optional[str] = None
    database: Optional[str] = None
    schema: Optional[str] = None
    table: Optional[str] = None
    description: Optional[str] = None
    
    @validator('sql', 'table')
    def sql_or_table_required(cls, v, values):
        if not v and not values.get('sql') and not values.get('table'):
            raise ValueError('Either sql or table must be provided')
        return v


class SemanticModel(BaseModel):
    """Complete semantic model definition."""
    
    name: str
    description: Optional[str] = None
    tables: Dict[str, Table] = {}
    dimensions: Dict[str, Dimension] = {}
    measures: Dict[str, Measure] = {}
    relationships: List[Relationship] = []
    
    def get_dimension(self, name: str) -> Optional[Dimension]:
        """Get a dimension by name."""
        return self.dimensions.get(name)
    
    def get_measure(self, name: str) -> Optional[Measure]:
        """Get a measure by name."""
        return self.measures.get(name)
    
    def get_table(self, name: str) -> Optional[Table]:
        """Get a table by name."""
        return self.tables.get(name)
    
    def get_relationships_for_table(self, table_name: str) -> List[Relationship]:
        """Get all relationships involving a specific table."""
        return [
            rel for rel in self.relationships 
            if rel.from_table == table_name or rel.to_table == table_name
        ]