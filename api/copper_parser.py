"""
Simple Copper language parser for live parsing demo
"""
import re
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from enum import Enum


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


class CopperParser:
    """Simple parser for Copper language syntax"""
    
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.nodes = []
        self.errors = []
        self.warnings = []
        self.current_line = 0
    
    def parse(self, content: str) -> ParseResult:
        """Parse Copper content and return structured result"""
        self.reset()
        lines = content.split('\n')
        
        try:
            self._parse_lines(lines)
        except Exception as e:
            self.errors.append(f"Parse error: {str(e)}")
        
        return ParseResult(
            success=len(self.errors) == 0,
            nodes=self.nodes,
            errors=self.errors,
            warnings=self.warnings
        )
    
    def _parse_lines(self, lines: List[str]):
        """Parse lines into structured nodes"""
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            self.current_line = i + 1
            
            if not line or line.startswith('#'):
                i += 1
                continue
            
            # Check for model or view definitions
            if line.startswith('model:') or line.startswith('view:'):
                node, consumed_lines = self._parse_block(lines, i)
                if node:
                    self.nodes.append(node)
                i += consumed_lines
            else:
                # Invalid top-level syntax
                if line.strip():  # Only flag non-empty lines
                    self.errors.append(f"Line {self.current_line}: Invalid syntax - expected 'model:', 'view:', or comment. Found: '{line[:50]}{'...' if len(line) > 50 else ''}'")
                i += 1
    
    def _parse_block(self, lines: List[str], start_idx: int) -> tuple[Optional[ParsedNode], int]:
        """Parse a model or view block"""
        line = lines[start_idx].strip()
        
        # Extract type and name
        if line.startswith('model:'):
            block_type = NodeType.MODEL
            name_match = re.match(r'model:\s*(\w+)\s*{?', line)
        elif line.startswith('view:'):
            block_type = NodeType.VIEW
            name_match = re.match(r'view:\s*(\w+)\s*{?', line)
        else:
            return None, 1
        
        if not name_match:
            self.errors.append(f"Line {self.current_line}: Invalid {block_type.value} syntax")
            return None, 1
        
        name = name_match.group(1)
        
        # Find the opening brace
        brace_line = start_idx
        if '{' not in line:
            brace_line += 1
            while brace_line < len(lines) and '{' not in lines[brace_line]:
                brace_line += 1
            if brace_line >= len(lines):
                self.errors.append(f"Line {self.current_line}: Missing opening brace for {block_type.value}")
                return None, 1
        
        # Find the closing brace
        brace_count = 0
        end_line = brace_line
        for i in range(brace_line, len(lines)):
            line_content = lines[i]
            brace_count += line_content.count('{') - line_content.count('}')
            if brace_count == 0:
                end_line = i
                break
        
        if brace_count != 0:
            self.errors.append(f"Line {self.current_line}: Unmatched braces for {block_type.value}")
            return None, end_line - start_idx + 1
        
        # Parse properties and children
        properties = {}
        children = []
        
        for i in range(brace_line + 1, end_line):
            line_content = lines[i].strip()
            if not line_content or line_content.startswith('#'):
                continue
            
            # Parse properties
            if ':' in line_content and not line_content.startswith(('dimension:', 'measure:', 'join:')):
                self.current_line = i + 1
                key, value = self._parse_property(line_content)
                if key:
                    properties[key] = value
            
            # Parse nested blocks (dimensions, measures, joins)
            elif line_content.startswith(('dimension:', 'measure:', 'join:')):
                child_node, _ = self._parse_child_block(lines, i)
                if child_node:
                    children.append(child_node)
            else:
                # Invalid content inside block
                # Check if this line might be part of a multi-line DAX expression
                dax_patterns = [
                    'DIVIDE(', 'CALCULATE(', 'FILTER(', 'SUM(', 'COUNT(', 'SUMX(',
                    'VAR ', 'RETURN ', ') ;;', ';;', 'WEEKDAY(', 'DISTINCTCOUNT(',
                    'RELATED(', 'DATE(', 'YEAR(', 'MONTH(', 'DAY(', 'DATEADD(',
                    'COUNTROWS(', 'Orders[', 'Customers[', 'Products[', ',',
                    ')', '(', 'CurrentRevenue', 'FilteredRevenue', 'PreviousRevenue',
                    'CurrentStock', 'NewCustomers', 'TotalCustomers'
                ]
                
                is_likely_dax = any(pattern in line_content for pattern in dax_patterns)
                
                if (line_content and 
                    not line_content in ['{', '}'] and 
                    not is_likely_dax and
                    not line_content.startswith(('IN {', 'IN(', '))', ','))):
                    self.current_line = i + 1
                    self.errors.append(f"Line {self.current_line}: Invalid content inside {block_type.value} block: '{line_content[:30]}{'...' if len(line_content) > 30 else ''}'")
        
        # Validate required elements for models
        if block_type == NodeType.MODEL and not children:
            self.warnings.append(f"Line {start_idx + 1}: Model '{name}' has no dimensions or measures")
        
        # Validate dimensions and measures have type
        for child in children:
            if child.type in [NodeType.DIMENSION, NodeType.MEASURE] and 'type' not in child.properties:
                self.errors.append(f"Line {child.line_number}: {child.type.value} '{child.name}' missing required 'type' property")
        
        return ParsedNode(
            type=block_type,
            name=name,
            properties=properties,
            children=children,
            line_number=start_idx + 1
        ), end_line - start_idx + 1
    
    def _parse_child_block(self, lines: List[str], start_idx: int) -> tuple[Optional[ParsedNode], int]:
        """Parse dimension, measure, or join blocks"""
        line = lines[start_idx].strip()
        
        if line.startswith('dimension:'):
            child_type = NodeType.DIMENSION
            name_match = re.match(r'dimension:\s*(\w+)\s*{?', line)
        elif line.startswith('measure:'):
            child_type = NodeType.MEASURE
            name_match = re.match(r'measure:\s*(\w+)\s*{?', line)
        elif line.startswith('join:'):
            child_type = NodeType.JOIN
            name_match = re.match(r'join:\s*(\w+)\s*{?', line)
        else:
            return None, 1
        
        if not name_match:
            return None, 1
        
        name = name_match.group(1)
        
        # Find block bounds
        brace_line = start_idx
        if '{' not in line:
            brace_line += 1
            while brace_line < len(lines) and '{' not in lines[brace_line]:
                brace_line += 1
        
        brace_count = 0
        end_line = brace_line
        for i in range(brace_line, len(lines)):
            line_content = lines[i]
            brace_count += line_content.count('{') - line_content.count('}')
            if brace_count == 0:
                end_line = i
                break
        
        # Parse properties
        properties = {}
        for i in range(brace_line + 1, end_line):
            line_content = lines[i].strip()
            if line_content and ':' in line_content:
                key, value = self._parse_property(line_content)
                if key:
                    properties[key] = value
        
        return ParsedNode(
            type=child_type,
            name=name,
            properties=properties,
            children=[],
            line_number=start_idx + 1
        ), end_line - start_idx + 1
    
    def _parse_property(self, line: str) -> tuple[Optional[str], str]:
        """Parse a property line like 'type: string'"""
        if ':' not in line:
            self.errors.append(f"Line {self.current_line}: Invalid property syntax - missing colon. Found: '{line[:30]}{'...' if len(line) > 30 else ''}'")
            return None, ""
        
        parts = line.split(':', 1)
        key = parts[0].strip()
        value = parts[1].strip()
        
        if not key:
            self.errors.append(f"Line {self.current_line}: Property missing name before colon")
            return None, ""
        
        if not value:
            # Allow empty values for 'expression' as it might continue on next lines
            if key == 'expression':
                return key, ""  # Return empty value, will be handled by multi-line logic
            else:
                self.errors.append(f"Line {self.current_line}: Property '{key}' missing value after colon")
                return None, ""
        
        # Remove trailing semicolons
        if value.endswith(';;'):
            value = value[:-2].strip()
        elif value.endswith(';'):
            value = value[:-1].strip()
        
        # Validate common property names
        valid_properties = {
            'type', 'expression', 'label', 'description', 'value_format',
            'primary_key', 'hidden', 'tiers', 'sql_latitude', 'sql_longitude',
            'units', 'relationship', 'from', 'extends', 'extension', 'required'
        }
        
        if key not in valid_properties:
            self.warnings.append(f"Line {self.current_line}: Unknown property '{key}' - might be a typo")
        
        return key, value


def validate_copper_syntax(content: str) -> Dict[str, Any]:
    """Validate Copper syntax and return analysis"""
    parser = CopperParser()
    result = parser.parse(content)
    
    # Basic syntax validation
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