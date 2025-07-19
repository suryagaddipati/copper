from typing import Optional, Dict, Any
from pydantic import BaseModel
from .dimension import DataType
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
import src as copper


class Measure(BaseModel):
    """Measure with expression and calculate method."""
    
    expression: str
    type: DataType = DataType.NUMBER
    label: Optional[str] = None
    description: Optional[str] = None
    format: Optional[str] = None
    
    def calculate(self, model, data_dict: Dict[str, Any]) -> Any:
        """Calculate the measure value using direct pandas execution."""
        from ..executors.pandas_executor import PandasExecutor
        from ..parser.antlr_parser import CopperParser
        
        # Parse the expression
        parser = CopperParser()
        ast = parser.parse(self.expression)
        
        # Execute directly with pandas
        executor = PandasExecutor()
        result = executor.execute(ast, data_dict)
        
        return result