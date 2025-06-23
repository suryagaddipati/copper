"""
ANTLR-based Copper language parser for live parsing demo
"""
import sys
import os
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from enum import Enum

# Add the generated parser to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'grammar', 'build', 'python'))

try:
    from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
    from antlr4.error.ErrorListener import ErrorListener
    from CopperSimpleLexer import CopperSimpleLexer
    from CopperSimpleParser import CopperSimpleParser
    from CopperSimpleListener import CopperSimpleListener
    ANTLR_AVAILABLE = True
except ImportError:
    ANTLR_AVAILABLE = False
    # Mock classes for when ANTLR is not available
    class ErrorListener:
        pass
    class CopperSimpleListener:
        pass


class NodeType(Enum):
    MODEL = "model"
    VIEW = "view"
    DIMENSION = "dimension"
    MEASURE = "measure"
    JOIN = "join"
    PARAMETER = "parameter"


@dataclass
class ParsedNode:
    type: NodeType
    name: str
    properties: Dict[str, Any]
    children: List['ParsedNode']
    line_number: int


@dataclass
class ParseResult:
    success: bool
    nodes: List[ParsedNode]
    errors: List[str]
    warnings: List[str]


class CopperErrorListener(ErrorListener):
    """Custom error listener for collecting parse errors"""
    
    def __init__(self):
        super().__init__()
        self.errors = []
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_msg = f"Line {line}:{column} - {msg}"
        self.errors.append(error_msg)


class CopperParseTreeListener(CopperSimpleListener):
    """Parse tree listener to extract structured data from ANTLR parse tree"""
    
    def __init__(self):
        super().__init__()
        self.nodes = []
        self.current_node = None
        self.node_stack = []
        self.errors = []
        self.warnings = []
    
    def enterModelStatement(self, ctx):
        """Enter a model statement"""
        if ctx.identifier():
            name = ctx.identifier().getText()
            model_node = ParsedNode(
                type=NodeType.MODEL,
                name=name,
                properties={},
                children=[],
                line_number=ctx.start.line
            )
            self.nodes.append(model_node)
            self.node_stack.append(self.current_node)
            self.current_node = model_node
    
    def exitModelStatement(self, ctx):
        """Exit a model statement"""
        self.current_node = self.node_stack.pop() if self.node_stack else None
    
    def enterViewStatement(self, ctx):
        """Enter a view statement"""
        if ctx.identifier():
            name = ctx.identifier().getText()
            view_node = ParsedNode(
                type=NodeType.VIEW,
                name=name,
                properties={},
                children=[],
                line_number=ctx.start.line
            )
            self.nodes.append(view_node)
            self.node_stack.append(self.current_node)
            self.current_node = view_node
    
    def exitViewStatement(self, ctx):
        """Exit a view statement"""
        self.current_node = self.node_stack.pop() if self.node_stack else None
    
    def enterDimensionStatement(self, ctx):
        """Enter a dimension statement"""
        if ctx.identifier() and self.current_node:
            name = ctx.identifier().getText()
            dimension_node = ParsedNode(
                type=NodeType.DIMENSION,
                name=name,
                properties={},
                children=[],
                line_number=ctx.start.line
            )
            self.current_node.children.append(dimension_node)
            self.node_stack.append(self.current_node)
            self.current_node = dimension_node
    
    def exitDimensionStatement(self, ctx):
        """Exit a dimension statement"""
        if self.node_stack:
            self.current_node = self.node_stack.pop()
    
    def enterMeasureStatement(self, ctx):
        """Enter a measure statement"""
        if ctx.identifier() and self.current_node:
            name = ctx.identifier().getText()
            measure_node = ParsedNode(
                type=NodeType.MEASURE,
                name=name,
                properties={},
                children=[],
                line_number=ctx.start.line
            )
            self.current_node.children.append(measure_node)
            self.node_stack.append(self.current_node)
            self.current_node = measure_node
    
    def exitMeasureStatement(self, ctx):
        """Exit a measure statement"""
        if self.node_stack:
            self.current_node = self.node_stack.pop()
    
    def enterJoinStatement(self, ctx):
        """Enter a join statement"""
        if ctx.identifier() and self.current_node:
            name = ctx.identifier().getText()
            join_node = ParsedNode(
                type=NodeType.JOIN,
                name=name,
                properties={},
                children=[],
                line_number=ctx.start.line
            )
            self.current_node.children.append(join_node)
            self.node_stack.append(self.current_node)
            self.current_node = join_node
    
    def exitJoinStatement(self, ctx):
        """Exit a join statement"""
        if self.node_stack:
            self.current_node = self.node_stack.pop()
    
    def enterTypeParameter(self, ctx):
        """Enter a type parameter"""
        if self.current_node and ctx.typeValue():
            self.current_node.properties['type'] = ctx.typeValue().getText()
    
    def enterExpressionParameter(self, ctx):
        """Enter an expression parameter"""
        if self.current_node and ctx.daxExpression():
            # Extract DAX expression, removing the leading colon and trailing semicolons
            dax_text = ctx.daxExpression().getText()
            if dax_text.startswith(':'):
                dax_text = dax_text[1:]
            if dax_text.endswith(';;'):
                dax_text = dax_text[:-2]
            self.current_node.properties['expression'] = dax_text.strip()
    
    def enterLabelParameter(self, ctx):
        """Enter a label parameter"""
        if self.current_node and ctx.stringValue():
            label_text = ctx.stringValue().getText()
            # Remove quotes if present
            if label_text.startswith('"') and label_text.endswith('"'):
                label_text = label_text[1:-1]
            self.current_node.properties['label'] = label_text
    
    def enterDescriptionParameter(self, ctx):
        """Enter a description parameter"""
        if self.current_node and ctx.stringValue():
            desc_text = ctx.stringValue().getText()
            # Remove quotes if present
            if desc_text.startswith('"') and desc_text.endswith('"'):
                desc_text = desc_text[1:-1]
            self.current_node.properties['description'] = desc_text
    
    def enterPrimaryKeyParameter(self, ctx):
        """Enter a primary_key parameter"""
        if self.current_node and ctx.booleanValue():
            value = ctx.booleanValue().getText().lower()
            self.current_node.properties['primary_key'] = value == 'yes'
    
    def enterHiddenParameter(self, ctx):
        """Enter a hidden parameter"""
        if self.current_node and ctx.booleanValue():
            value = ctx.booleanValue().getText().lower()
            self.current_node.properties['hidden'] = value == 'yes'
    
    def enterValueFormatParameter(self, ctx):
        """Enter a value_format parameter"""
        if self.current_node and ctx.formatValue():
            self.current_node.properties['value_format'] = ctx.formatValue().getText()
    
    def enterUnitsParameter(self, ctx):
        """Enter a units parameter"""
        if self.current_node and ctx.stringValue():
            units_text = ctx.stringValue().getText()
            # Remove quotes if present
            if units_text.startswith('"') and units_text.endswith('"'):
                units_text = units_text[1:-1]
            self.current_node.properties['units'] = units_text
    
    def enterFromParameter(self, ctx):
        """Enter a from parameter"""
        if self.current_node and ctx.identifier():
            self.current_node.properties['from'] = ctx.identifier().getText()
    
    def enterExtendsParameter(self, ctx):
        """Enter an extends parameter"""
        if self.current_node and ctx.identifier():
            self.current_node.properties['extends'] = ctx.identifier().getText()
    
    def enterRelationshipParameter(self, ctx):
        """Enter a relationship parameter"""
        if self.current_node and ctx.relationshipValue():
            self.current_node.properties['relationship'] = ctx.relationshipValue().getText()


class CopperANTLRParser:
    """ANTLR-based parser for Copper language syntax"""
    
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.nodes = []
        self.errors = []
        self.warnings = []
    
    def parse(self, content: str) -> ParseResult:
        """Parse Copper content and return structured result"""
        self.reset()
        
        try:
            # Create input stream
            input_stream = InputStream(content)
            
            # Create lexer
            lexer = CopperSimpleLexer(input_stream)
            
            # Create error listener
            error_listener = CopperErrorListener()
            lexer.removeErrorListeners()
            lexer.addErrorListener(error_listener)
            
            # Create token stream
            stream = CommonTokenStream(lexer)
            
            # Create parser
            parser = CopperSimpleParser(stream)
            parser.removeErrorListeners()
            parser.addErrorListener(error_listener)
            
            # Parse the input
            tree = parser.program()
            
            # Walk the parse tree
            listener = CopperParseTreeListener()
            walker = ParseTreeWalker()
            walker.walk(listener, tree)
            
            # Collect results
            self.nodes = listener.nodes
            self.errors.extend(error_listener.errors)
            self.errors.extend(listener.errors)
            self.warnings.extend(listener.warnings)
            
            # Validate parsed content
            self._validate_nodes()
            
        except Exception as e:
            self.errors.append(f"Parse error: {str(e)}")
        
        return ParseResult(
            success=len(self.errors) == 0,
            nodes=self.nodes,
            errors=self.errors,
            warnings=self.warnings
        )
    
    def _validate_nodes(self):
        """Validate parsed nodes and add warnings/errors"""
        for node in self.nodes:
            if node.type == NodeType.MODEL and not node.children:
                self.warnings.append(f"Line {node.line_number}: Model '{node.name}' has no dimensions or measures")
            
            # Validate required properties for dimensions and measures
            for child in node.children:
                if child.type in [NodeType.DIMENSION, NodeType.MEASURE]:
                    if 'type' not in child.properties:
                        self.errors.append(f"Line {child.line_number}: {child.type.value} '{child.name}' missing required 'type' property")


def validate_copper_syntax(content: str) -> Dict[str, Any]:
    """Validate Copper syntax and return analysis using ANTLR parser"""
    if not ANTLR_AVAILABLE:
        # Temporary fallback to minimal parser
        print("⚠️  ANTLR not available, using minimal fallback parser")
        from copper_parser_minimal import validate_copper_syntax as minimal_parser
        return minimal_parser(content)
    
    parser = CopperANTLRParser()
    result = parser.parse(content)
    
    # Convert to same format as original parser for API compatibility
    analysis = {
        "valid": result.success,
        "errors": result.errors,
        "warnings": result.warnings,
        "models": [node for node in result.nodes if node.type == NodeType.MODEL],
        "views": [node for node in result.nodes if node.type == NodeType.VIEW],
        "statistics": {
            "total_models": len([n for n in result.nodes if n.type == NodeType.MODEL]),
            "total_views": len([n for n in result.nodes if n.type == NodeType.VIEW]),
            "total_dimensions": sum(len([c for c in n.children if c.type == NodeType.DIMENSION]) for n in result.nodes),
            "total_measures": sum(len([c for c in n.children if c.type == NodeType.MEASURE]) for n in result.nodes),
            "total_joins": sum(len([c for c in n.children if c.type == NodeType.JOIN]) for n in result.nodes)
        }
    }
    
    return analysis