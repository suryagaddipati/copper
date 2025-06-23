/*
 * Simplified ANTLR4 Grammar for Copper Language
 * 
 * A metadata format for describing data dimensions and measures,
 * inspired by LookML but using DAX expressions instead of SQL.
 * 
 * This version treats DAX expressions as simple string literals.
 */

grammar CopperSimple;

// ============================================================================
// PARSER RULES (start with lowercase)
// ============================================================================

// Entry point
program
    : statement* EOF
    ;

statement
    : modelStatement
    | viewStatement
    | comment
    | NEWLINE
    ;

comment
    : COMMENT
    ;

// ============================================================================
// MODEL STATEMENTS
// ============================================================================

modelStatement
    : MODEL COLON identifier LBRACE modelBody* RBRACE
    ;

modelBody
    : dimensionStatement
    | measureStatement
    | comment
    | NEWLINE
    ;

dimensionStatement
    : DIMENSION COLON identifier LBRACE dimensionParameter* RBRACE
    ;

measureStatement
    : MEASURE COLON identifier LBRACE measureParameter* RBRACE
    ;

dimensionParameter
    : typeParameter
    | expressionParameter
    | labelParameter
    | descriptionParameter
    | primaryKeyParameter
    | hiddenParameter
    | valueFormatParameter
    | tiersParameter
    | sqlLatitudeParameter
    | sqlLongitudeParameter
    | unitsParameter
    | comment
    | NEWLINE
    ;

measureParameter
    : typeParameter
    | expressionParameter
    | labelParameter
    | descriptionParameter
    | hiddenParameter
    | valueFormatParameter
    | unitsParameter
    | comment
    | NEWLINE
    ;

// ============================================================================
// VIEW STATEMENTS
// ============================================================================

viewStatement
    : VIEW COLON identifier LBRACE viewBody* RBRACE
    ;

viewBody
    : fromParameter
    | extendsParameter
    | joinStatement
    | dimensionStatement
    | measureStatement
    | comment
    | NEWLINE
    ;

joinStatement
    : JOIN COLON identifier LBRACE joinParameter* RBRACE
    ;

joinParameter
    : typeParameter
    | relationshipParameter
    | expressionParameter
    | comment
    | NEWLINE
    ;

// ============================================================================
// PARAMETER DEFINITIONS
// ============================================================================

typeParameter
    : TYPE COLON typeValue SEMICOLON SEMICOLON?
    ;

expressionParameter
    : EXPRESSION COLON daxExpression SEMICOLON SEMICOLON
    ;

labelParameter
    : LABEL COLON stringValue SEMICOLON SEMICOLON?
    ;

descriptionParameter
    : DESCRIPTION COLON stringValue SEMICOLON SEMICOLON?
    ;

primaryKeyParameter
    : PRIMARY_KEY COLON booleanValue SEMICOLON SEMICOLON?
    ;

hiddenParameter
    : HIDDEN_PARAM COLON booleanValue SEMICOLON SEMICOLON?
    ;

valueFormatParameter
    : VALUE_FORMAT COLON formatValue SEMICOLON SEMICOLON?
    ;

tiersParameter
    : TIERS COLON arrayValue SEMICOLON SEMICOLON?
    ;

sqlLatitudeParameter
    : SQL_LATITUDE COLON daxExpression SEMICOLON SEMICOLON
    ;

sqlLongitudeParameter
    : SQL_LONGITUDE COLON daxExpression SEMICOLON SEMICOLON
    ;

unitsParameter
    : UNITS COLON stringValue SEMICOLON SEMICOLON?
    ;

fromParameter
    : FROM COLON identifier SEMICOLON SEMICOLON?
    ;

extendsParameter
    : EXTENDS COLON identifier SEMICOLON SEMICOLON?
    ;

relationshipParameter
    : RELATIONSHIP COLON relationshipValue SEMICOLON SEMICOLON?
    ;

// ============================================================================
// VALUE TYPES
// ============================================================================

typeValue
    : STRING_TYPE | NUMBER_TYPE | DATE_TYPE | DATE_TIME_TYPE
    | YESNO_TYPE | TIER_TYPE | BIN_TYPE | LOCATION_TYPE
    | ZIPCODE_TYPE | DISTANCE_TYPE | DURATION_TYPE | TIME_TYPE
    | UNQUOTED_TYPE | COUNT_TYPE | SUM_TYPE | AVERAGE_TYPE
    | MIN_TYPE | MAX_TYPE | COUNT_DISTINCT_TYPE | MEDIAN_TYPE
    | PERCENTILE_TYPE
    ;

relationshipValue
    : ONE_TO_ONE | ONE_TO_MANY | MANY_TO_ONE | MANY_TO_MANY
    ;

booleanValue
    : YES | NO
    ;

stringValue
    : STRING_LITERAL | identifier
    ;

formatValue
    : USD | PERCENT | PERCENT_1 | PERCENT_2 | STRING_LITERAL
    ;

arrayValue
    : LBRACKET (INTEGER (COMMA INTEGER)*)? RBRACKET
    ;

daxExpression
    : DAX_EXPRESSION
    ;

identifier
    : IDENTIFIER
    ;

// ============================================================================
// LEXER RULES (start with uppercase)
// ============================================================================

// Keywords
MODEL           : 'model';
VIEW            : 'view';
DIMENSION       : 'dimension';
MEASURE         : 'measure';
JOIN            : 'join';
FROM            : 'from';
EXTENDS         : 'extends';
TYPE            : 'type';
EXPRESSION      : 'expression';
PRIMARY_KEY     : 'primary_key';
VALUE_FORMAT    : 'value_format';
LABEL           : 'label';
DESCRIPTION     : 'description';
HIDDEN_PARAM    : 'hidden';
TIERS           : 'tiers';
SQL_LATITUDE    : 'sql_latitude';
SQL_LONGITUDE   : 'sql_longitude';
UNITS           : 'units';
RELATIONSHIP    : 'relationship';

// Dimension Types
STRING_TYPE     : 'string';
NUMBER_TYPE     : 'number';
DATE_TYPE       : 'date';
DATE_TIME_TYPE  : 'date_time';
YESNO_TYPE      : 'yesno';
TIER_TYPE       : 'tier';
BIN_TYPE        : 'bin';
LOCATION_TYPE   : 'location';
ZIPCODE_TYPE    : 'zipcode';
DISTANCE_TYPE   : 'distance';
DURATION_TYPE   : 'duration';
TIME_TYPE       : 'time';
UNQUOTED_TYPE   : 'unquoted';

// Measure Types
COUNT_TYPE      : 'count';
SUM_TYPE        : 'sum';
AVERAGE_TYPE    : 'average';
MIN_TYPE        : 'min';
MAX_TYPE        : 'max';
COUNT_DISTINCT_TYPE : 'count_distinct';
MEDIAN_TYPE     : 'median';
PERCENTILE_TYPE : 'percentile';

// Relationship Types
ONE_TO_ONE      : 'one_to_one';
ONE_TO_MANY     : 'one_to_many';
MANY_TO_ONE     : 'many_to_one';
MANY_TO_MANY    : 'many_to_many';

// Boolean Values
YES             : 'yes';
NO              : 'no';

// Format Values
USD             : 'usd';
PERCENT         : 'percent';
PERCENT_1       : 'percent_1';
PERCENT_2       : 'percent_2';

// Punctuation
COLON           : ':';
SEMICOLON       : ';';
LBRACE          : '{';
RBRACE          : '}';
LBRACKET        : '[';
RBRACKET        : ']';
COMMA           : ',';

// Literals
IDENTIFIER      : [a-zA-Z_][a-zA-Z0-9_]*;
INTEGER         : [0-9]+;
STRING_LITERAL  : '"' (~["\\\r\n] | '\\' .)* '"';

// DAX Expression - everything between colon and double semicolon
DAX_EXPRESSION  : ':' .*? ';;';

// Comments
COMMENT         : '#' ~[\r\n]*;

// Whitespace
NEWLINE         : ('\r'? '\n')+;
WS              : [ \t]+ -> skip;