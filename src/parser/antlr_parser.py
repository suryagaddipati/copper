"""
ANTLR-based Copper language parser for live parsing demo
"""
import sys
import os
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from enum import Enum

# Add the generated parser to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'generated'))

from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from antlr4.error.ErrorListener import ErrorListener
from CopperLexer import CopperLexer
from CopperParser import CopperParser
from CopperListener import CopperListener


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
        self.warnings = []
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Filter out token recognition errors for common DAX operators
        if "token recognition error" in msg:
            # These are common in DAX expressions and should be warnings, not errors
            if any(char in msg for char in ["'='", "'.'", "'+'", "'-'", "'*'", "'/'", "'('", "')'", "'<'", "'>'", "'!'", "'?'", "'&'", "'|'", "'%'", "'^'"]):
                # Convert to warning instead of error for DAX operator tokens
                warning_msg = f"Line {line}:{column} - Possible DAX syntax: {msg}"
                self.warnings.append(warning_msg)
                return
        
        error_msg = f"Line {line}:{column} - {msg}"
        self.errors.append(error_msg)


class CopperParseTreeListener(CopperListener):
    """Parse tree listener to extract structured data from ANTLR parse tree"""
    
    def __init__(self):
        super().__init__()
        self.nodes = []
        self.current_node = None
        self.node_stack = []
        self.errors = []
        self.warnings = []

    def _add_error(self, message, line_number):
        self.errors.append(f"Line {line_number}: {message}")

    def _add_warning(self, message, line_number):
        self.warnings.append(f"Line {line_number}: {message}")

    def _enter_node(self, node_type, name, ctx):
        new_node = ParsedNode(
            type=node_type,
            name=name,
            properties={},
            children=[],
            line_number=ctx.start.line
        )
        if self.current_node:
            self.current_node.children.append(new_node)
        else:
            self.nodes.append(new_node)
        
        self.node_stack.append(self.current_node)
        self.current_node = new_node

    def _exit_node(self):
        if self.node_stack:
            self.current_node = self.node_stack.pop()

    def enterModelStatement(self, ctx):
        if ctx.identifier():
            self._enter_node(NodeType.MODEL, ctx.identifier().getText(), ctx)
    
    def exitModelStatement(self, ctx):
        self._exit_node()
    
    def enterViewStatement(self, ctx):
        if ctx.identifier():
            self._enter_node(NodeType.VIEW, ctx.identifier().getText(), ctx)
    
    def exitViewStatement(self, ctx):
        self._exit_node()
    
    def enterDimensionStatement(self, ctx):
        if ctx.identifier():
            self._enter_node(NodeType.DIMENSION, ctx.identifier().getText(), ctx)
    
    def exitDimensionStatement(self, ctx):
        self._exit_node()
    
    def enterMeasureStatement(self, ctx):
        if ctx.identifier():
            self._enter_node(NodeType.MEASURE, ctx.identifier().getText(), ctx)
    
    def exitMeasureStatement(self, ctx):
        self._exit_node()
    
    def enterJoinStatement(self, ctx):
        if ctx.identifier():
            self._enter_node(NodeType.JOIN, ctx.identifier().getText(), ctx)
    
    def exitJoinStatement(self, ctx):
        self._exit_node()
    
    def enterTypeParameter(self, ctx):
        if self.current_node:
            if ctx.dimensionType():
                self.current_node.properties['type'] = ctx.dimensionType().getText()

    def enterMeasureTypeParameter(self, ctx):
        if self.current_node and ctx.measureType():
            self.current_node.properties['type'] = ctx.measureType().getText()

    def enterExpressionParameter(self, ctx):
        if self.current_node:
            dax_text = ""
            if hasattr(ctx, 'daxExpression') and ctx.daxExpression():
                dax_expr_ctx = ctx.daxExpression()
                if hasattr(dax_expr_ctx, 'daxContent') and dax_expr_ctx.daxContent():
                    dax_text = dax_expr_ctx.daxContent().getText()
                else:
                    full_text = dax_expr_ctx.getText()
                    dax_text = full_text.rstrip(';').strip()
            
            if dax_text:
                self.current_node.properties['expression'] = dax_text
                try:
                    from dax_parser import validate_dax_expression
                    validation_result = validate_dax_expression(dax_text)
                    self.current_node.properties['dax_validation'] = validation_result
                    if not validation_result['valid']:
                        for error in validation_result['errors']:
                            self._add_error(f"DAX validation error: {error}", ctx.start.line)
                except ImportError:
                    pass
    
    def enterLabelParameter(self, ctx):
        if self.current_node and ctx.stringLiteral():
            label_text = ctx.stringLiteral().getText()
            if label_text.startswith('"') and label_text.endswith('"'):
                label_text = label_text[1:-1]
            self.current_node.properties['label'] = label_text
    
    def enterDescriptionParameter(self, ctx):
        if self.current_node and ctx.stringLiteral():
            desc_text = ctx.stringLiteral().getText()
            if desc_text.startswith('"') and desc_text.endswith('"'):
                desc_text = desc_text[1:-1]
            self.current_node.properties['description'] = desc_text
    
    def enterPrimaryKeyParameter(self, ctx):
        if self.current_node and ctx.booleanValue():
            value = ctx.booleanValue().getText().lower()
            self.current_node.properties['primary_key'] = value in ['yes', 'true']
    
    def enterHiddenParameter(self, ctx):
        if self.current_node and ctx.booleanValue():
            value = ctx.booleanValue().getText().lower()
            self.current_node.properties['hidden'] = value in ['yes', 'true']
    
    def enterValueFormatParameter(self, ctx):
        if self.current_node:
            if ctx.stringLiteral():
                self.current_node.properties['value_format'] = ctx.stringLiteral().getText().strip('"')
            elif ctx.formatName():
                self.current_node.properties['value_format'] = ctx.formatName().getText()

    def enterUnitsParameter(self, ctx):
        if self.current_node and ctx.stringLiteral():
            self.current_node.properties['units'] = ctx.stringLiteral().getText().strip('"')

    def enterFromStatement(self, ctx):
        if self.current_node and ctx.identifier():
            self.current_node.properties['from'] = ctx.identifier().getText()
    
    def enterExtendsStatement(self, ctx):
        if self.current_node and ctx.identifierList():
            self.current_node.properties['extends'] = [ident.getText() for ident in ctx.identifierList().identifier()]

    def enterJoinTypeParameter(self, ctx):
        if self.current_node and ctx.joinType():
            self.current_node.properties['type'] = ctx.joinType().getText()

    def enterRelationshipParameter(self, ctx):
        if self.current_node and ctx.relationshipType():
            self.current_node.properties['relationship'] = ctx.relationshipType().getText()


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
            lexer = CopperLexer(input_stream)
            
            # Create error listener
            error_listener = CopperErrorListener()
            lexer.removeErrorListeners()
            lexer.addErrorListener(error_listener)
            
            # Create token stream
            stream = CommonTokenStream(lexer)
            
            # Create parser
            parser = CopperParser(stream)
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
            self.warnings.extend(error_listener.warnings)
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