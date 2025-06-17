"""
Copper Language Parser

A parser for the Copper metadata format based on the EBNF grammar specification.
Treats DAX expressions as opaque strings for now.
"""

from .copper_parser import CopperParser, parse_file, parse_string
from .ast_nodes import *

__version__ = "0.1.0"
__all__ = ["CopperParser", "parse_file", "parse_string"]