

/*
 * ANTLR4 Grammar for DAX (Data Analysis Expressions)
 *
 * This grammar provides a complete parser for DAX expressions,
 * suitable for integration into other tools or for standalone validation.
 */

grammar DAXParser;

// ===========================================================================
// PARSER RULES
// ===========================================================================

// Entry point for a DAX expression
daxExpression
    : expression EOF
    ;

expression
    : singleExpression (comparisonOperator singleExpression)*
    ;

singleExpression
    : term (additiveOperator term)*
    ;

term
    : factor (multiplicativeOperator factor)*
    ;

factor
    : (PLUS | MINUS)? primaryExpression
    ;

primaryExpression
    : parenthesizedExpression
    | functionCall
    | columnOrMeasureReference
    | literal
    | variableReference
    ;

parenthesizedExpression
    : LPAREN expression RPAREN
    ;

literal
    : stringLiteral
    | numberLiteral
    | booleanLiteral
    | BLANK
    ;

stringLiteral
    : STRING_LITERAL
    ;

numberLiteral
    : NUMBER_LITERAL
    ;

booleanLiteral
    : TRUE
    | FALSE
    ;

columnOrMeasureReference
    : (quotedTableName? LBRACKET columnName RBRACKET)
    | (LBRACKET measureName RBRACKET)
    ;

quotedTableName
    : QUOTED_TABLE_NAME
    ;

columnName
    : IDENTIFIER
    ;

measureName
    : IDENTIFIER
    ;

variableReference
    : IDENTIFIER
    ;

functionCall
    : functionName LPAREN argumentList? RPAREN
    ;

functionName
    : IDENTIFIER
    ;

argumentList
    : expression (COMMA expression)*
    ;

// Operators
comparisonOperator
    : EQ | NE | LT | LE | GT | GE
    ;

additiveOperator
    : PLUS | MINUS
    ;

multiplicativeOperator
    : MULTIPLY | DIVIDE
    ;

// ===========================================================================
// LEXER RULES
// ===========================================================================

// Keywords
VAR             : 'VAR';
RETURN          : 'RETURN';
IF              : 'IF';
SWITCH          : 'SWITCH';
AND             : 'AND';
OR              : 'OR';
NOT             : 'NOT';
TRUE            : 'TRUE';
FALSE           : 'FALSE';
BLANK           : 'BLANK';

// Functions (a selection, can be extended)
SUM             : 'SUM';
AVERAGE         : 'AVERAGE';
MIN             : 'MIN';
MAX             : 'MAX';
COUNT           : 'COUNT';
DISTINCTCOUNT   : 'DISTINCTCOUNT';
CALCULATE       : 'CALCULATE';
FILTER          : 'FILTER';
RELATED         : 'RELATED';
VALUES          : 'VALUES';
DATE            : 'DATE';
YEAR            : 'YEAR';
MONTH           : 'MONTH';
DAY             : 'DAY';
TODAY           : 'TODAY';
NOW             : 'NOW';
DIVIDE          : 'DIVIDE';

// Operators
PLUS            : '+';
MINUS           : '-';
MULTIPLY        : '*';
DIVIDE          : '/';
EQ              : '=';
NE              : '<>' | '!=';
LT              : '<';
LE              : '<=';
GT              : '>';
GE              : '>=';
LOGICAL_AND     : '&&';
LOGICAL_OR      : '||';

// Delimiters
LPAREN          : '(';
RPAREN          : ')';
LBRACKET        : '[';
RBRACKET        : ']';
LBRACE          : '{';
LBRACE          : '}';
COMMA           : ',';
DOT             : '.';

// Literals
IDENTIFIER      : [a-zA-Z_] [a-zA-Z0-9_]*;
QUOTED_TABLE_NAME : '\'' ~['\'] '\'';
STRING_LITERAL  : '"' ( ~('"'|'\') | ('\' .) )* '"';
NUMBER_LITERAL  : ('-')? [0-9]+ ('.' [0-9]+)?;

// Comments and Whitespace
COMMENT         : '//' ~[\r\n]* -> channel(HIDDEN);
WS              : [ \t\r\n]+ -> skip;

