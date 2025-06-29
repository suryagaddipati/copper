from abc import ABC, abstractmethod
from typing import List, Optional, Any, Union
from dataclasses import dataclass


class ASTNode(ABC):
    """Base class for all AST nodes."""
    
    @abstractmethod
    def accept(self, visitor):
        """Accept a visitor for the visitor pattern."""
        pass


@dataclass
class Literal(ASTNode):
    """Represents literal values (numbers, strings, booleans, null)."""
    value: Any
    type: str  # 'number', 'string', 'boolean', 'null'
    
    def accept(self, visitor):
        return visitor.visit_literal(self)


@dataclass
class Identifier(ASTNode):
    """Represents an identifier (variable name, column name)."""
    name: str
    
    def accept(self, visitor):
        return visitor.visit_identifier(self)


@dataclass
class ColumnReference(ASTNode):
    """Represents a column reference (Table.column or just column)."""
    table: Optional[str]
    column: str
    
    def accept(self, visitor):
        return visitor.visit_column_reference(self)


@dataclass
class BinaryOperation(ASTNode):
    """Represents binary operations (+, -, *, /, =, <, >, etc.)."""
    left: ASTNode
    operator: str
    right: ASTNode
    
    def accept(self, visitor):
        return visitor.visit_binary_operation(self)


@dataclass
class UnaryOperation(ASTNode):
    """Represents unary operations (NOT, -)."""
    operator: str
    operand: ASTNode
    
    def accept(self, visitor):
        return visitor.visit_unary_operation(self)


@dataclass
class FunctionCall(ASTNode):
    """Represents function calls."""
    function_name: str
    arguments: List[ASTNode]
    
    def accept(self, visitor):
        return visitor.visit_function_call(self)


@dataclass
class IfExpression(ASTNode):
    """Represents IF(condition, true_value, false_value)."""
    condition: ASTNode
    true_value: ASTNode
    false_value: ASTNode
    
    def accept(self, visitor):
        return visitor.visit_if_expression(self)


@dataclass
class SwitchCase:
    """Represents a single case in a SWITCH expression."""
    condition: ASTNode
    value: ASTNode


@dataclass
class SwitchExpression(ASTNode):
    """Represents SWITCH(expr, case1, value1, case2, value2, default)."""
    expression: ASTNode
    cases: List[SwitchCase]
    default_value: Optional[ASTNode] = None
    
    def accept(self, visitor):
        return visitor.visit_switch_expression(self)


@dataclass
class WhenClause:
    """Represents a WHEN clause in a CASE expression."""
    condition: ASTNode
    value: ASTNode


@dataclass
class CaseExpression(ASTNode):
    """Represents CASE WHEN ... THEN ... ELSE ... END."""
    when_clauses: List[WhenClause]
    else_value: Optional[ASTNode] = None
    
    def accept(self, visitor):
        return visitor.visit_case_expression(self)


class ASTVisitor(ABC):
    """Abstract visitor for AST nodes."""
    
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