"""
AST Node Definitions for Copper Language

This module defines the Abstract Syntax Tree node classes
that represent the parsed structure of Copper files.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Union, Any
from abc import ABC, abstractmethod


@dataclass
class ASTNode(ABC):
    """Base class for all AST nodes"""
    line: int = 0
    column: int = 0


@dataclass
class Program(ASTNode):
    """Root node representing a complete Copper file"""
    statements: List['Statement'] = field(default_factory=list)


@dataclass
class Statement(ASTNode):
    """Base class for top-level statements"""
    pass


@dataclass
class Comment(Statement):
    """Comment statement"""
    text: str = ""


@dataclass
class Model(Statement):
    """Model definition"""
    name: str = ""
    dimensions: List['Dimension'] = field(default_factory=list)
    measures: List['Measure'] = field(default_factory=list)


@dataclass
class View(Statement):
    """View definition"""
    name: str = ""
    from_model: Optional[str] = None
    joins: List['Join'] = field(default_factory=list)
    extends: List[str] = field(default_factory=list)
    extension: Optional[str] = None  # "required" or "optional"


@dataclass
class Dimension(ASTNode):
    """Dimension definition within a model"""
    name: str = ""
    type: Optional[str] = None
    expression: Optional['DaxExpression'] = None
    primary_key: Optional[bool] = None
    value_format: Optional[Union[str, 'FormatName']] = None
    label: Optional[str] = None
    description: Optional[str] = None
    hidden: Optional[bool] = None
    tiers: Optional[List[Union[str, float]]] = None
    sql_latitude: Optional['DaxExpression'] = None
    sql_longitude: Optional['DaxExpression'] = None
    units: Optional[str] = None


@dataclass
class Measure(ASTNode):
    """Measure definition within a model"""
    name: str = ""
    type: Optional[str] = None
    expression: Optional['DaxExpression'] = None
    value_format: Optional[Union[str, 'FormatName']] = None
    label: Optional[str] = None
    description: Optional[str] = None
    hidden: Optional[bool] = None


@dataclass
class Join(ASTNode):
    """Join definition within a view"""
    name: str = ""
    type: Optional[str] = None  # left_outer, inner, full_outer, cross
    relationship: Optional[str] = None  # one_to_one, many_to_one, one_to_many, many_to_many
    expression: Optional['DaxExpression'] = None


@dataclass
class DaxExpression(ASTNode):
    """DAX expression - treated as opaque string"""
    raw_text: str = ""


@dataclass
class FormatName(ASTNode):
    """Named format (usd, eur, percent_1, etc.)"""
    name: str = ""


@dataclass
class StringLiteral(ASTNode):
    """String literal value"""
    value: str = ""


@dataclass
class NumberLiteral(ASTNode):
    """Numeric literal value"""
    value: float = 0.0


@dataclass
class BooleanLiteral(ASTNode):
    """Boolean literal value"""
    value: bool = False


@dataclass
class Identifier(ASTNode):
    """Identifier (variable name, etc.)"""
    name: str = ""


# Type aliases for common node types
DimensionType = str  # string, number, date, etc.
MeasureType = str    # count, sum, average, etc.
JoinType = str       # left_outer, inner, etc.
RelationshipType = str  # one_to_one, many_to_one, etc.
UnitsType = str      # miles, kilometers, etc.

# Valid enum values
DIMENSION_TYPES = {
    "string", "number", "date", "date_time", "yesno", 
    "tier", "bin", "location", "zipcode", "distance",
    "duration", "time", "unquoted"
}

MEASURE_TYPES = {
    "count", "sum", "average", "min", "max", 
    "count_distinct", "median", "percentile", "number"
}

JOIN_TYPES = {
    "left_outer", "inner", "full_outer", "cross"
}

RELATIONSHIP_TYPES = {
    "one_to_one", "many_to_one", "one_to_many", "many_to_many"
}

FORMAT_NAMES = {
    "usd", "eur", "gbp", 
    "percent_1", "percent_2",
    "decimal_0", "decimal_1", "decimal_2",
    "id"
}

UNITS = {
    "miles", "kilometers", "meters", "feet"
}