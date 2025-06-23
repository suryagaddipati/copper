"""
Minimal Copper language parser for emergency fallback
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


def validate_copper_syntax(content: str) -> Dict[str, Any]:
    """Minimal Copper syntax validation - emergency fallback"""
    
    models = []
    views = []
    errors = []
    warnings = []
    
    try:
        lines = content.split('\n')
        current_line = 0
        
        # Basic parsing - just look for models and views
        while current_line < len(lines):
            line = lines[current_line].strip()
            
            if line.startswith('model:'):
                model_match = re.match(r'model:\s*(\w+)', line)
                if model_match:
                    model_name = model_match.group(1)
                    
                    # Count dimensions and measures in this model
                    model_children = []
                    brace_count = 0
                    start_line = current_line
                    
                    # Find the model block
                    while current_line < len(lines):
                        line_content = lines[current_line]
                        brace_count += line_content.count('{') - line_content.count('}')
                        
                        # Look for dimensions and measures
                        if 'dimension:' in line_content:
                            dim_match = re.search(r'dimension:\s*(\w+)', line_content)
                            if dim_match:
                                dim_props = {}
                                if 'type:' in line_content or (current_line + 1 < len(lines) and 'type:' in lines[current_line + 1]):
                                    dim_props['type'] = 'string'  # Default
                                
                                model_children.append(ParsedNode(
                                    type=NodeType.DIMENSION,
                                    name=dim_match.group(1),
                                    properties=dim_props,
                                    children=[],
                                    line_number=current_line + 1
                                ))
                        
                        elif 'measure:' in line_content:
                            meas_match = re.search(r'measure:\s*(\w+)', line_content)
                            if meas_match:
                                meas_props = {}
                                if 'type:' in line_content or (current_line + 1 < len(lines) and 'type:' in lines[current_line + 1]):
                                    meas_props['type'] = 'count'  # Default
                                
                                model_children.append(ParsedNode(
                                    type=NodeType.MEASURE,
                                    name=meas_match.group(1),
                                    properties=meas_props,
                                    children=[],
                                    line_number=current_line + 1
                                ))
                        
                        if brace_count == 0 and current_line > start_line:
                            break
                        current_line += 1
                    
                    models.append(ParsedNode(
                        type=NodeType.MODEL,
                        name=model_name,
                        properties={},
                        children=model_children,
                        line_number=start_line + 1
                    ))
            
            elif line.startswith('view:'):
                view_match = re.match(r'view:\s*(\w+)', line)
                if view_match:
                    view_name = view_match.group(1)
                    views.append(ParsedNode(
                        type=NodeType.VIEW,
                        name=view_name,
                        properties={},
                        children=[],
                        line_number=current_line + 1
                    ))
            
            current_line += 1
        
        # Basic validation
        if not models and not views:
            errors.append("No models or views found")
        
    except Exception as e:
        errors.append(f"Parse error: {str(e)}")
    
    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
        "models": models,
        "views": views,
        "statistics": {
            "total_models": len(models),
            "total_views": len(views),
            "total_dimensions": sum(len([c for c in m.children if c.type == NodeType.DIMENSION]) for m in models),
            "total_measures": sum(len([c for c in m.children if c.type == NodeType.MEASURE]) for m in models),
            "total_joins": 0
        }
    }