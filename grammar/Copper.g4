grammar Copper;

// Parser Rules
expression
    : logicalOrExpression
    ;

logicalOrExpression
    : logicalAndExpression (OR logicalAndExpression)*
    ;

logicalAndExpression
    : equalityExpression (AND equalityExpression)*
    ;

equalityExpression
    : relationalExpression ((EQUALS | NOT_EQUALS) relationalExpression)*
    ;

relationalExpression
    : additiveExpression ((LESS_THAN | GREATER_THAN | LESS_THAN_EQUALS | GREATER_THAN_EQUALS) additiveExpression)*
    ;

additiveExpression
    : multiplicativeExpression ((PLUS | MINUS) multiplicativeExpression)*
    ;

multiplicativeExpression
    : unaryExpression ((MULTIPLY | DIVIDE) unaryExpression)*
    ;

unaryExpression
    : (NOT | MINUS) unaryExpression
    | primaryExpression
    ;

primaryExpression
    : literal
    | identifier
    | functionCall
    | columnReference
    | conditionalExpression
    | LPAREN expression RPAREN
    ;

functionCall
    : functionName LPAREN argumentList? RPAREN
    ;

functionName
    : SUM | COUNT | AVG | MIN | MAX | IF | SWITCH | CASE
    | DATE_TRUNC | YEAR | MONTH | DAY
    | COALESCE | ISNULL | ISBLANK
    | identifier
    ;

argumentList
    : expression (COMMA expression)*
    ;

conditionalExpression
    : ifExpression
    | switchExpression
    | caseExpression
    ;

ifExpression
    : IF LPAREN expression COMMA expression COMMA expression RPAREN
    ;

switchExpression
    : SWITCH LPAREN expression COMMA switchCaseList defaultCase? RPAREN
    ;

switchCaseList
    : switchCase (COMMA switchCase)*
    ;

switchCase
    : expression COMMA expression
    ;

defaultCase
    : COMMA expression
    ;

caseExpression
    : CASE whenClauseList elseClause? END
    ;

whenClauseList
    : whenClause+
    ;

whenClause
    : WHEN expression THEN expression
    ;

elseClause
    : ELSE expression
    ;

columnReference
    : tableName DOT columnName
    | columnName
    ;

tableName
    : identifier
    ;

columnName
    : identifier
    ;

identifier
    : IDENTIFIER
    | QUOTED_IDENTIFIER
    ;

literal
    : NUMBER
    | STRING
    | BOOLEAN
    | NULL
    ;

// Lexer Rules
// Keywords
SUM         : 'SUM';
COUNT       : 'COUNT';
AVG         : 'AVG';
MIN         : 'MIN';
MAX         : 'MAX';
IF          : 'IF';
SWITCH      : 'SWITCH';
CASE        : 'CASE';
WHEN        : 'WHEN';
THEN        : 'THEN';
ELSE        : 'ELSE';
END         : 'END';
AND         : 'AND';
OR          : 'OR';
NOT         : 'NOT';
WHERE       : 'WHERE';
DATE_TRUNC  : 'DATE_TRUNC';
YEAR        : 'YEAR';
MONTH       : 'MONTH';
DAY         : 'DAY';
COALESCE    : 'COALESCE';
ISNULL      : 'ISNULL';
ISBLANK     : 'ISBLANK';
NULL        : 'NULL';

// Operators
EQUALS              : '=';
NOT_EQUALS          : '<>' | '!=';
LESS_THAN           : '<';
GREATER_THAN        : '>';
LESS_THAN_EQUALS    : '<=';
GREATER_THAN_EQUALS : '>=';
PLUS                : '+';
MINUS               : '-';
MULTIPLY            : '*';
DIVIDE              : '/';

// Delimiters
LPAREN      : '(';
RPAREN      : ')';
COMMA       : ',';
DOT         : '.';

// Literals
NUMBER
    : [0-9]+ ('.' [0-9]+)?
    | '.' [0-9]+
    ;

STRING
    : '\'' (~['\r\n] | '\'\'')* '\''
    | '"' (~["\r\n] | '""')* '"'
    ;

BOOLEAN
    : 'TRUE'
    | 'FALSE'
    | 'true'
    | 'false'
    ;

// Identifiers
IDENTIFIER
    : [a-zA-Z_][a-zA-Z0-9_]*
    ;

QUOTED_IDENTIFIER
    : '[' (~[[\]'\r\n])* ']'
    ;

// Whitespace and Comments
WS
    : [ \t\r\n]+ -> skip
    ;

LINE_COMMENT
    : '//' ~[\r\n]* -> skip
    ;

BLOCK_COMMENT
    : '/*' .*? '*/' -> skip
    ;