from typing import Optional, Dict, Any
from pydantic import BaseModel
from .dimension import DataType
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
import src as copper


class Measure(BaseModel):
    
    expression: str
    type: DataType = DataType.NUMBER
    label: Optional[str] = None
    description: Optional[str] = None
    format: Optional[str] = None
    
    def calculate(self, model, data_dict: Dict[str, Any]) -> Any:
        from ..executors.pandas_executor import PandasCodeGenerator
        from ..parser.antlr_parser import CopperParser
        import numpy as np
        
        parser = CopperParser()
        ast = parser.parse(self.expression)
        
        generator = PandasCodeGenerator(data_dict)
        code = ast.accept(generator)
        
        local_vars = data_dict.copy()
        local_vars['np'] = np
        
        try:
            result = eval(code, {"__builtins__": {}}, local_vars)
            return result
        except Exception as e:
            raise ValueError(f"Could not evaluate measure expression '{code}': {e}")