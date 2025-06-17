/*
 * ANTLR4 Grammar for DAX (Data Analysis Expressions)
 * 
 * Complete grammar for DAX expressions used in Copper.
 * Converted from EBNF specification to ANTLR4 format.
 * 
 * This grammar can be imported by the main Copper grammar
 * or used standalone for full DAX parsing.
 */

lexer grammar DAX;

// ============================================================================
// DAX KEYWORDS AND OPERATORS
// ============================================================================

// Logical Operators
AND             : 'AND';
OR              : 'OR';
NOT             : 'NOT';
TRUE            : 'TRUE';
FALSE           : 'FALSE';
BLANK           : 'BLANK';

// Comparison Operators
EQ              : '=';
NE              : '<>' | '!=';
LT              : '<';
LE              : '<=';
GT              : '>';
GE              : '>=';
IN              : 'IN';

// Arithmetic Operators
PLUS            : '+';
MINUS           : '-';
MULTIPLY        : '*';
DIVIDE          : '/';
POWER           : '^';

// Logical Operators (symbolic)
LOGICAL_AND     : '&&';
LOGICAL_OR      : '||';

// DAX Keywords
VAR             : 'VAR';
RETURN          : 'RETURN';
IF              : 'IF';
SWITCH          : 'SWITCH';
RELATED         : 'RELATED';
RELATEDTABLE    : 'RELATEDTABLE';

// ============================================================================
// AGGREGATION FUNCTIONS
// ============================================================================

// Basic Aggregations
SUM             : 'SUM';
SUMX            : 'SUMX';
COUNT           : 'COUNT';
COUNTA          : 'COUNTA';
COUNTX          : 'COUNTX';
COUNTROWS       : 'COUNTROWS';
COUNTBLANK      : 'COUNTBLANK';
AVERAGE         : 'AVERAGE';
AVERAGEX        : 'AVERAGEX';
MIN             : 'MIN';
MINX            : 'MINX';
MAX             : 'MAX';
MAXX            : 'MAXX';
DISTINCTCOUNT   : 'DISTINCTCOUNT';
DISTINCTCOUNTNOBLANK : 'DISTINCTCOUNTNOBLANK';
MEDIAN          : 'MEDIAN';

// Statistical Functions
PERCENTILE_EXC  : 'PERCENTILE.EXC';
PERCENTILE_INC  : 'PERCENTILE.INC';
STDEV_P         : 'STDEV.P';
STDEV_S         : 'STDEV.S';
VAR_P           : 'VAR.P';
VAR_S           : 'VAR.S';

// ============================================================================
// FILTER FUNCTIONS
// ============================================================================

CALCULATE       : 'CALCULATE';
CALCULATETABLE  : 'CALCULATETABLE';
FILTER          : 'FILTER';
ALL             : 'ALL';
ALLEXCEPT       : 'ALLEXCEPT';
ALLSELECTED     : 'ALLSELECTED';
VALUES          : 'VALUES';
DISTINCT        : 'DISTINCT';
EARLIER         : 'EARLIER';
EARLIEST        : 'EARLIEST';
HASONEVALUE     : 'HASONEVALUE';
HASONEFILTER    : 'HASONEFILTER';
ISCROSSFILTERED : 'ISCROSSFILTERED';
ISFILTERED      : 'ISFILTERED';
SELECTEDVALUE   : 'SELECTEDVALUE';
USERRELATIONSHIP : 'USERRELATIONSHIP';

// ============================================================================
// LOGICAL FUNCTIONS
// ============================================================================

IFERROR         : 'IFERROR';
IFNA            : 'IFNA';
ISBLANK         : 'ISBLANK';
ISEMPTY         : 'ISEMPTY';
ISNUMBER        : 'ISNUMBER';
ISTEXT          : 'ISTEXT';

// ============================================================================
// MATHEMATICAL FUNCTIONS
// ============================================================================

ABS             : 'ABS';
CEILING         : 'CEILING';
FLOOR           : 'FLOOR';
ROUND           : 'ROUND';
ROUNDUP         : 'ROUNDUP';
ROUNDDOWN       : 'ROUNDDOWN';
TRUNC           : 'TRUNC';
MOD             : 'MOD';
QUOTIENT        : 'QUOTIENT';
SQRT            : 'SQRT';
EXP             : 'EXP';
LN              : 'LN';
LOG             : 'LOG';
LOG10           : 'LOG10';
SIGN            : 'SIGN';
PI              : 'PI';
DEGREES         : 'DEGREES';
RADIANS         : 'RADIANS';
SIN             : 'SIN';
COS             : 'COS';
TAN             : 'TAN';
ASIN            : 'ASIN';
ACOS            : 'ACOS';
ATAN            : 'ATAN';

// ============================================================================
// TEXT FUNCTIONS
// ============================================================================

CONCATENATE     : 'CONCATENATE';
CONCATENATEX    : 'CONCATENATEX';
LEFT            : 'LEFT';
RIGHT           : 'RIGHT';
MID             : 'MID';
LEN             : 'LEN';
TRIM            : 'TRIM';
UPPER           : 'UPPER';
LOWER           : 'LOWER';
PROPER          : 'PROPER';
SUBSTITUTE      : 'SUBSTITUTE';
REPLACE         : 'REPLACE';
REPT            : 'REPT';
FIND            : 'FIND';
SEARCH          : 'SEARCH';
EXACT           : 'EXACT';
FORMAT          : 'FORMAT';
VALUE           : 'VALUE';
UNICHAR         : 'UNICHAR';
UNICODE         : 'UNICODE';

// ============================================================================
// DATE/TIME FUNCTIONS
// ============================================================================

DATE            : 'DATE';
TIME            : 'TIME';
DATETIME        : 'DATETIME';
NOW             : 'NOW';
TODAY           : 'TODAY';
UTCNOW          : 'UTCNOW';
UTCTODAY        : 'UTCTODAY';
YEAR            : 'YEAR';
MONTH           : 'MONTH';
DAY             : 'DAY';
HOUR            : 'HOUR';
MINUTE          : 'MINUTE';
SECOND          : 'SECOND';
WEEKDAY         : 'WEEKDAY';
WEEKNUM         : 'WEEKNUM';
DATEDIFF        : 'DATEDIFF';
DATEADD         : 'DATEADD';
EOMONTH         : 'EOMONTH';
EDATE           : 'EDATE';

// Time Intelligence Functions
STARTOFYEAR     : 'STARTOFYEAR';
ENDOFYEAR       : 'ENDOFYEAR';
STARTOFQUARTER  : 'STARTOFQUARTER';
ENDOFQUARTER    : 'ENDOFQUARTER';
STARTOFMONTH    : 'STARTOFMONTH';
ENDOFMONTH      : 'ENDOFMONTH';
STARTOFWEEK     : 'STARTOFWEEK';
ENDOFWEEK       : 'ENDOFWEEK';
FIRSTDATE       : 'FIRSTDATE';
LASTDATE        : 'LASTDATE';
NEXTDAY         : 'NEXTDAY';
PREVIOUSDAY     : 'PREVIOUSDAY';
NEXTMONTH       : 'NEXTMONTH';
PREVIOUSMONTH   : 'PREVIOUSMONTH';
NEXTYEAR        : 'NEXTYEAR';
PREVIOUSYEAR    : 'PREVIOUSYEAR';
SAMEPERIODLASTYEAR : 'SAMEPERIODLASTYEAR';
TOTALYTD        : 'TOTALYTD';
TOTALQTD        : 'TOTALQTD';
TOTALMTD        : 'TOTALMTD';
DATESYTD        : 'DATESYTD';
DATESQTD        : 'DATESQTD';
DATESMTD        : 'DATESMTD';
DATESINPERIOD   : 'DATESINPERIOD';
DATESBETWEEN    : 'DATESBETWEEN';
PARALLELPERIOD  : 'PARALLELPERIOD';
CALENDARAUTO    : 'CALENDARAUTO';
CALENDAR        : 'CALENDAR';

// ============================================================================
// TABLE FUNCTIONS
// ============================================================================

ADDCOLUMNS      : 'ADDCOLUMNS';
SELECTCOLUMNS   : 'SELECTCOLUMNS';
SUMMARIZE       : 'SUMMARIZE';
SUMMARIZECOLUMNS : 'SUMMARIZECOLUMNS';
GROUPBY         : 'GROUPBY';
TOPN            : 'TOPN';
SAMPLE          : 'SAMPLE';
DATATABLE       : 'DATATABLE';
ROW             : 'ROW';
UNION           : 'UNION';
INTERSECT       : 'INTERSECT';
EXCEPT          : 'EXCEPT';
NATURALINNERJOIN : 'NATURALINNERJOIN';
NATURALLEFTOUTERJOIN : 'NATURALLEFTOUTERJOIN';
CROSSJOIN       : 'CROSSJOIN';
GENERATE        : 'GENERATE';
GENERATEALL     : 'GENERATEALL';
GENERATESERIES  : 'GENERATESERIES';

// ============================================================================
// INFORMATION FUNCTIONS
// ============================================================================

COLUMNCOUNT     : 'COLUMNCOUNT';
CONTAINS        : 'CONTAINS';
CONTAINSROW     : 'CONTAINSROW';
CONTAINSSTRING  : 'CONTAINSSTRING';
CONTAINSSTRINGEXACT : 'CONTAINSSTRINGEXACT';
CUSTOMDATA      : 'CUSTOMDATA';
ERROR           : 'ERROR';
ISAFTER         : 'ISAFTER';
ISINSCOPE       : 'ISINSCOPE';
ISLOGICAL       : 'ISLOGICAL';
ISONORAFTER     : 'ISONORAFTER';
ISSELECTEDMEASURE : 'ISSELECTEDMEASURE';
ISSUBTOTAL      : 'ISSUBTOTAL';
PATH            : 'PATH';
PATHCONTAINS    : 'PATHCONTAINS';
PATHITEM        : 'PATHITEM';
PATHITEMREVERSE : 'PATHITEMREVERSE';
PATHLENGTH      : 'PATHLENGTH';
USERNAME        : 'USERNAME';
USERPRINCIPALNAME : 'USERPRINCIPALNAME';

// ============================================================================
// DELIMITERS AND PUNCTUATION
// ============================================================================

LPAREN          : '(';
RPAREN          : ')';
LBRACKET        : '[';
RBRACKET        : ']';
LBRACE          : '{';
RBRACE          : '}';
COMMA           : ',';
SEMICOLON       : ';';
DOT             : '.';
APOSTROPHE      : '\'';

// ============================================================================
// LITERALS
// ============================================================================

// Identifiers (table names, column names, variables)
IDENTIFIER      : LETTER (LETTER | DIGIT | '_')*;

// Table names can be quoted with single quotes
QUOTED_TABLE_NAME : '\'' (~['\\] | '\\' . | '\'\'')* '\'';

// Column names in brackets
COLUMN_NAME     : '[' (~[\\[\]] | '\\' . | ']]' | '[[')* ']';

// String literals
STRING_LITERAL  : '"' (~["\\\r\n] | '\\' ('"' | '\\' | '/' | 'b' | 'f' | 'n' | 'r' | 't' | 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT))* '"';

// Numeric literals
INTEGER_LITERAL : DIGIT+;
DECIMAL_LITERAL : DIGIT+ '.' DIGIT+;
SCIENTIFIC_LITERAL : (INTEGER_LITERAL | DECIMAL_LITERAL) [eE] [+-]? DIGIT+;

NUMBER_LITERAL  : '-'? (SCIENTIFIC_LITERAL | DECIMAL_LITERAL | INTEGER_LITERAL);

// ============================================================================
// WHITESPACE AND COMMENTS
// ============================================================================

// Comments (DAX supports only single-line comments)
COMMENT         : '//' ~[\r\n]* -> channel(HIDDEN);

// Whitespace
WS              : [ \t\r\n]+ -> skip;

// ============================================================================
// FRAGMENTS
// ============================================================================

fragment LETTER : [a-zA-Z];
fragment DIGIT  : [0-9];
fragment HEX_DIGIT : [0-9a-fA-F];