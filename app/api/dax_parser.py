"""
DAX Expression Parser Module

Dedicated parser for DAX (Data Analysis Expressions) used in Copper language.
This module handles parsing and validation of DAX expressions independently
from the main Copper grammar.
"""

import re
from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass
from enum import Enum


class DAXTokenType(Enum):
    """Types of tokens in DAX expressions"""
    IDENTIFIER = "identifier"
    NUMBER = "number"
    STRING = "string"
    FUNCTION = "function"
    OPERATOR = "operator"
    BRACKET_OPEN = "bracket_open"
    BRACKET_CLOSE = "bracket_close"
    PAREN_OPEN = "paren_open"
    PAREN_CLOSE = "paren_close"
    COMMA = "comma"
    DOT = "dot"
    WHITESPACE = "whitespace"
    UNKNOWN = "unknown"


@dataclass
class DAXToken:
    """A single DAX token"""
    type: DAXTokenType
    value: str
    position: int


@dataclass
class DAXParseResult:
    """Result of DAX expression parsing"""
    success: bool
    tokens: List[DAXToken]
    errors: List[str]
    original_expression: str
    normalized_expression: str


class DAXLexer:
    """Lexer for DAX expressions"""
    
    # DAX operators
    OPERATORS = {
        '+', '-', '*', '/', '=', '<', '>', '<=', '>=', '<>', '!=',
        '&&', '||', '&'
    }
    
    # Common DAX functions (can be extended)
    FUNCTIONS = {
        'SUM', 'COUNT', 'AVERAGE', 'MIN', 'MAX', 'CALCULATE', 'FILTER',
        'RELATED', 'RELATEDTABLE', 'VALUES', 'DISTINCT', 'COUNTROWS',
        'IF', 'SWITCH', 'AND', 'OR', 'NOT', 'TRUE', 'FALSE', 'BLANK',
        'CONCATENATE', 'LEFT', 'RIGHT', 'MID', 'LEN', 'UPPER', 'LOWER',
        'DATE', 'YEAR', 'MONTH', 'DAY', 'TODAY', 'NOW', 'DATEDIFF',
        'DATEADD', 'SAMEPERIODLASTYEAR', 'TOTALYTD', 'DIVIDE'
    }
    
    def __init__(self):
        self.tokens: List[DAXToken] = []
        self.position = 0
        self.expression = ""
        self.errors: List[str] = []
    
    def tokenize(self, expression: str) -> List[DAXToken]:
        """Tokenize a DAX expression"""
        self.tokens = []
        self.position = 0
        self.expression = expression.strip()
        self.errors = []
        
        while self.position < len(self.expression):
            if self._consume_whitespace():
                continue
            elif self._consume_number():
                continue
            elif self._consume_string():
                continue
            elif self._consume_operator():
                continue
            elif self._consume_bracket_or_paren():
                continue
            elif self._consume_comma_or_dot():
                continue
            elif self._consume_identifier_or_function():
                continue
            else:
                # Unknown character
                char = self.expression[self.position]
                self._add_token(DAXTokenType.UNKNOWN, char)
                self.errors.append(f"Unknown character '{char}' at position {self.position}")
                self.position += 1
        
        return self.tokens
    
    def _current_char(self) -> Optional[str]:
        """Get current character"""
        if self.position >= len(self.expression):
            return None
        return self.expression[self.position]
    
    def _peek_char(self, offset: int = 1) -> Optional[str]:
        """Peek at character ahead"""
        pos = self.position + offset
        if pos >= len(self.expression):
            return None
        return self.expression[pos]
    
    def _add_token(self, token_type: DAXTokenType, value: str):
        """Add a token to the list"""
        token = DAXToken(token_type, value, self.position - len(value))
        self.tokens.append(token)
    
    def _consume_whitespace(self) -> bool:
        """Consume whitespace characters"""
        start_pos = self.position
        while self._current_char() and self._current_char().isspace():
            self.position += 1
        
        if self.position > start_pos:
            value = self.expression[start_pos:self.position]
            self._add_token(DAXTokenType.WHITESPACE, value)
            return True
        return False
    
    def _consume_number(self) -> bool:
        """Consume numeric literals"""
        start_pos = self.position
        char = self._current_char()
        
        if not char or not (char.isdigit() or char == '.'):
            return False
        
        has_dot = False
        while self._current_char() and (self._current_char().isdigit() or 
                                       (self._current_char() == '.' and not has_dot)):
            if self._current_char() == '.':
                has_dot = True
            self.position += 1
        
        if self.position > start_pos:
            value = self.expression[start_pos:self.position]
            self._add_token(DAXTokenType.NUMBER, value)
            return True
        return False
    
    def _consume_string(self) -> bool:
        """Consume string literals"""
        char = self._current_char()
        if not char or char not in ['"', "'"]:
            return False
        
        quote_char = char
        start_pos = self.position
        self.position += 1  # Skip opening quote
        
        while self._current_char() and self._current_char() != quote_char:
            if self._current_char() == '\\':
                self.position += 1  # Skip escape character
                if self._current_char():
                    self.position += 1  # Skip escaped character
            else:
                self.position += 1
        
        if self._current_char() == quote_char:
            self.position += 1  # Skip closing quote
            value = self.expression[start_pos:self.position]
            self._add_token(DAXTokenType.STRING, value)
            return True
        else:
            self.errors.append(f"Unterminated string starting at position {start_pos}")
            return False
    
    def _consume_operator(self) -> bool:
        """Consume operators"""
        # Check for two-character operators first
        if self.position + 1 < len(self.expression):
            two_char = self.expression[self.position:self.position + 2]
            if two_char in self.OPERATORS:
                self._add_token(DAXTokenType.OPERATOR, two_char)
                self.position += 2
                return True
        
        # Check for single-character operators
        char = self._current_char()
        if char and char in self.OPERATORS:
            self._add_token(DAXTokenType.OPERATOR, char)
            self.position += 1
            return True
        
        return False
    
    def _consume_bracket_or_paren(self) -> bool:
        """Consume brackets and parentheses"""
        char = self._current_char()
        if char == '[':
            self._add_token(DAXTokenType.BRACKET_OPEN, char)
            self.position += 1
            return True
        elif char == ']':
            self._add_token(DAXTokenType.BRACKET_CLOSE, char)
            self.position += 1
            return True
        elif char == '(':
            self._add_token(DAXTokenType.PAREN_OPEN, char)
            self.position += 1
            return True
        elif char == ')':
            self._add_token(DAXTokenType.PAREN_CLOSE, char)
            self.position += 1
            return True
        return False
    
    def _consume_comma_or_dot(self) -> bool:
        """Consume commas and dots"""
        char = self._current_char()
        if char == ',':
            self._add_token(DAXTokenType.COMMA, char)
            self.position += 1
            return True
        elif char == '.':
            self._add_token(DAXTokenType.DOT, char)
            self.position += 1
            return True
        return False
    
    def _consume_identifier_or_function(self) -> bool:
        """Consume identifiers and function names"""
        start_pos = self.position
        char = self._current_char()
        
        if not char or not (char.isalpha() or char == '_'):
            return False
        
        while self._current_char() and (self._current_char().isalnum() or 
                                       self._current_char() in ['_', ' ']):
            # Handle spaces in table/column names
            if self._current_char() == ' ':
                # Look ahead to see if this is part of an identifier
                next_char = self._peek_char()
                if not next_char or not (next_char.isalnum() or next_char == '_'):
                    break
            self.position += 1
        
        if self.position > start_pos:
            value = self.expression[start_pos:self.position].strip()
            
            # Check if it's a known function
            if value.upper() in self.FUNCTIONS:
                self._add_token(DAXTokenType.FUNCTION, value)
            else:
                self._add_token(DAXTokenType.IDENTIFIER, value)
            return True
        return False


class DAXParser:
    """Main DAX expression parser"""
    
    def __init__(self):
        self.lexer = DAXLexer()
    
    def parse(self, expression: str) -> DAXParseResult:
        """Parse a DAX expression and return result"""
        # Remove the trailing ;; if present
        cleaned_expression = expression.rstrip(';').strip()
        
        # Tokenize the expression
        tokens = self.lexer.tokenize(cleaned_expression)
        
        # Basic validation
        errors = list(self.lexer.errors)
        success = len(errors) == 0
        
        # Additional validation can be added here
        # - Balanced parentheses/brackets
        # - Function syntax validation
        # - etc.
        
        errors.extend(self._validate_structure(tokens))
        success = len(errors) == 0
        
        # Create normalized expression (removing unnecessary whitespace)
        normalized = self._normalize_expression(tokens)
        
        return DAXParseResult(
            success=success,
            tokens=[t for t in tokens if t.type != DAXTokenType.WHITESPACE],
            errors=errors,
            original_expression=expression,
            normalized_expression=normalized
        )
    
    def _validate_structure(self, tokens: List[DAXToken]) -> List[str]:
        """Validate the structural correctness of tokens"""
        errors = []
        
        # Check balanced parentheses
        paren_count = 0
        bracket_count = 0
        
        for token in tokens:
            if token.type == DAXTokenType.PAREN_OPEN:
                paren_count += 1
            elif token.type == DAXTokenType.PAREN_CLOSE:
                paren_count -= 1
                if paren_count < 0:
                    errors.append(f"Unmatched closing parenthesis at position {token.position}")
            elif token.type == DAXTokenType.BRACKET_OPEN:
                bracket_count += 1
            elif token.type == DAXTokenType.BRACKET_CLOSE:
                bracket_count -= 1
                if bracket_count < 0:
                    errors.append(f"Unmatched closing bracket at position {token.position}")
        
        if paren_count > 0:
            errors.append("Unmatched opening parenthesis")
        if bracket_count > 0:
            errors.append("Unmatched opening bracket")
        
        return errors
    
    def _normalize_expression(self, tokens: List[DAXToken]) -> str:
        """Create a normalized version of the expression"""
        result = []
        
        for i, token in enumerate(tokens):
            if token.type == DAXTokenType.WHITESPACE:
                # Only add single space between non-whitespace tokens
                if (i > 0 and i < len(tokens) - 1 and 
                    tokens[i-1].type != DAXTokenType.WHITESPACE and
                    tokens[i+1].type != DAXTokenType.WHITESPACE):
                    result.append(' ')
            else:
                result.append(token.value)
        
        return ''.join(result)


# Convenience function for simple DAX parsing
def parse_dax_expression(expression: str) -> DAXParseResult:
    """
    Parse a DAX expression and return the result.
    
    Args:
        expression: The DAX expression to parse (with or without trailing ;;)
    
    Returns:
        DAXParseResult containing success status, tokens, and any errors
    """
    parser = DAXParser()
    return parser.parse(expression)


# Validation function for integration with main parser
def validate_dax_expression(expression: str) -> Dict[str, Any]:
    """
    Validate a DAX expression and return result in format compatible with main parser.
    
    Args:
        expression: The DAX expression to validate
    
    Returns:
        Dictionary with 'valid' boolean and 'errors' list
    """
    result = parse_dax_expression(expression)
    return {
        'valid': result.success,
        'errors': result.errors,
        'tokens': len(result.tokens),
        'normalized': result.normalized_expression
    }