grammar Copper;

// ===========================================================================
// PARSER RULES
// ===========================================================================

program
    : (statement | NEWLINE)* EOF
    ;

statement
    : modelStatement
    | viewStatement
    | measureStatement
    | dimensionStatement
    ;

modelStatement
    : MODEL COLON identifier LBRACE (modelElement | NEWLINE)* RBRACE
    ;

viewStatement
    : VIEW COLON identifier LBRACE (viewElement | NEWLINE)* RBRACE
    ;

modelElement
    : dimensionStatement
    | measureStatement
    | joinStatement
    ;

viewElement
    : fromStatement
    | extendsStatement
    | joinStatement
    | dimensionStatement
    | measureStatement
    ;

measureStatement
    : MEASURE COLON identifier LBRACE (measureParameter | NEWLINE)* RBRACE
    ;

dimensionStatement
    : DIMENSION COLON identifier LBRACE (dimensionParameter | NEWLINE)* RBRACE
    ;

joinStatement
    : JOIN COLON identifier LBRACE (joinParameter | NEWLINE)* RBRACE
    ;

dimensionParameter
    : typeParameter
    | expressionParameter
    | labelParameter
    | descriptionParameter
    | primaryKeyParameter
    | hiddenParameter
    | valueFormatParameter
    | unitsParameter
    ;

measureParameter
    : measureTypeParameter
    | expressionParameter
    | labelParameter
    | descriptionParameter
    | hiddenParameter
    | valueFormatParameter
    | unitsParameter
    ;

joinParameter
    : joinTypeParameter
    | relationshipParameter
    | expressionParameter
    ;

typeParameter
    : TYPE COLON dimensionType
    ;

measureTypeParameter
    : TYPE COLON measureType
    ;

expressionParameter
    : EXPRESSION COLON daxExpression
    ;

labelParameter
    : LABEL COLON stringLiteral
    ;

descriptionParameter
    : DESCRIPTION COLON stringLiteral
    ;

primaryKeyParameter
    : PRIMARY_KEY COLON booleanValue
    ;

hiddenParameter
    : HIDDEN_ COLON booleanValue
    ;

valueFormatParameter
    : VALUE_FORMAT COLON (stringLiteral | formatName)
    ;

unitsParameter
    : UNITS COLON stringLiteral
    ;

joinTypeParameter
    : TYPE COLON joinType
    ;

relationshipParameter
    : RELATIONSHIP COLON relationshipType
    ;

fromStatement
    : FROM COLON identifier
    ;

extendsStatement
    : EXTENDS COLON identifierList
    ;

identifierList
    : identifier (COMMA identifier)*
    ;

dimensionType
    : STRING | NUMBER | DATE | TIME | TIMESTAMP | BOOLEAN
    ;

measureType
    : SUM | COUNT | AVERAGE | MIN | MAX | COUNT_DISTINCT | NUMBER
    ;

joinType
    : LEFT_OUTER | INNER | FULL_OUTER | CROSS
    ;

relationshipType
    : ONE_TO_ONE | ONE_TO_MANY | MANY_TO_ONE | MANY_TO_MANY
    ;

formatName
    : USD | PERCENT | PERCENT_2 | DECIMAL_2
    ;

booleanValue
    : YES | NO | TRUE | FALSE
    ;

daxExpression
    : daxContent DOUBLE_SEMICOLON
    ;

daxContent
    : ~(DOUBLE_SEMICOLON | NEWLINE)*
    ;

stringLiteral
    : STRING_LITERAL
    ;

// Expression grammar with precedence from lowest to highest
expression
    : logicalOrExpression
    ;

logicalOrExpression
    : logicalAndExpression (OR logicalAndExpression)*
    ;

logicalAndExpression
    : comparisonExpression (AND comparisonExpression)*
    ;

comparisonExpression
    : additiveExpression ( (EQUALS | NOT_EQUALS | GTE | LTE | GREATER_THAN | LESS_THAN) additiveExpression )?
    ;

additiveExpression
    : multiplicativeExpression ( (PLUS | MINUS) multiplicativeExpression )*
    ;

multiplicativeExpression
    : primary ( (MULTIPLY | DIVIDE) primary )*
    ;

primary
    : LPAREN expression RPAREN
    | literal
    | fieldReference
    | functionCall
    ;

functionCall
    : AGGREGATE LPAREN namedArgument (COMMA namedArgument)* RPAREN (overClause)? # aggregateFunc
    | identifier LPAREN (expression (COMMA expression)*)? RPAREN                # simpleFunc
    ;

overClause
    : OVER LBRACE namedArgument (COMMA namedArgument)* RBRACE
    ;

namedArgument
    : identifier COLON value_
    ;

value_
    : expression
    | list_
    ;

list_
    : LBRACKET (expression (COMMA expression)*)? RBRACKET
    ;

fieldReference
    : DOLLAR_LBRACE identifier (DOT identifier)? RBRACE
    ;

literal
    : NUMBER_LITERAL
    | STRING_LITERAL
    | booleanLiteral
    ;

booleanLiteral
    : TRUE | FALSE
    ;

identifier
    : IDENTIFIER
    | STRING | NUMBER | DATE | TIME | TIMESTAMP | BOOLEAN
    | SUM | COUNT | AVERAGE | MIN | MAX | COUNT_DISTINCT
    | LEFT_OUTER | INNER | FULL_OUTER | CROSS
    | ONE_TO_ONE | ONE_TO_MANY | MANY_TO_ONE | MANY_TO_MANY
    | USD | PERCENT | PERCENT_2 | DECIMAL_2
    | YES | NO | TRUE | FALSE
    ;


// ===========================================================================
// LEXER RULES
// ===========================================================================

// Keywords
MODEL           : 'model';
VIEW            : 'view';
MEASURE         : 'measure';
DIMENSION       : 'dimension';
JOIN            : 'join';
TYPE            : 'type';
EXPRESSION      : 'expression';
LABEL           : 'label';
DESCRIPTION     : 'description';
PRIMARY_KEY     : 'primary_key';
HIDDEN_         : 'hidden';
VALUE_FORMAT    : 'value_format';
UNITS           : 'units';
RELATIONSHIP    : 'relationship';
FROM            : 'from';
EXTENDS         : 'extends';
AGGREGATE       : 'Aggregate';
OVER            : 'OVER';

// Dimension Types
STRING          : 'string';
NUMBER          : 'number';
DATE            : 'date';
TIME            : 'time';
TIMESTAMP       : 'timestamp';
BOOLEAN         : 'boolean';

// Measure Types
SUM             : 'sum';
COUNT           : 'count';
AVERAGE         : 'average';
MIN             : 'min';
MAX             : 'max';
COUNT_DISTINCT  : 'count_distinct';

// Join Types
LEFT_OUTER      : 'left_outer';
INNER           : 'inner';
FULL_OUTER      : 'full_outer';
CROSS           : 'cross';

// Relationship Types
ONE_TO_ONE      : 'one_to_one';
ONE_TO_MANY     : 'one_to_many';
MANY_TO_ONE     : 'many_to_one';
MANY_TO_MANY    : 'many_to_many';

// Format Names
USD             : 'usd';
PERCENT         : 'percent';
PERCENT_2       : 'percent_2';
DECIMAL_2       : 'decimal_2';

// Boolean Values
YES             : 'yes';
NO              : 'no';
TRUE            : 'true';
FALSE           : 'false';
AND             : 'and';
OR              : 'or';

// Delimiters
LPAREN          : '(';
RPAREN          : ')';
LBRACE          : '{';
RBRACE          : '}';
LBRACKET        : '[';
RBRACKET        : ']';
DOLLAR_LBRACE   : '${';
COLON           : ':';
COMMA           : ',';
DOT             : '.';
DOUBLE_SEMICOLON: ';;';

// Operators
PLUS            : '+';
MINUS           : '-';
MULTIPLY        : '*';
DIVIDE          : '/';
EQUALS          : '==';
NOT_EQUALS      : '!=';
GTE             : '>=';
LTE             : '<=';
GREATER_THAN    : '>';
LESS_THAN       : '<';

// Base tokens
IDENTIFIER      : [a-zA-Z_] [a-zA-Z0-9_]*;
STRING_LITERAL  : '"' ( ~["\\] | '\\' . )*? '"'; // Corrected for proper escaping
NUMBER_LITERAL  : '-'? [0-9]+ ('.' [0-9]+)?;

// Whitespace and Comments
COMMENT         : '#' ~[\r\n]* -> skip;
NEWLINE         : [\r\n]+;
WS              : [ \t]+ -> skip;
