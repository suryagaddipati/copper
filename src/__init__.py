"""
Copper - Universal Semantic Layer

A portable semantic layer that compiles metric definitions and queries 
into runtime code across multiple execution engines.

Copper = Define Once. Run Anywhere. ☄️
"""

__version__ = "0.1.0"

from semantic.loader import load
from query.builder import Query

__all__ = ["load", "Query"]