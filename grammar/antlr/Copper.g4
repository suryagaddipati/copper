/*
 * ANTLR4 Grammar for Copper Language
 * 
 * A metadata format for describing data dimensions and measures,
 * inspired by LookML but using DAX expressions instead of SQL.
 * 
 * Converted from EBNF specification to ANTLR4 format.
 */

grammar Copper;

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

// ============================================================================
// VIEW STATEMENTS
// ============================================================================

viewStatement
    : VIEW COLON identifier LBRACE viewBody* RBRACE
    ;

viewBody
    : fromStatement
    | joinStatement
    | extendsStatement
    | extensionStatement
    | comment
    | NEWLINE
    ;

fromStatement
    : FROM COLON identifier
    ;

joinStatement
    : JOIN COLON identifier LBRACE joinParameter* RBRACE
    ;

extendsStatement
    : EXTENDS COLON LBRACKET identifierList RBRACKET
    ;

extensionStatement
    : EXTENSION COLON (REQUIRED | OPTIONAL)
    ;

// ============================================================================
// DIMENSION PARAMETERS
// ============================================================================

dimensionParameter
    : typeParameter
    | expressionParameter
    | primaryKeyParameter
    | valueFormatParameter
    | labelParameter
    | descriptionParameter
    | hiddenParameter
    | tiersParameter
    | sqlLatitudeParameter
    | sqlLongitudeParameter
    | unitsParameter
    | comment
    | NEWLINE
    ;

typeParameter
    : TYPE COLON dimensionType
    ;

dimensionType
    : STRING_TYPE
    | NUMBER_TYPE
    | DATE_TYPE
    | DATE_TIME_TYPE
    | YESNO_TYPE
    | TIER_TYPE
    | BIN_TYPE
    | LOCATION_TYPE
    | ZIPCODE_TYPE
    | DISTANCE_TYPE
    | DURATION_TYPE
    | TIME_TYPE
    | UNQUOTED_TYPE
    ;

// ============================================================================
// MEASURE PARAMETERS
// ============================================================================

measureParameter
    : measureTypeParameter
    | expressionParameter
    | valueFormatParameter
    | labelParameter
    | descriptionParameter
    | hiddenParameter
    | comment
    | NEWLINE
    ;

measureTypeParameter
    : TYPE COLON measureType
    ;

measureType
    : COUNT_TYPE
    | SUM_TYPE
    | AVERAGE_TYPE
    | MIN_TYPE
    | MAX_TYPE
    | COUNT_DISTINCT_TYPE
    | MEDIAN_TYPE
    | PERCENTILE_TYPE
    | NUMBER_TYPE  // 'number' can be both dimension and measure type
    ;

// ============================================================================
// JOIN PARAMETERS
// ============================================================================

joinParameter
    : joinTypeParameter
    | relationshipParameter
    | expressionParameter
    | comment
    | NEWLINE
    ;

joinTypeParameter
    : TYPE COLON joinType
    ;

joinType
    : LEFT_OUTER
    | INNER
    | FULL_OUTER
    | CROSS
    ;

relationshipParameter
    : RELATIONSHIP COLON relationshipType
    ;

relationshipType
    : ONE_TO_ONE
    | MANY_TO_ONE
    | ONE_TO_MANY
    | MANY_TO_MANY
    ;

// ============================================================================
// COMMON PARAMETERS
// ============================================================================

expressionParameter
    : EXPRESSION COLON daxExpression SEMICOLON_SEMICOLON
    ;

primaryKeyParameter
    : PRIMARY_KEY COLON booleanValue
    ;

valueFormatParameter
    : VALUE_FORMAT COLON (stringLiteral | formatName)
    ;

labelParameter
    : LABEL COLON stringLiteral
    ;

descriptionParameter
    : DESCRIPTION COLON stringLiteral
    ;

hiddenParameter
    : HIDDEN COLON booleanValue
    ;

tiersParameter
    : TIERS COLON LBRACKET (stringList | numberList) RBRACKET
    ;

sqlLatitudeParameter
    : SQL_LATITUDE COLON daxExpression SEMICOLON_SEMICOLON
    ;

sqlLongitudeParameter
    : SQL_LONGITUDE COLON daxExpression SEMICOLON_SEMICOLON
    ;

unitsParameter
    : UNITS COLON units
    ;

// ============================================================================
// DAX EXPRESSIONS (Blackbox for now)
// ============================================================================

daxExpression
    : DAX_STRING
    ;

// ============================================================================
// LITERALS AND BASIC TYPES
// ============================================================================

identifier
    : IDENTIFIER
    | contextualKeyword  // Handle keywords used as identifiers
    ;

contextualKeyword
    : STRING_TYPE | NUMBER_TYPE | DATE_TYPE | DATE_TIME_TYPE | YESNO_TYPE
    | TIER_TYPE | BIN_TYPE | LOCATION_TYPE | ZIPCODE_TYPE | DISTANCE_TYPE
    | DURATION_TYPE | TIME_TYPE | UNQUOTED_TYPE
    | COUNT_TYPE | SUM_TYPE | AVERAGE_TYPE | MIN_TYPE | MAX_TYPE
    | COUNT_DISTINCT_TYPE | MEDIAN_TYPE | PERCENTILE_TYPE
    | LEFT_OUTER | INNER | FULL_OUTER | CROSS
    | ONE_TO_ONE | MANY_TO_ONE | ONE_TO_MANY | MANY_TO_MANY
    | USD | EUR | GBP | PERCENT_1 | PERCENT_2 | DECIMAL_0 | DECIMAL_1 | DECIMAL_2 | ID
    | MILES | KILOMETERS | METERS | FEET
    ;

stringLiteral
    : STRING_LITERAL
    ;

numberLiteral
    : NUMBER_LITERAL
    ;

booleanValue
    : booleanLiteral
    ;

booleanLiteral
    : TRUE | FALSE | YES | NO
    ;

formatName
    : USD | EUR | GBP 
    | PERCENT_1 | PERCENT_2
    | DECIMAL_0 | DECIMAL_1 | DECIMAL_2
    | ID
    ;

units
    : MILES | KILOMETERS | METERS | FEET
    ;

// ============================================================================
// LISTS
// ============================================================================

identifierList
    : identifier (COMMA identifier)*
    ;

stringList
    : stringLiteral (COMMA stringLiteral)*
    ;

numberList
    : numberLiteral (COMMA numberLiteral)*
    ;

// ============================================================================
// LEXER RULES (start with uppercase)
// ============================================================================

// Keywords - Structural
MODEL           : 'model';
VIEW            : 'view';
DIMENSION       : 'dimension';
MEASURE         : 'measure';
FROM            : 'from';
JOIN            : 'join';
EXTENDS         : 'extends';
EXTENSION       : 'extension';
TYPE            : 'type';
EXPRESSION      : 'expression' -> pushMode(DAX_MODE);
PRIMARY_KEY     : 'primary_key';
VALUE_FORMAT    : 'value_format';
LABEL           : 'label';
DESCRIPTION     : 'description';
HIDDEN          : 'hidden';
TIERS           : 'tiers';
SQL_LATITUDE    : 'sql_latitude' -> pushMode(DAX_MODE);
SQL_LONGITUDE   : 'sql_longitude' -> pushMode(DAX_MODE);
UNITS           : 'units';
RELATIONSHIP    : 'relationship';

// Extension Types
REQUIRED        : 'required';
OPTIONAL        : 'optional';

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

// Join Types
LEFT_OUTER      : 'left_outer';
INNER           : 'inner';
FULL_OUTER      : 'full_outer';
CROSS           : 'cross';

// Relationship Types
ONE_TO_ONE      : 'one_to_one';
MANY_TO_ONE     : 'many_to_one';
ONE_TO_MANY     : 'one_to_many';
MANY_TO_MANY    : 'many_to_many';

// Format Names
USD             : 'usd';
EUR             : 'eur';
GBP             : 'gbp';
PERCENT_1       : 'percent_1';
PERCENT_2       : 'percent_2';
DECIMAL_0       : 'decimal_0';
DECIMAL_1       : 'decimal_1';
DECIMAL_2       : 'decimal_2';
ID              : 'id';

// Units
MILES           : 'miles';
KILOMETERS      : 'kilometers';
METERS          : 'meters';
FEET            : 'feet';

// Boolean Literals
TRUE            : 'true';
FALSE           : 'false';
YES             : 'yes';
NO              : 'no';

// Delimiters
COLON           : ':';
SEMICOLON       : ';';
SEMICOLON_SEMICOLON : ';;';
LBRACE          : '{';
RBRACE          : '}';
LBRACKET        : '[';
RBRACKET        : ']';
COMMA           : ',';

// Literals
IDENTIFIER      : LETTER (LETTER | DIGIT | '_')*;

STRING_LITERAL  : '"' (~["\\\r\n] | '\\' ('"' | '\\' | '/' | 'b' | 'f' | 'n' | 'r' | 't'))* '"';

NUMBER_LITERAL  : '-'? DIGIT+ ('.' DIGIT+)?;

// Comments
COMMENT         : '#' ~[\r\n]* -> channel(HIDDEN);

// Whitespace
NEWLINE         : ('\r'? '\n')+;
WS              : [ \t]+ -> skip;

// Character classes
fragment LETTER : [a-zA-Z];
fragment DIGIT  : [0-9];

// ============================================================================
// DAX MODE for parsing DAX expressions as strings
// ============================================================================

mode DAX_MODE;

DAX_STRING      : ':' WS_DAX* (~[;] | ';' ~[;])+ -> popMode;
WS_DAX          : [ \t\r\n]+ -> skip;
DAX_COMMENT     : '#' ~[\r\n]* -> channel(HIDDEN);