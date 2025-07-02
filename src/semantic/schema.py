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
    
    expression: str  # Required: Copper expression
    type: DataType = DataType.STRING
    description: Optional[str] = None
    label: Optional[str] = None


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


class DataSource(BaseModel):
    """Represents a data source in the semantic model."""
    
    type: str = "table"  # table, view, api, stream, etc.
    sql: Optional[str] = None
    database: Optional[str] = None
    schema: Optional[str] = None
    table: Optional[str] = None
    endpoint: Optional[str] = None  # for API sources
    topic: Optional[str] = None     # for streaming sources
    refresh_schedule: Optional[str] = None
    description: Optional[str] = None
    columns: Optional[List[Dict[str, str]]] = None
    
    @validator('sql', 'table', 'endpoint')
    def source_identifier_required(cls, v, values):
        # At least one source identifier must be provided
        if not any([v, values.get('sql'), values.get('table'), values.get('endpoint')]):
            raise ValueError('At least one of sql, table, or endpoint must be provided')
        return v


class Connection(BaseModel):
    """Represents a data connection with authentication and configuration."""
    
    name: str
    type: str  # postgresql, mysql, api, file, etc.
    host: Optional[str] = None
    port: Optional[int] = None
    database: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    connection_string: Optional[str] = None
    api_endpoint: Optional[str] = None
    api_key: Optional[str] = None
    file_path: Optional[str] = None
    options: Optional[Dict[str, Any]] = {}
    description: Optional[str] = None


class Table(BaseModel):
    """Represents a logical table with schema information."""
    
    name: str
    connection: str  # Reference to connection name
    source: str  # Table name, view name, or query
    type: str = "table"  # table, view, query, api_endpoint
    schema: Optional[str] = None
    columns: Optional[List[Dict[str, Any]]] = None
    description: Optional[str] = None
    refresh_schedule: Optional[str] = None


class Model(BaseModel):
    """Represents a semantic model with business logic."""
    
    name: str
    description: Optional[str] = None
    tables: List[str] = []  # References to table names
    models: List[str] = []  # References to other model names
    dimensions: Dict[str, Dimension] = {}
    measures: Dict[str, Measure] = {}
    relationships: List[Relationship] = []


class Project(BaseModel):
    """Simple project container for organizing definitions."""
    
    name: str
    description: Optional[str] = None
    version: str = "1.0.0"
    
    # References to component files (keep existing structure)
    datasources_file: Optional[str] = "datasources.yaml"
    model_file: Optional[str] = "model.yaml" 
    connection_file: Optional[str] = "../connections/local_files.yaml"


class SemanticModel(BaseModel):
    """Complete semantic model definition."""
    
    name: str
    description: Optional[str] = None
    datasources: Dict[str, DataSource] = {}
    tables: Dict[str, DataSource] = {}  # Backward compatibility alias
    dimensions: Dict[str, Dimension] = {}
    measures: Dict[str, Measure] = {}
    relationships: List[Relationship] = []
    
    def get_dimension(self, name: str) -> Optional[Dimension]:
        """Get a dimension by name."""
        return self.dimensions.get(name)
    
    def get_measure(self, name: str) -> Optional[Measure]:
        """Get a measure by name."""
        return self.measures.get(name)
    
    def get_datasource(self, name: str) -> Optional[DataSource]:
        """Get a data source by name."""
        # Check datasources first, then fall back to tables for backward compatibility
        return self.datasources.get(name) or self.tables.get(name)
    
    def get_table(self, name: str) -> Optional[DataSource]:
        """Get a table by name (backward compatibility)."""
        return self.get_datasource(name)
    
    def get_relationships_for_datasource(self, source_name: str) -> List[Relationship]:
        """Get all relationships involving a specific data source."""
        return [
            rel for rel in self.relationships 
            if rel.from_table == source_name or rel.to_table == source_name
        ]
    
    def get_relationships_for_table(self, table_name: str) -> List[Relationship]:
        """Get all relationships involving a specific table (backward compatibility)."""
        return self.get_relationships_for_datasource(table_name)