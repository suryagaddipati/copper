import pandas as pd
from typing import Dict, Any, List, Optional
from ..parser.antlr_parser import CopperParser
from ..parser.ast_nodes import *


class PandasCodeGenerator(ASTVisitor):
    
    def __init__(self, dataframes: Dict[str, pd.DataFrame]):
        self.dataframes = dataframes
        self.current_df_name = None
    
    def visit_literal(self, node: Literal) -> str:
        if node.type == 'string':
            return f"'{node.value}'"
        elif node.type == 'null':
            return 'None'
        else:
            return str(node.value)
    
    def visit_identifier(self, node: Identifier) -> str:
        return node.name
    
    def visit_column_reference(self, node: ColumnReference) -> str:
        if node.table:
            return f"{node.table}['{node.column}']"
        else:
            return f"df['{node.column}']"
    
    def visit_binary_operation(self, node: BinaryOperation) -> str:
        left = node.left.accept(self)
        right = node.right.accept(self)
        
        operator_map = {
            '=': '==',
            '<>': '!=',
            '!=': '!=',
            'AND': '&',
            'OR': '|',
        }
        
        op = operator_map.get(node.operator, node.operator)
        
        if op in ['&', '|']:
            return f"({left}) {op} ({right})"
        else:
            return f"{left} {op} {right}"
    
    def visit_unary_operation(self, node: UnaryOperation) -> str:
        operand = node.operand.accept(self)
        
        if node.operator == 'NOT':
            return f"~({operand})"
        elif node.operator == '-':
            return f"-({operand})"
        else:
            return f"{node.operator}({operand})"
    
    def visit_function_call(self, node: FunctionCall) -> str:
        func_name = node.function_name.upper()
        args = [arg.accept(self) for arg in node.arguments]
        
        if func_name == 'SUM':
            return f"({args[0]}).sum()"
        elif func_name == 'COUNT':
            return f"({args[0]}).count()"
        elif func_name == 'AVG':
            return f"({args[0]}).mean()"
        elif func_name == 'MIN':
            return f"({args[0]}).min()"
        elif func_name == 'MAX':
            return f"({args[0]}).max()"
        elif func_name == 'COALESCE':
            result = args[0]
            for arg in args[1:]:
                result = f"({result}).fillna({arg})"
            return result
        else:
            args_str = ', '.join(args)
            return f"{func_name.lower()}({args_str})"
    
    def visit_if_expression(self, node: IfExpression) -> str:
        condition = node.condition.accept(self)
        true_val = node.true_value.accept(self)
        false_val = node.false_value.accept(self)
        
        return f"np.where({condition}, {true_val}, {false_val})"
    
    def visit_switch_expression(self, node: SwitchExpression) -> str:
        expr = node.expression.accept(self)
        
        result = None
        if node.default_value:
            result = node.default_value.accept(self)
        else:
            result = "None"
        
        for case in reversed(node.cases):
            condition = f"({expr}) == ({case.condition.accept(self)})"
            value = case.value.accept(self)
            result = f"np.where({condition}, {value}, {result})"
        
        return result
    
    def visit_case_expression(self, node: CaseExpression) -> str:
        result = None
        if node.else_value:
            result = node.else_value.accept(self)
        else:
            result = "None"
        
        for when_clause in reversed(node.when_clauses):
            condition = when_clause.condition.accept(self)
            value = when_clause.value.accept(self)
            result = f"np.where({condition}, {value}, {result})"
        
        return result

