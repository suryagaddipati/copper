"""
Tokenizer for Copper Language

Performs lexical analysis, converting source code into tokens.
Handles DAX expressions as opaque tokens between 'expression:' and ';;'
"""

import re
from dataclasses import dataclass
from typing import List, Optional, Iterator, TextIO
from enum import Enum, auto


class TokenType(Enum):
    """Token types for Copper language"""
    # Literals
    IDENTIFIER = auto()
    STRING_LITERAL = auto()
    NUMBER_LITERAL = auto()
    BOOLEAN_LITERAL = auto()
    
    # Keywords
    MODEL = auto()
    VIEW = auto()
    DIMENSION = auto()
    MEASURE = auto()
    FROM = auto()
    JOIN = auto()
    EXTENDS = auto()
    EXTENSION = auto()
    TYPE = auto()
    EXPRESSION = auto()
    PRIMARY_KEY = auto()
    VALUE_FORMAT = auto()
    LABEL = auto()
    DESCRIPTION = auto()
    HIDDEN = auto()
    TIERS = auto()
    SQL_LATITUDE = auto()
    SQL_LONGITUDE = auto()
    UNITS = auto()
    RELATIONSHIP = auto()
    
    # Dimension types
    DIM_STRING = auto()
    DIM_NUMBER = auto()
    DIM_DATE = auto()
    DIM_DATE_TIME = auto()
    DIM_YESNO = auto()
    DIM_TIER = auto()
    DIM_BIN = auto()
    DIM_LOCATION = auto()
    DIM_ZIPCODE = auto()
    DIM_DISTANCE = auto()
    DIM_DURATION = auto()
    DIM_TIME = auto()
    DIM_UNQUOTED = auto()
    
    # Measure types
    MEAS_COUNT = auto()
    MEAS_SUM = auto()
    MEAS_AVERAGE = auto()
    MEAS_MIN = auto()
    MEAS_MAX = auto()
    MEAS_COUNT_DISTINCT = auto()
    MEAS_MEDIAN = auto()
    MEAS_PERCENTILE = auto()
    MEAS_NUMBER = auto()
    
    # Join types
    JOIN_LEFT_OUTER = auto()
    JOIN_INNER = auto()
    JOIN_FULL_OUTER = auto()
    JOIN_CROSS = auto()
    
    # Relationship types
    REL_ONE_TO_ONE = auto()
    REL_MANY_TO_ONE = auto()
    REL_ONE_TO_MANY = auto()
    REL_MANY_TO_MANY = auto()
    
    # Format names
    FMT_USD = auto()
    FMT_EUR = auto()
    FMT_GBP = auto()
    FMT_PERCENT_1 = auto()
    FMT_PERCENT_2 = auto()
    FMT_DECIMAL_0 = auto()
    FMT_DECIMAL_1 = auto()
    FMT_DECIMAL_2 = auto()
    FMT_ID = auto()
    
    # Units
    UNIT_MILES = auto()
    UNIT_KILOMETERS = auto()
    UNIT_METERS = auto()
    UNIT_FEET = auto()
    
    # Extension types
    REQUIRED = auto()
    OPTIONAL = auto()
    
    # Delimiters
    COLON = auto()
    SEMICOLON = auto()
    SEMICOLON_SEMICOLON = auto()  # ;;
    LEFT_BRACE = auto()
    RIGHT_BRACE = auto()
    LEFT_BRACKET = auto()
    RIGHT_BRACKET = auto()
    COMMA = auto()
    
    # Special
    DAX_EXPRESSION = auto()
    COMMENT = auto()
    NEWLINE = auto()
    EOF = auto()


@dataclass
class Token:
    """Represents a single token"""
    type: TokenType
    value: str
    line: int
    column: int


class CopperTokenizer:
    """Tokenizer for Copper language"""
    
    # Keywords mapping
    KEYWORDS = {
        'model': TokenType.MODEL,
        'view': TokenType.VIEW,
        'dimension': TokenType.DIMENSION,
        'measure': TokenType.MEASURE,
        'from': TokenType.FROM,
        'join': TokenType.JOIN,
        'extends': TokenType.EXTENDS,
        'extension': TokenType.EXTENSION,
        'type': TokenType.TYPE,
        'expression': TokenType.EXPRESSION,
        'primary_key': TokenType.PRIMARY_KEY,
        'value_format': TokenType.VALUE_FORMAT,
        'label': TokenType.LABEL,
        'description': TokenType.DESCRIPTION,
        'hidden': TokenType.HIDDEN,
        'tiers': TokenType.TIERS,
        'sql_latitude': TokenType.SQL_LATITUDE,
        'sql_longitude': TokenType.SQL_LONGITUDE,
        'units': TokenType.UNITS,
        'relationship': TokenType.RELATIONSHIP,
        
        # Dimension types
        'string': TokenType.DIM_STRING,
        'number': TokenType.DIM_NUMBER,
        'date': TokenType.DIM_DATE,
        'date_time': TokenType.DIM_DATE_TIME,
        'yesno': TokenType.DIM_YESNO,
        'tier': TokenType.DIM_TIER,
        'bin': TokenType.DIM_BIN,
        'location': TokenType.DIM_LOCATION,
        'zipcode': TokenType.DIM_ZIPCODE,
        'distance': TokenType.DIM_DISTANCE,
        'duration': TokenType.DIM_DURATION,
        'time': TokenType.DIM_TIME,
        'unquoted': TokenType.DIM_UNQUOTED,
        
        # Measure types
        'count': TokenType.MEAS_COUNT,
        'sum': TokenType.MEAS_SUM,
        'average': TokenType.MEAS_AVERAGE,
        'min': TokenType.MEAS_MIN,
        'max': TokenType.MEAS_MAX,
        'count_distinct': TokenType.MEAS_COUNT_DISTINCT,
        'median': TokenType.MEAS_MEDIAN,
        'percentile': TokenType.MEAS_PERCENTILE,
        
        # Join types
        'left_outer': TokenType.JOIN_LEFT_OUTER,
        'inner': TokenType.JOIN_INNER,
        'full_outer': TokenType.JOIN_FULL_OUTER,
        'cross': TokenType.JOIN_CROSS,
        
        # Relationship types
        'one_to_one': TokenType.REL_ONE_TO_ONE,
        'many_to_one': TokenType.REL_MANY_TO_ONE,
        'one_to_many': TokenType.REL_ONE_TO_MANY,
        'many_to_many': TokenType.REL_MANY_TO_MANY,
        
        # Format names
        'usd': TokenType.FMT_USD,
        'eur': TokenType.FMT_EUR,
        'gbp': TokenType.FMT_GBP,
        'percent_1': TokenType.FMT_PERCENT_1,
        'percent_2': TokenType.FMT_PERCENT_2,
        'decimal_0': TokenType.FMT_DECIMAL_0,
        'decimal_1': TokenType.FMT_DECIMAL_1,
        'decimal_2': TokenType.FMT_DECIMAL_2,
        'id': TokenType.FMT_ID,
        
        # Units
        'miles': TokenType.UNIT_MILES,
        'kilometers': TokenType.UNIT_KILOMETERS,
        'meters': TokenType.UNIT_METERS,
        'feet': TokenType.UNIT_FEET,
        
        # Extension types
        'required': TokenType.REQUIRED,
        'optional': TokenType.OPTIONAL,
        
        # Boolean literals
        'true': TokenType.BOOLEAN_LITERAL,
        'false': TokenType.BOOLEAN_LITERAL,
        'yes': TokenType.BOOLEAN_LITERAL,
        'no': TokenType.BOOLEAN_LITERAL,
    }
    
    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.line = 1
        self.column = 1
        self.tokens: List[Token] = []
    
    def error(self, message: str) -> Exception:
        """Create a tokenizer error with position information"""
        return SyntaxError(f"Line {self.line}, Column {self.column}: {message}")
    
    def peek(self, offset: int = 0) -> str:
        """Peek at character at current position + offset"""
        pos = self.pos + offset
        if pos >= len(self.text):
            return '\0'
        return self.text[pos]
    
    def advance(self) -> str:
        """Advance position and return current character"""
        if self.pos >= len(self.text):
            return '\0'
        
        char = self.text[self.pos]
        self.pos += 1
        
        if char == '\n':
            self.line += 1
            self.column = 1
        else:
            self.column += 1
        
        return char
    
    def skip_whitespace(self):
        """Skip whitespace except newlines"""
        while self.peek() in ' \t\r':
            self.advance()
    
    def read_string_literal(self) -> str:
        """Read a string literal enclosed in quotes"""
        quote_char = self.advance()  # Skip opening quote
        value = ""
        
        while self.peek() != '\0' and self.peek() != quote_char:
            char = self.advance()
            if char == '\\':
                # Handle escape sequences
                next_char = self.advance()
                if next_char == 'n':
                    value += '\n'
                elif next_char == 't':
                    value += '\t'
                elif next_char == 'r':
                    value += '\r'
                elif next_char == '\\':
                    value += '\\'
                elif next_char == '"':
                    value += '"'
                elif next_char == "'":
                    value += "'"
                else:
                    value += next_char
            else:
                value += char
        
        if self.peek() != quote_char:
            raise self.error(f"Unterminated string literal")
        
        self.advance()  # Skip closing quote
        return value
    
    def read_number_literal(self) -> str:
        """Read a numeric literal"""
        value = ""
        
        # Handle negative numbers
        if self.peek() == '-':
            value += self.advance()
        
        # Read integer part
        while self.peek().isdigit():
            value += self.advance()
        
        # Read decimal part if present
        if self.peek() == '.' and self.peek(1).isdigit():
            value += self.advance()  # Add '.'
            while self.peek().isdigit():
                value += self.advance()
        
        return value
    
    def read_identifier(self) -> str:
        """Read an identifier or keyword"""
        value = ""
        
        while self.peek().isalnum() or self.peek() == '_':
            value += self.advance()
        
        return value
    
    def read_comment(self) -> str:
        """Read a comment line"""
        self.advance()  # Skip '#'
        value = ""
        
        while self.peek() != '\0' and self.peek() != '\n':
            value += self.advance()
        
        return value.strip()
    
    def read_dax_expression(self) -> str:
        """Read DAX expression between 'expression:' and ';;'"""
        # We've already consumed 'expression:'
        # Skip whitespace and read until ';;'
        self.skip_whitespace()
        
        value = ""
        while self.pos < len(self.text) - 1:
            if self.peek() == ';' and self.peek(1) == ';':
                break
            value += self.advance()
        
        if self.pos >= len(self.text) - 1:
            raise self.error("Unterminated DAX expression (missing ';;')")
        
        # Skip the ';;'
        self.advance()  # Skip first ';'
        self.advance()  # Skip second ';'
        
        return value.strip()
    
    def tokenize(self) -> List[Token]:
        """Tokenize the input text"""
        self.tokens = []
        
        while self.pos < len(self.text):
            start_line = self.line
            start_column = self.column
            
            char = self.peek()
            
            # Skip whitespace (except newlines)
            if char in ' \t\r':
                self.skip_whitespace()
                continue
            
            # Newlines
            elif char == '\n':
                self.advance()
                self.tokens.append(Token(TokenType.NEWLINE, '\\n', start_line, start_column))
            
            # Comments
            elif char == '#':
                comment_text = self.read_comment()
                self.tokens.append(Token(TokenType.COMMENT, comment_text, start_line, start_column))
            
            # String literals
            elif char in '"\'':
                string_value = self.read_string_literal()
                self.tokens.append(Token(TokenType.STRING_LITERAL, string_value, start_line, start_column))
            
            # Numbers
            elif char.isdigit() or (char == '-' and self.peek(1).isdigit()):
                number_value = self.read_number_literal()
                self.tokens.append(Token(TokenType.NUMBER_LITERAL, number_value, start_line, start_column))
            
            # Identifiers and keywords
            elif char.isalpha() or char == '_':
                identifier = self.read_identifier()
                
                # Check if we just read a keyword that expects DAX expressions
                dax_keywords = {'expression', 'sql_latitude', 'sql_longitude'}
                if identifier in dax_keywords and self.peek() == ':':
                    # Add the keyword token
                    token_type = self.KEYWORDS.get(identifier, TokenType.IDENTIFIER)
                    self.tokens.append(Token(token_type, identifier, start_line, start_column))
                    # Add the ':' token
                    self.advance()
                    self.tokens.append(Token(TokenType.COLON, ':', self.line, self.column - 1))
                    # Read the DAX expression
                    dax_line = self.line
                    dax_column = self.column
                    dax_value = self.read_dax_expression()
                    self.tokens.append(Token(TokenType.DAX_EXPRESSION, dax_value, dax_line, dax_column))
                    # Add the ';;' token
                    self.tokens.append(Token(TokenType.SEMICOLON_SEMICOLON, ';;', self.line, self.column - 2))
                    continue
                
                # Context-sensitive keyword handling
                # Check previous tokens to determine if we're expecting a name
                expecting_name = False
                if len(self.tokens) >= 2:
                    # Look for pattern: KEYWORD COLON (expecting name next)
                    prev_token = self.tokens[-1]
                    prev_prev_token = self.tokens[-2]
                    if (prev_token.type == TokenType.COLON and 
                        prev_prev_token.type in {TokenType.DIMENSION, TokenType.MEASURE, TokenType.JOIN, 
                                               TokenType.MODEL, TokenType.VIEW, TokenType.FROM}):
                        expecting_name = True
                
                # Structural keywords should always be treated as keywords
                structural_keywords = {'model', 'view', 'dimension', 'measure', 'join', 'from', 'extends', 'extension', 
                                     'type', 'expression', 'primary_key', 'value_format', 'label', 'description', 
                                     'hidden', 'tiers', 'sql_latitude', 'sql_longitude', 'units', 'relationship'}
                
                if expecting_name:
                    # After certain patterns, treat any word as an identifier (even keywords)
                    self.tokens.append(Token(TokenType.IDENTIFIER, identifier, start_line, start_column))
                elif identifier in structural_keywords:
                    # Always treat structural keywords as keywords
                    token_type = self.KEYWORDS.get(identifier, TokenType.IDENTIFIER)
                    self.tokens.append(Token(token_type, identifier, start_line, start_column))
                else:
                    # Regular keyword/identifier handling
                    token_type = self.KEYWORDS.get(identifier, TokenType.IDENTIFIER)
                    self.tokens.append(Token(token_type, identifier, start_line, start_column))
            
            # Delimiters
            elif char == ':':
                self.advance()
                self.tokens.append(Token(TokenType.COLON, ':', start_line, start_column))
            
            elif char == ';':
                if self.peek(1) == ';':
                    self.advance()
                    self.advance()
                    self.tokens.append(Token(TokenType.SEMICOLON_SEMICOLON, ';;', start_line, start_column))
                else:
                    self.advance()
                    self.tokens.append(Token(TokenType.SEMICOLON, ';', start_line, start_column))
            
            elif char == '{':
                self.advance()
                self.tokens.append(Token(TokenType.LEFT_BRACE, '{', start_line, start_column))
            
            elif char == '}':
                self.advance()
                self.tokens.append(Token(TokenType.RIGHT_BRACE, '}', start_line, start_column))
            
            elif char == '[':
                self.advance()
                self.tokens.append(Token(TokenType.LEFT_BRACKET, '[', start_line, start_column))
            
            elif char == ']':
                self.advance()
                self.tokens.append(Token(TokenType.RIGHT_BRACKET, ']', start_line, start_column))
            
            elif char == ',':
                self.advance()
                self.tokens.append(Token(TokenType.COMMA, ',', start_line, start_column))
            
            else:
                raise self.error(f"Unexpected character: '{char}'")
        
        # Add EOF token
        self.tokens.append(Token(TokenType.EOF, '', self.line, self.column))
        return self.tokens
    
    def get_tokens(self) -> List[Token]:
        """Get the tokenized result"""
        if not self.tokens:
            self.tokenize()
        return self.tokens