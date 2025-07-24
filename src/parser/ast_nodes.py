from abc import ABC, abstractmethod
from typing import List, Optional, Any, Union
from dataclasses import dataclass


class ASTNode(ABC):
    
    @abstractmethod
    def accept(self, visitor):
        pass


@dataclass
class Literal(ASTNode):
    value: Any
    type: str
    
    def accept(self, visitor):
        return visitor.visit_literal(self)


@dataclass
class Identifier(ASTNode):
    name: str
    
    def accept(self, visitor):
        return visitor.visit_identifier(self)


@dataclass
class ColumnReference(ASTNode):
    table: Optional[str]
    column: str
    
    def accept(self, visitor):
        return visitor.visit_column_reference(self)


@dataclass
class BinaryOperation(ASTNode):
    left: ASTNode
    operator: str
    right: ASTNode
    
    def accept(self, visitor):
        return visitor.visit_binary_operation(self)


@dataclass
class UnaryOperation(ASTNode):
    operator: str
    operand: ASTNode
    
    def accept(self, visitor):
        return visitor.visit_unary_operation(self)


@dataclass
class FunctionCall(ASTNode):
    function_name: str
    arguments: List[ASTNode]
    
    def accept(self, visitor):
        return visitor.visit_function_call(self)


@dataclass
class IfExpression(ASTNode):
    condition: ASTNode
    true_value: ASTNode
    false_value: ASTNode
    
    def accept(self, visitor):
        return visitor.visit_if_expression(self)


@dataclass
class SwitchCase:
    condition: ASTNode
    value: ASTNode


@dataclass
class SwitchExpression(ASTNode):
    expression: ASTNode
    cases: List[SwitchCase]
    default_value: Optional[ASTNode] = None
    
    def accept(self, visitor):
        return visitor.visit_switch_expression(self)


@dataclass
class WhenClause:
    condition: ASTNode
    value: ASTNode


@dataclass
class CaseExpression(ASTNode):
    when_clauses: List[WhenClause]
    else_value: Optional[ASTNode] = None
    
    def accept(self, visitor):
        return visitor.visit_case_expression(self)


class ASTVisitor(ABC):
    
    @abstractmethod
    def visit_literal(self, node: Literal):
        pass
    
    @abstractmethod
    def visit_identifier(self, node: Identifier):
        pass
    
    @abstractmethod
    def visit_column_reference(self, node: ColumnReference):
        pass
    
    @abstractmethod
    def visit_binary_operation(self, node: BinaryOperation):
        pass
    
    @abstractmethod
    def visit_unary_operation(self, node: UnaryOperation):
        pass
    
    @abstractmethod
    def visit_function_call(self, node: FunctionCall):
        pass
    
    @abstractmethod
    def visit_if_expression(self, node: IfExpression):
        pass
    
    @abstractmethod
    def visit_switch_expression(self, node: SwitchExpression):
        pass
    
    @abstractmethod
    def visit_case_expression(self, node: CaseExpression):
        pass