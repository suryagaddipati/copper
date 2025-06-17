"""
Recursive Descent Parser for Copper Language

Implements the syntax analysis phase, building an AST from tokens
according to the Copper EBNF grammar specification.
"""

from typing import List, Optional, Union, Any
try:
    from .tokenizer import Token, TokenType, CopperTokenizer
    from .ast_nodes import *
except ImportError:
    from tokenizer import Token, TokenType, CopperTokenizer
    from ast_nodes import *


class ParseError(Exception):
    """Exception raised during parsing"""
    def __init__(self, message: str, token: Optional[Token] = None):
        self.message = message
        self.token = token
        if token:
            super().__init__(f"Line {token.line}, Column {token.column}: {message}")
        else:
            super().__init__(message)


class CopperParser:
    """Recursive descent parser for Copper language"""
    
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[0] if tokens else None
    
    def error(self, message: str) -> ParseError:
        """Create a parse error with current token information"""
        return ParseError(message, self.current_token)
    
    def advance(self):
        """Move to the next token"""
        if self.pos < len(self.tokens) - 1:
            self.pos += 1
            self.current_token = self.tokens[self.pos]
    
    def peek(self, offset: int = 1) -> Optional[Token]:
        """Peek at the token at current position + offset"""
        pos = self.pos + offset
        if pos < len(self.tokens):
            return self.tokens[pos]
        return None
    
    def expect(self, token_type: TokenType) -> Token:
        """Expect a specific token type and advance"""
        if not self.current_token or self.current_token.type != token_type:
            raise self.error(f"Expected {token_type}, got {self.current_token.type if self.current_token else 'EOF'}")
        
        token = self.current_token
        self.advance()
        return token
    
    def match(self, *token_types: TokenType) -> bool:
        """Check if current token matches any of the given types"""
        if not self.current_token:
            return False
        return self.current_token.type in token_types
    
    def skip_newlines(self):
        """Skip newline tokens"""
        while self.match(TokenType.NEWLINE):
            self.advance()
    
    def skip_comments_and_newlines(self):
        """Skip comments and newlines"""
        while self.match(TokenType.COMMENT, TokenType.NEWLINE):
            self.advance()
    
    def parse(self) -> Program:
        """Parse the entire program"""
        statements = []
        
        self.skip_comments_and_newlines()
        
        while not self.match(TokenType.EOF):
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
            self.skip_comments_and_newlines()
        
        return Program(statements=statements)
    
    def parse_statement(self) -> Optional[Statement]:
        """Parse a top-level statement"""
        if self.match(TokenType.COMMENT):
            return self.parse_comment()
        elif self.match(TokenType.MODEL):
            return self.parse_model()
        elif self.match(TokenType.VIEW):
            return self.parse_view()
        elif self.match(TokenType.NEWLINE):
            self.advance()
            return None
        else:
            raise self.error(f"Unexpected token in statement: {self.current_token.type}")
    
    def parse_comment(self) -> Comment:
        """Parse a comment"""
        token = self.expect(TokenType.COMMENT)
        return Comment(text=token.value, line=token.line, column=token.column)
    
    def parse_model(self) -> Model:
        """Parse a model statement"""
        model_token = self.expect(TokenType.MODEL)
        self.expect(TokenType.COLON)
        name_token = self.expect(TokenType.IDENTIFIER)
        self.expect(TokenType.LEFT_BRACE)
        
        dimensions = []
        measures = []
        
        self.skip_comments_and_newlines()
        
        while not self.match(TokenType.RIGHT_BRACE):
            if self.match(TokenType.DIMENSION):
                dimensions.append(self.parse_dimension())
            elif self.match(TokenType.MEASURE):
                measures.append(self.parse_measure())
            elif self.match(TokenType.COMMENT):
                self.advance()  # Skip comments in model body
            else:
                raise self.error(f"Expected dimension or measure in model body, got {self.current_token.type}")
            
            self.skip_comments_and_newlines()
        
        self.expect(TokenType.RIGHT_BRACE)
        
        return Model(
            name=name_token.value,
            dimensions=dimensions,
            measures=measures,
            line=model_token.line,
            column=model_token.column
        )
    
    def parse_dimension(self) -> Dimension:
        """Parse a dimension statement"""
        dim_token = self.expect(TokenType.DIMENSION)
        self.expect(TokenType.COLON)
        name_token = self.expect(TokenType.IDENTIFIER)
        self.expect(TokenType.LEFT_BRACE)
        
        dimension = Dimension(
            name=name_token.value,
            line=dim_token.line,
            column=dim_token.column
        )
        
        self.skip_comments_and_newlines()
        
        while not self.match(TokenType.RIGHT_BRACE):
            if self.match(TokenType.TYPE):
                self.advance()
                self.expect(TokenType.COLON)
                dimension.type = self.parse_dimension_type()
            
            elif self.match(TokenType.EXPRESSION):
                self.advance()
                self.expect(TokenType.COLON)
                dimension.expression = self.parse_dax_expression()
                self.expect(TokenType.SEMICOLON_SEMICOLON)
            
            elif self.match(TokenType.PRIMARY_KEY):
                self.advance()
                self.expect(TokenType.COLON)
                dimension.primary_key = self.parse_boolean()
            
            elif self.match(TokenType.VALUE_FORMAT):
                self.advance()
                self.expect(TokenType.COLON)
                dimension.value_format = self.parse_value_format()
            
            elif self.match(TokenType.LABEL):
                self.advance()
                self.expect(TokenType.COLON)
                dimension.label = self.parse_string_literal()
            
            elif self.match(TokenType.DESCRIPTION):
                self.advance()
                self.expect(TokenType.COLON)
                dimension.description = self.parse_string_literal()
            
            elif self.match(TokenType.HIDDEN):
                self.advance()
                self.expect(TokenType.COLON)
                dimension.hidden = self.parse_boolean()
            
            elif self.match(TokenType.TIERS):
                self.advance()
                self.expect(TokenType.COLON)
                dimension.tiers = self.parse_tiers()
            
            elif self.match(TokenType.SQL_LATITUDE):
                self.advance()
                self.expect(TokenType.COLON)
                dimension.sql_latitude = self.parse_dax_expression()
                self.expect(TokenType.SEMICOLON_SEMICOLON)
            
            elif self.match(TokenType.SQL_LONGITUDE):
                self.advance()
                self.expect(TokenType.COLON)
                dimension.sql_longitude = self.parse_dax_expression()
                self.expect(TokenType.SEMICOLON_SEMICOLON)
            
            elif self.match(TokenType.UNITS):
                self.advance()
                self.expect(TokenType.COLON)
                dimension.units = self.parse_units()
            
            elif self.match(TokenType.COMMENT):
                self.advance()  # Skip comments
            
            else:
                raise self.error(f"Unexpected token in dimension: {self.current_token.type}")
            
            self.skip_comments_and_newlines()
        
        self.expect(TokenType.RIGHT_BRACE)
        return dimension
    
    def parse_measure(self) -> Measure:
        """Parse a measure statement"""
        meas_token = self.expect(TokenType.MEASURE)
        self.expect(TokenType.COLON)
        name_token = self.expect(TokenType.IDENTIFIER)
        self.expect(TokenType.LEFT_BRACE)
        
        measure = Measure(
            name=name_token.value,
            line=meas_token.line,
            column=meas_token.column
        )
        
        self.skip_comments_and_newlines()
        
        while not self.match(TokenType.RIGHT_BRACE):
            if self.match(TokenType.TYPE):
                self.advance()
                self.expect(TokenType.COLON)
                measure.type = self.parse_measure_type()
            
            elif self.match(TokenType.EXPRESSION):
                self.advance()
                self.expect(TokenType.COLON)
                measure.expression = self.parse_dax_expression()
                self.expect(TokenType.SEMICOLON_SEMICOLON)
            
            elif self.match(TokenType.VALUE_FORMAT):
                self.advance()
                self.expect(TokenType.COLON)
                measure.value_format = self.parse_value_format()
            
            elif self.match(TokenType.LABEL):
                self.advance()
                self.expect(TokenType.COLON)
                measure.label = self.parse_string_literal()
            
            elif self.match(TokenType.DESCRIPTION):
                self.advance()
                self.expect(TokenType.COLON)
                measure.description = self.parse_string_literal()
            
            elif self.match(TokenType.HIDDEN):
                self.advance()
                self.expect(TokenType.COLON)
                measure.hidden = self.parse_boolean()
            
            elif self.match(TokenType.COMMENT):
                self.advance()  # Skip comments
            
            else:
                raise self.error(f"Unexpected token in measure: {self.current_token.type}")
            
            self.skip_comments_and_newlines()
        
        self.expect(TokenType.RIGHT_BRACE)
        return measure
    
    def parse_view(self) -> View:
        """Parse a view statement"""
        view_token = self.expect(TokenType.VIEW)
        self.expect(TokenType.COLON)
        name_token = self.expect(TokenType.IDENTIFIER)
        self.expect(TokenType.LEFT_BRACE)
        
        view = View(
            name=name_token.value,
            line=view_token.line,
            column=view_token.column
        )
        
        self.skip_comments_and_newlines()
        
        while not self.match(TokenType.RIGHT_BRACE):
            if self.match(TokenType.FROM):
                self.advance()
                self.expect(TokenType.COLON)
                from_token = self.expect(TokenType.IDENTIFIER)
                view.from_model = from_token.value
            
            elif self.match(TokenType.JOIN):
                view.joins.append(self.parse_join())
            
            elif self.match(TokenType.EXTENDS):
                self.advance()
                self.expect(TokenType.COLON)
                view.extends = self.parse_identifier_list()
            
            elif self.match(TokenType.EXTENSION):
                self.advance()
                self.expect(TokenType.COLON)
                if self.match(TokenType.REQUIRED):
                    view.extension = "required"
                    self.advance()
                elif self.match(TokenType.OPTIONAL):
                    view.extension = "optional"
                    self.advance()
                else:
                    raise self.error("Expected 'required' or 'optional' for extension")
            
            elif self.match(TokenType.COMMENT):
                self.advance()  # Skip comments
            
            else:
                raise self.error(f"Unexpected token in view: {self.current_token.type}")
            
            self.skip_comments_and_newlines()
        
        self.expect(TokenType.RIGHT_BRACE)
        return view
    
    def parse_join(self) -> Join:
        """Parse a join statement"""
        join_token = self.expect(TokenType.JOIN)
        self.expect(TokenType.COLON)
        name_token = self.expect(TokenType.IDENTIFIER)
        self.expect(TokenType.LEFT_BRACE)
        
        join = Join(
            name=name_token.value,
            line=join_token.line,
            column=join_token.column
        )
        
        self.skip_comments_and_newlines()
        
        while not self.match(TokenType.RIGHT_BRACE):
            if self.match(TokenType.TYPE):
                self.advance()
                self.expect(TokenType.COLON)
                join.type = self.parse_join_type()
            
            elif self.match(TokenType.RELATIONSHIP):
                self.advance()
                self.expect(TokenType.COLON)
                join.relationship = self.parse_relationship_type()
            
            elif self.match(TokenType.EXPRESSION):
                self.advance()
                self.expect(TokenType.COLON)
                join.expression = self.parse_dax_expression()
                self.expect(TokenType.SEMICOLON_SEMICOLON)
            
            elif self.match(TokenType.COMMENT):
                self.advance()  # Skip comments
            
            else:
                raise self.error(f"Unexpected token in join: {self.current_token.type}")
            
            self.skip_comments_and_newlines()
        
        self.expect(TokenType.RIGHT_BRACE)
        return join
    
    def parse_dimension_type(self) -> str:
        """Parse a dimension type"""
        if self.match(TokenType.DIM_STRING, TokenType.DIM_NUMBER, TokenType.DIM_DATE,
                     TokenType.DIM_DATE_TIME, TokenType.DIM_YESNO, TokenType.DIM_TIER,
                     TokenType.DIM_BIN, TokenType.DIM_LOCATION, TokenType.DIM_ZIPCODE,
                     TokenType.DIM_DISTANCE, TokenType.DIM_DURATION, TokenType.DIM_TIME,
                     TokenType.DIM_UNQUOTED):
            token = self.current_token
            self.advance()
            return token.value
        else:
            raise self.error(f"Expected dimension type, got {self.current_token.type}")
    
    def parse_measure_type(self) -> str:
        """Parse a measure type"""
        if self.match(TokenType.MEAS_COUNT, TokenType.MEAS_SUM, TokenType.MEAS_AVERAGE,
                     TokenType.MEAS_MIN, TokenType.MEAS_MAX, TokenType.MEAS_COUNT_DISTINCT,
                     TokenType.MEAS_MEDIAN, TokenType.MEAS_PERCENTILE, TokenType.MEAS_NUMBER,
                     TokenType.DIM_NUMBER):  # 'number' can be both dimension and measure type
            token = self.current_token
            self.advance()
            return token.value
        else:
            raise self.error(f"Expected measure type, got {self.current_token.type}")
    
    def parse_join_type(self) -> str:
        """Parse a join type"""
        if self.match(TokenType.JOIN_LEFT_OUTER, TokenType.JOIN_INNER,
                     TokenType.JOIN_FULL_OUTER, TokenType.JOIN_CROSS):
            token = self.current_token
            self.advance()
            return token.value
        else:
            raise self.error(f"Expected join type, got {self.current_token.type}")
    
    def parse_relationship_type(self) -> str:
        """Parse a relationship type"""
        if self.match(TokenType.REL_ONE_TO_ONE, TokenType.REL_MANY_TO_ONE,
                     TokenType.REL_ONE_TO_MANY, TokenType.REL_MANY_TO_MANY):
            token = self.current_token
            self.advance()
            return token.value
        else:
            raise self.error(f"Expected relationship type, got {self.current_token.type}")
    
    def parse_dax_expression(self) -> DaxExpression:
        """Parse a DAX expression"""
        if not self.match(TokenType.DAX_EXPRESSION):
            raise self.error(f"Expected DAX expression, got {self.current_token.type}")
        
        token = self.current_token
        self.advance()
        return DaxExpression(raw_text=token.value, line=token.line, column=token.column)
    
    def parse_boolean(self) -> bool:
        """Parse a boolean value"""
        if not self.match(TokenType.BOOLEAN_LITERAL):
            raise self.error(f"Expected boolean value, got {self.current_token.type}")
        
        token = self.current_token
        self.advance()
        return token.value in ['true', 'yes']
    
    def parse_string_literal(self) -> str:
        """Parse a string literal"""
        if not self.match(TokenType.STRING_LITERAL):
            raise self.error(f"Expected string literal, got {self.current_token.type}")
        
        token = self.current_token
        self.advance()
        return token.value
    
    def parse_value_format(self) -> Union[str, FormatName]:
        """Parse a value format (string literal or format name)"""
        if self.match(TokenType.STRING_LITERAL):
            return self.parse_string_literal()
        elif self.match(TokenType.FMT_USD, TokenType.FMT_EUR, TokenType.FMT_GBP,
                       TokenType.FMT_PERCENT_1, TokenType.FMT_PERCENT_2,
                       TokenType.FMT_DECIMAL_0, TokenType.FMT_DECIMAL_1,
                       TokenType.FMT_DECIMAL_2, TokenType.FMT_ID):
            token = self.current_token
            self.advance()
            return FormatName(name=token.value, line=token.line, column=token.column)
        else:
            raise self.error(f"Expected value format, got {self.current_token.type}")
    
    def parse_tiers(self) -> List[Union[str, float]]:
        """Parse tiers array"""
        self.expect(TokenType.LEFT_BRACKET)
        
        tiers = []
        
        if not self.match(TokenType.RIGHT_BRACKET):
            # Parse first element
            if self.match(TokenType.STRING_LITERAL):
                tiers.append(self.parse_string_literal())
            elif self.match(TokenType.NUMBER_LITERAL):
                token = self.current_token
                self.advance()
                tiers.append(float(token.value))
            else:
                raise self.error("Expected string or number in tiers")
            
            # Parse remaining elements
            while self.match(TokenType.COMMA):
                self.advance()
                if self.match(TokenType.STRING_LITERAL):
                    tiers.append(self.parse_string_literal())
                elif self.match(TokenType.NUMBER_LITERAL):
                    token = self.current_token
                    self.advance()
                    tiers.append(float(token.value))
                else:
                    raise self.error("Expected string or number in tiers")
        
        self.expect(TokenType.RIGHT_BRACKET)
        return tiers
    
    def parse_units(self) -> str:
        """Parse units"""
        if self.match(TokenType.UNIT_MILES, TokenType.UNIT_KILOMETERS,
                     TokenType.UNIT_METERS, TokenType.UNIT_FEET):
            token = self.current_token
            self.advance()
            return token.value
        else:
            raise self.error(f"Expected units, got {self.current_token.type}")
    
    def parse_identifier_list(self) -> List[str]:
        """Parse a list of identifiers [id1, id2, ...]"""
        self.expect(TokenType.LEFT_BRACKET)
        
        identifiers = []
        
        if not self.match(TokenType.RIGHT_BRACKET):
            # Parse first identifier
            token = self.expect(TokenType.IDENTIFIER)
            identifiers.append(token.value)
            
            # Parse remaining identifiers
            while self.match(TokenType.COMMA):
                self.advance()
                token = self.expect(TokenType.IDENTIFIER)
                identifiers.append(token.value)
        
        self.expect(TokenType.RIGHT_BRACKET)
        return identifiers