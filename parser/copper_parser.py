"""
Main Copper Parser Interface

Provides the public API for parsing Copper files and strings.
"""

from typing import Union, Optional
from pathlib import Path
import json

try:
    from .tokenizer import CopperTokenizer
    from .parser import CopperParser, ParseError
    from .ast_nodes import Program, ASTNode
except ImportError:
    from tokenizer import CopperTokenizer
    from parser import CopperParser, ParseError
    from ast_nodes import Program, ASTNode


class CopperParseResult:
    """Result of parsing a Copper file or string"""
    
    def __init__(self, ast: Optional[Program] = None, error: Optional[ParseError] = None):
        self.ast = ast
        self.error = error
        self.success = error is None
    
    def __str__(self) -> str:
        if self.success:
            return f"Parse successful: {len(self.ast.statements)} statements"
        else:
            return f"Parse failed: {self.error}"


def parse_string(source: str) -> CopperParseResult:
    """
    Parse a Copper source string
    
    Args:
        source: The Copper source code as a string
        
    Returns:
        CopperParseResult containing the AST or error information
    """
    try:
        # Tokenize
        tokenizer = CopperTokenizer(source)
        tokens = tokenizer.tokenize()
        
        # Parse
        parser = CopperParser(tokens)
        ast = parser.parse()
        
        return CopperParseResult(ast=ast)
    
    except (ParseError, SyntaxError) as e:
        error = e if isinstance(e, ParseError) else ParseError(str(e))
        return CopperParseResult(error=error)
    except Exception as e:
        error = ParseError(f"Unexpected error: {e}")
        return CopperParseResult(error=error)


def parse_file(file_path: Union[str, Path]) -> CopperParseResult:
    """
    Parse a Copper file
    
    Args:
        file_path: Path to the .copper file
        
    Returns:
        CopperParseResult containing the AST or error information
    """
    try:
        path = Path(file_path)
        if not path.exists():
            return CopperParseResult(error=ParseError(f"File not found: {file_path}"))
        
        if not path.suffix.lower() == '.copper':
            return CopperParseResult(error=ParseError(f"Expected .copper file, got: {path.suffix}"))
        
        with open(path, 'r', encoding='utf-8') as f:
            source = f.read()
        
        result = parse_string(source)
        return result
    
    except IOError as e:
        return CopperParseResult(error=ParseError(f"Error reading file: {e}"))
    except Exception as e:
        return CopperParseResult(error=ParseError(f"Unexpected error: {e}"))


def ast_to_dict(node: ASTNode) -> dict:
    """
    Convert an AST node to a dictionary representation
    
    Args:
        node: The AST node to convert
        
    Returns:
        Dictionary representation of the AST node
    """
    if node is None:
        return None
    
    result = {
        'type': node.__class__.__name__,
        'line': node.line,
        'column': node.column
    }
    
    for field_name, field_value in node.__dict__.items():
        if field_name in ['line', 'column']:
            continue
        
        if isinstance(field_value, ASTNode):
            result[field_name] = ast_to_dict(field_value)
        elif isinstance(field_value, list):
            result[field_name] = [
                ast_to_dict(item) if isinstance(item, ASTNode) else item
                for item in field_value
            ]
        else:
            result[field_name] = field_value
    
    return result


def pretty_print_ast(ast: Program, indent: int = 0) -> str:
    """
    Pretty print an AST for debugging
    
    Args:
        ast: The AST to print
        indent: Current indentation level
        
    Returns:
        Formatted string representation of the AST
    """
    def _indent(level: int) -> str:
        return "  " * level
    
    def _print_node(node: ASTNode, level: int) -> str:
        if node is None:
            return f"{_indent(level)}None"
        
        lines = [f"{_indent(level)}{node.__class__.__name__}:"]
        
        for field_name, field_value in node.__dict__.items():
            if field_name in ['line', 'column']:
                continue
            
            if isinstance(field_value, ASTNode):
                lines.append(f"{_indent(level + 1)}{field_name}:")
                lines.append(_print_node(field_value, level + 2))
            elif isinstance(field_value, list) and field_value:
                lines.append(f"{_indent(level + 1)}{field_name}: [")
                for item in field_value:
                    if isinstance(item, ASTNode):
                        lines.append(_print_node(item, level + 2))
                    else:
                        lines.append(f"{_indent(level + 2)}{repr(item)}")
                lines.append(f"{_indent(level + 1)}]")
            elif field_value is not None:
                lines.append(f"{_indent(level + 1)}{field_name}: {repr(field_value)}")
        
        return "\n".join(lines)
    
    return _print_node(ast, indent)


class CopperParserCLI:
    """Command-line interface for the Copper parser"""
    
    @staticmethod
    def validate_file(file_path: str) -> bool:
        """
        Validate a Copper file
        
        Args:
            file_path: Path to the file to validate
            
        Returns:
            True if valid, False otherwise
        """
        result = parse_file(file_path)
        if result.success:
            print(f"✓ {file_path}: Valid Copper file")
            print(f"  Found {len(result.ast.statements)} statements")
            
            # Count models and views
            models = sum(1 for stmt in result.ast.statements if stmt.__class__.__name__ == 'Model')
            views = sum(1 for stmt in result.ast.statements if stmt.__class__.__name__ == 'View')
            
            if models > 0:
                print(f"  Models: {models}")
            if views > 0:
                print(f"  Views: {views}")
            
            return True
        else:
            print(f"✗ {file_path}: Parse error")
            print(f"  {result.error}")
            return False
    
    @staticmethod
    def dump_ast(file_path: str, format: str = 'pretty') -> bool:
        """
        Dump the AST of a Copper file
        
        Args:
            file_path: Path to the file to parse
            format: Output format ('pretty', 'json')
            
        Returns:
            True if successful, False otherwise
        """
        result = parse_file(file_path)
        if not result.success:
            print(f"Parse error: {result.error}")
            return False
        
        if format == 'json':
            ast_dict = ast_to_dict(result.ast)
            print(json.dumps(ast_dict, indent=2))
        else:  # pretty
            print(pretty_print_ast(result.ast))
        
        return True


# Convenience functions for backward compatibility
def main_parse_file(file_path: str) -> Program:
    """Parse a file and return the AST (raises exception on error)"""
    result = parse_file(file_path)
    if not result.success:
        raise result.error
    return result.ast


def main_parse_string(source: str) -> Program:
    """Parse a string and return the AST (raises exception on error)"""
    result = parse_string(source)
    if not result.success:
        raise result.error
    return result.ast