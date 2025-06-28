import * as monaco from 'monaco-editor'

// Comprehensive Copper language syntax highlighting configuration
export const copperLanguageDefinition: monaco.languages.IMonarchLanguage = {
  // Set defaultToken to invalid to see what you do not tokenize yet
  defaultToken: '',
  ignoreCase: false,
  
  // Keywords for the Copper language
  keywords: [
    'model', 'view', 'dimension', 'measure', 'join', 'parameter',
    'type', 'expression', 'label', 'description', 'value_format',
    'primary_key', 'hidden', 'tiers', 'sql_latitude', 'sql_longitude',
    'units', 'relationship', 'from', 'extends', 'extension', 'required'
  ],

  // Data types
  typeKeywords: [
    'string', 'number', 'count', 'count_distinct', 'sum', 'average',
    'median', 'min', 'max', 'date', 'date_time', 'duration', 'yesno',
    'tier', 'location', 'zipcode', 'distance', 'time'
  ],

  // Join types
  joinTypes: [
    'inner', 'left_outer', 'right_outer', 'full_outer', 'cross'
  ],

  // Relationship types
  relationships: [
    'one_to_one', 'one_to_many', 'many_to_one', 'many_to_many'
  ],

  // Value formats
  formats: [
    'usd', 'eur', 'gbp', 'jpy', 'cad', 'aud', 'chf', 'cny',
    'percent', 'percent_0', 'percent_1', 'percent_2', 'percent_3', 'percent_4',
    'decimal_0', 'decimal_1', 'decimal_2', 'decimal_3', 'decimal_4',
    'id', 'email', 'url', 'phone', 'miles', 'kilometers', 'scientific'
  ],

  // Boolean values
  booleans: ['yes', 'no', 'true', 'false'],

  // DAX functions (comprehensive list)
  daxFunctions: [
    // Aggregation functions
    'SUM', 'COUNT', 'COUNTROWS', 'COUNTA', 'COUNTAX', 'COUNTBLANK', 'COUNTX',
    'AVERAGE', 'AVERAGEA', 'AVERAGEX', 'MIN', 'MINA', 'MINX', 'MAX', 'MAXA', 'MAXX',
    'MEDIAN', 'MEDIANX', 'STDEV.P', 'STDEV.S', 'STDEVX.P', 'STDEVX.S',
    'VAR.P', 'VAR.S', 'VARX.P', 'VARX.S', 'GEOMEAN', 'GEOMEANX',
    
    // Filter functions
    'CALCULATE', 'CALCULATETABLE', 'FILTER', 'ALL', 'ALLEXCEPT', 'ALLNOBLANKROW',
    'ALLSELECTED', 'EARLIER', 'EARLIEST', 'HASONEFILTER', 'HASONEVALUE',
    'ISFILTERED', 'ISCROSSFILTERED', 'KEEPFILTERS', 'REMOVEFILTERS',
    'SELECTEDVALUE', 'USERELATIONSHIP',
    
    // Relationship functions
    'RELATED', 'RELATEDTABLE', 'LOOKUPVALUE', 'CROSSFILTER',
    
    // Table functions
    'DISTINCT', 'DISTINCTCOUNT', 'VALUES', 'SUMMARIZE', 'SUMMARIZECOLUMNS',
    'ADDCOLUMNS', 'SELECTCOLUMNS', 'TOPN', 'SAMPLE', 'DATATABLE',
    'ROW', 'UNION', 'INTERSECT', 'EXCEPT', 'NATURALINNERJOIN', 'NATURALLEFTOUTERJOIN',
    
    // Iterator functions
    'SUMX', 'AVERAGEX', 'MAXX', 'MINX', 'PRODUCTX', 'CONCATENATEX',
    'RANKX', 'PERCENTILEX.EXC', 'PERCENTILEX.INC',
    
    // Logical functions
    'IF', 'IFERROR', 'IFNA', 'SWITCH', 'AND', 'OR', 'NOT', 'TRUE', 'FALSE',
    'ISBLANK', 'ISEMPTY', 'ISERROR', 'ISLOGICAL', 'ISNONTEXT', 'ISNUMBER', 'ISTEXT',
    
    // Math functions
    'ABS', 'CEILING', 'FLOOR', 'ROUND', 'ROUNDUP', 'ROUNDDOWN', 'TRUNC',
    'MOD', 'QUOTIENT', 'SIGN', 'SQRT', 'POWER', 'EXP', 'LN', 'LOG', 'LOG10',
    'PI', 'RADIANS', 'DEGREES', 'SIN', 'COS', 'TAN', 'ASIN', 'ACOS', 'ATAN',
    'DIVIDE', 'GCD', 'LCM', 'FACT', 'COMBIN', 'PERMUT',
    
    // Text functions
    'CONCATENATE', 'EXACT', 'FIND', 'LEFT', 'LEN', 'LOWER', 'MID', 'REPLACE',
    'REPT', 'RIGHT', 'SEARCH', 'SUBSTITUTE', 'TRIM', 'UPPER', 'VALUE',
    'FORMAT', 'FIXED', 'UNICHAR', 'UNICODE',
    
    // Date/Time functions
    'DATE', 'DATEVALUE', 'TIME', 'TIMEVALUE', 'NOW', 'TODAY', 'UTCNOW', 'UTCTODAY',
    'YEAR', 'MONTH', 'DAY', 'HOUR', 'MINUTE', 'SECOND', 'WEEKDAY', 'WEEKNUM',
    'YEARFRAC', 'DATEDIFF', 'DATEADD', 'EOMONTH', 'EDATE',
    'CALENDAR', 'CALENDARAUTO', 'STARTOFMONTH', 'STARTOFQUARTER', 'STARTOFYEAR',
    'ENDOFMONTH', 'ENDOFQUARTER', 'ENDOFYEAR',
    
    // Time Intelligence functions
    'CLOSINGBALANCEMONTH', 'CLOSINGBALANCEQUARTER', 'CLOSINGBALANCEYEAR',
    'OPENINGBALANCEMONTH', 'OPENINGBALANCEQUARTER', 'OPENINGBALANCEYEAR',
    'TOTALMTD', 'TOTALQTD', 'TOTALYTD', 'DATESBETWEEN', 'DATESINPERIOD',
    'DATESMTD', 'DATESQTD', 'DATESYTD', 'FIRSTDATE', 'LASTDATE',
    'NEXTDAY', 'NEXTMONTH', 'NEXTQUARTER', 'NEXTYEAR',
    'PREVIOUSDAY', 'PREVIOUSMONTH', 'PREVIOUSQUARTER', 'PREVIOUSYEAR',
    'SAMEPERIODLASTYEAR', 'PARALLELPERIOD', 'FIRSTNONBLANK', 'LASTNONBLANK',
    
    // Statistical functions
    'BETA.DIST', 'BETA.INV', 'CHISQ.DIST', 'CHISQ.DIST.RT', 'CHISQ.INV', 'CHISQ.INV.RT',
    'CONFIDENCE.NORM', 'CONFIDENCE.T', 'EXPON.DIST', 'NORM.DIST', 'NORM.INV',
    'NORM.S.DIST', 'NORM.S.INV', 'POISSON.DIST', 'T.DIST', 'T.DIST.2T', 'T.DIST.RT',
    'T.INV', 'T.INV.2T', 'WEIBULL.DIST',
    
    // Information functions
    'BLANK', 'ERROR', 'HASONEFILTER', 'HASONEVALUE', 'ISBLANK', 'ISERROR',
    'ISEVEN', 'ISLOGICAL', 'ISNONTEXT', 'ISNUMBER', 'ISODD', 'ISTEXT',
    'USERNAME', 'USERPRINCIPALNAME'
  ],

  // DAX keywords and operators
  daxKeywords: [
    'VAR', 'RETURN', 'EVALUATE', 'ORDER BY', 'ASC', 'DESC',
    'DEFINE', 'MEASURE', 'COLUMN', 'TABLE'
  ],

  // Escape sequences
  escapes: /\\(?:[abfnrtv\\"']|x[0-9A-Fa-f]{1,4}|u[0-9A-Fa-f]{4}|U[0-9A-Fa-f]{8})/,

  // The main tokenizer for our languages
  tokenizer: {
    root: [
      // Comments MUST be first to take precedence - use custom token name
      [/#.*$/, 'copper-comment'],
      
      // Whitespace
      [/\s+/, ''],

      // Block declarations with highlighting for names
      [/(model|view|dimension|measure|join|parameter)(\s*)(:)(\s*)([a-zA-Z_][a-zA-Z0-9_]*)/, [
        'keyword.declaration', '', 'delimiter.colon', '', 'entity.name'
      ]],

      // Property keywords (highlighted differently)
      [/\b(type|expression|label|description|value_format|primary_key|hidden|tiers|sql_latitude|sql_longitude|units|relationship|from|extends|extension|required)(\s*)(:)/, [
        'keyword.property', '', 'delimiter.colon'
      ]],

      // Data types
      [/\b(string|number|count|count_distinct|sum|average|median|min|max|date|date_time|duration|yesno|tier|location|zipcode|distance|time)\b/, 'type'],

      // Join and relationship types
      [/\b(inner|left_outer|right_outer|full_outer|cross)\b/, 'keyword.join'],
      [/\b(one_to_one|one_to_many|many_to_one|many_to_many)\b/, 'keyword.relationship'],

      // Value formats
      [/\b(usd|eur|gbp|jpy|cad|aud|chf|cny|percent|percent_[0-4]|decimal_[0-4]|id|email|url|phone|miles|kilometers|scientific)\b/, 'constant.format'],

      // Boolean values
      [/\b(yes|no|true|false)\b/, 'constant.boolean'],

      // Array/tier values
      [/\[\s*[0-9,\s"'a-zA-Z_-]+\s*\]/, 'constant.array'],

      // DAX expression start (colon followed by space/content until ;;)
      [/:(?=\s)/, { token: 'delimiter.dax.start', next: '@daxExpression' }],

      // Quoted strings
      [/"([^"\\]|\\.)*$/, 'string.invalid'],  // non-terminated string
      [/"/, { token: 'string.quote', bracket: '@open', next: '@string' }],
      [/'([^'\\]|\\.)*$/, 'string.invalid'],  // non-terminated string
      [/'/, { token: 'string.quote', bracket: '@open', next: '@stringSingle' }],

      // Custom format strings (quoted with special highlighting)
      [/"[0-9#.,%;$€£¥-]+\s*"/, 'string.format'],

      // Numbers
      [/\d*\.\d+([eE][\-+]?\d+)?[fFlL]?/, 'number.float'],
      [/0[xX][\da-fA-F]+[lL]?/, 'number.hex'],
      [/\d+[lL]?/, 'number'],

      // Table[Column] references (common in DAX)
      [/[A-Za-z_][A-Za-z0-9_]*\[[A-Za-z_][A-Za-z0-9_]*\]/, 'variable.table-column'],

      // Identifiers
      [/[a-zA-Z_][a-zA-Z0-9_]*/, 'identifier'],

      // Brackets and braces with better categorization
      [/\[/, { token: 'delimiter.bracket', bracket: '@open' }],
      [/\]/, { token: 'delimiter.bracket', bracket: '@close' }],
      [/\{/, { token: 'delimiter.curly', bracket: '@open' }],
      [/\}/, { token: 'delimiter.curly', bracket: '@close' }],
      [/\(/, { token: 'delimiter.parenthesis', bracket: '@open' }],
      [/\)/, { token: 'delimiter.parenthesis', bracket: '@close' }],

      // Operators
      [/[=<>!]+/, 'operator'],
      [/[,;]/, 'delimiter'],
      [/[+\-*/]/, 'operator.arithmetic'],
    ],

    daxExpression: [
      // End DAX expression with double semicolon
      [/;;/, { token: 'delimiter.dax.end', next: '@pop' }],
      
      // Multi-line DAX with proper indentation
      [/\n/, ''],
      [/\s+/, ''],
      
      // DAX functions - comprehensive list
      [/\b(SUM|COUNT|COUNTROWS|COUNTA|COUNTAX|COUNTBLANK|COUNTX|AVERAGE|AVERAGEA|AVERAGEX|MIN|MINA|MINX|MAX|MAXA|MAXX|MEDIAN|MEDIANX)\b/, 'support.function.aggregation'],
      [/\b(CALCULATE|CALCULATETABLE|FILTER|ALL|ALLEXCEPT|ALLNOBLANKROW|ALLSELECTED|EARLIER|EARLIEST|HASONEFILTER|HASONEVALUE|ISFILTERED|ISCROSSFILTERED|KEEPFILTERS|REMOVEFILTERS|SELECTEDVALUE|USERELATIONSHIP)\b/, 'support.function.filter'],
      [/\b(RELATED|RELATEDTABLE|LOOKUPVALUE|CROSSFILTER)\b/, 'support.function.relationship'],
      [/\b(DISTINCT|DISTINCTCOUNT|VALUES|SUMMARIZE|SUMMARIZECOLUMNS|ADDCOLUMNS|SELECTCOLUMNS|TOPN|SAMPLE|DATATABLE|ROW|UNION|INTERSECT|EXCEPT)\b/, 'support.function.table'],
      [/\b(SUMX|AVERAGEX|MAXX|MINX|PRODUCTX|CONCATENATEX|RANKX|PERCENTILEX\.EXC|PERCENTILEX\.INC)\b/, 'support.function.iterator'],
      [/\b(IF|IFERROR|IFNA|SWITCH|AND|OR|NOT|TRUE|FALSE|ISBLANK|ISEMPTY|ISERROR|ISLOGICAL|ISNONTEXT|ISNUMBER|ISTEXT)\b/, 'support.function.logical'],
      [/\b(ABS|CEILING|FLOOR|ROUND|ROUNDUP|ROUNDDOWN|TRUNC|MOD|QUOTIENT|SIGN|SQRT|POWER|EXP|LN|LOG|LOG10|PI|RADIANS|DEGREES|SIN|COS|TAN|ASIN|ACOS|ATAN|DIVIDE|GCD|LCM|FACT|COMBIN|PERMUT)\b/, 'support.function.math'],
      [/\b(CONCATENATE|EXACT|FIND|LEFT|LEN|LOWER|MID|REPLACE|REPT|RIGHT|SEARCH|SUBSTITUTE|TRIM|UPPER|VALUE|FORMAT|FIXED|UNICHAR|UNICODE)\b/, 'support.function.text'],
      [/\b(DATE|DATEVALUE|TIME|TIMEVALUE|NOW|TODAY|UTCNOW|UTCTODAY|YEAR|MONTH|DAY|HOUR|MINUTE|SECOND|WEEKDAY|WEEKNUM|YEARFRAC|DATEDIFF|DATEADD|EOMONTH|EDATE)\b/, 'support.function.datetime'],
      [/\b(TOTALMTD|TOTALQTD|TOTALYTD|DATESBETWEEN|DATESINPERIOD|DATESMTD|DATESQTD|DATESYTD|FIRSTDATE|LASTDATE|SAMEPERIODLASTYEAR|PARALLELPERIOD|FIRSTNONBLANK|LASTNONBLANK)\b/, 'support.function.timeintel'],
      [/\b(BLANK|ERROR|USERNAME|USERPRINCIPALNAME)\b/, 'support.function.info'],
      
      // DAX keywords
      [/\b(VAR|RETURN|EVALUATE|ORDER\s+BY|ASC|DESC|DEFINE|MEASURE|COLUMN|TABLE)\b/, 'keyword.dax'],
      
      // Table and column references with better highlighting
      [/([A-Za-z_][A-Za-z0-9_]*)(\[)([A-Za-z_][A-Za-z0-9_]*)(\])/, [
        'entity.name.table', 'delimiter.bracket', 'entity.name.column', 'delimiter.bracket'
      ]],
      
      // Date literals
      [/DATE\s*\(\s*\d{4}\s*,\s*\d{1,2}\s*,\s*\d{1,2}\s*\)/, 'constant.date'],
      
      // Strings in DAX with escape sequences
      [/"([^"\\]|\\.)*"/, 'string.dax'],
      [/'([^'\\]|\\.)*'/, 'string.dax'],
      
      // Numbers in DAX
      [/\d*\.\d+([eE][\-+]?\d+)?/, 'number.float.dax'],
      [/\d+/, 'number.dax'],
      
      // Boolean constants
      [/\b(TRUE|FALSE)\b/, 'constant.boolean.dax'],
      
      // Comparison and logical operators
      [/(>=|<=|<>|=|>|<)/, 'operator.comparison.dax'],
      [/(\|\||&&|!)/, 'operator.logical.dax'],
      [/[+\-*/]/, 'operator.arithmetic.dax'],
      [/[&]/, 'operator.concatenation.dax'],
      
      // Special DAX values
      [/\bBLANK\s*\(\s*\)/, 'constant.blank.dax'],
      [/\{[^}]*\}/, 'constant.array.dax'],
      
      // Parentheses and brackets in DAX
      [/[\(\)]/, 'delimiter.parenthesis.dax'],
      [/[\[\]]/, 'delimiter.bracket.dax'],
      [/[,;]/, 'delimiter.dax'],
      
      // Comments within DAX
      [/\/\/.*$/, 'copper-comment-dax'],
      [/\/\*/, { token: 'copper-comment-dax', next: '@daxComment' }],
      
      // Identifiers in DAX
      [/[A-Za-z_][A-Za-z0-9_]*/, 'identifier.dax'],
      
      // Default for everything else in DAX
      [/./, 'text.dax'],
    ],
    
    daxComment: [
      [/[^\/*]+/, 'copper-comment-dax'],
      [/\*\//, { token: 'copper-comment-dax', next: '@pop' }],
      [/[\/*]/, 'copper-comment-dax']
    ],

    string: [
      [/[^\\"]+/, 'string'],
      [/@escapes/, 'string.escape'],
      [/\\./, 'string.escape.invalid'],
      [/"/, { token: 'string.quote', bracket: '@close', next: '@pop' }]
    ],
    
    stringSingle: [
      [/[^\\']+/, 'string'],
      [/@escapes/, 'string.escape'],
      [/\\./, 'string.escape.invalid'],
      [/'/, { token: 'string.quote', bracket: '@close', next: '@pop' }]
    ],
  },
}

// Light theme configuration for Copper language
export const copperLightTheme: monaco.editor.IStandaloneThemeData = {
  base: 'vs',
  inherit: true, // Restore inheritance to get basic syntax highlighting back
  rules: [
    // Comments - FORCE subtle gray with custom token names
    { token: 'copper-comment', foreground: '999999', fontStyle: 'italic' },
    { token: 'copper-comment-dax', foreground: '999999', fontStyle: 'italic' },

    // Copper language keywords - very vibrant colors
    { token: 'keyword', foreground: 'FF1493' },
    { token: 'keyword.declaration', foreground: '0000FF', fontStyle: 'bold' },      // Bright blue for model/view/dimension/measure
    { token: 'keyword.property', foreground: 'FF4500', fontStyle: 'bold' },        // Orange-red for type/expression/etc
    { token: 'keyword.join', foreground: '9932CC', fontStyle: 'bold' },
    { token: 'keyword.relationship', foreground: '9932CC', fontStyle: 'bold' },

    // Entity names
    { token: 'entity.name', foreground: '1E90FF', fontStyle: 'bold' },
    { token: 'entity.name.table', foreground: '4169E1', fontStyle: 'bold' },
    { token: 'entity.name.column', foreground: '228B22' },

    // Data types - bright green
    { token: 'type', foreground: '00AA00', fontStyle: 'bold' },

    // Constants and literals
    { token: 'constant.format', foreground: 'DAA520', fontStyle: 'bold' },
    { token: 'constant.boolean', foreground: 'FF0000', fontStyle: 'bold' },        // Bright red for yes/no
    { token: 'constant.boolean.dax', foreground: 'FF0000', fontStyle: 'bold' },
    { token: 'constant.array', foreground: '9932CC' },
    { token: 'constant.array.dax', foreground: '9932CC' },
    { token: 'constant.date', foreground: 'FF4500' },
    { token: 'constant.blank.dax', foreground: '696969', fontStyle: 'italic' },

    // DAX functions by category
    { token: 'support.function.aggregation', foreground: 'FF8C00', fontStyle: 'bold' },
    { token: 'support.function.filter', foreground: 'DC143C', fontStyle: 'bold' },
    { token: 'support.function.relationship', foreground: '32CD32', fontStyle: 'bold' },
    { token: 'support.function.table', foreground: '4682B4', fontStyle: 'bold' },
    { token: 'support.function.iterator', foreground: 'BA55D3', fontStyle: 'bold' },
    { token: 'support.function.logical', foreground: 'C71585', fontStyle: 'bold' },
    { token: 'support.function.math', foreground: '008B8B', fontStyle: 'bold' },
    { token: 'support.function.text', foreground: 'CD853F', fontStyle: 'bold' },
    { token: 'support.function.datetime', foreground: 'FF6347', fontStyle: 'bold' },
    { token: 'support.function.timeintel', foreground: 'DA70D6', fontStyle: 'bold' },
    { token: 'support.function.info', foreground: '708090', fontStyle: 'bold' },

    // DAX keywords
    { token: 'keyword.dax', foreground: '8B008B', fontStyle: 'bold' },

    // Table and column references - bright blue
    { token: 'variable.table-column', foreground: '0066CC', fontStyle: 'bold' },

    // Numbers - bright blue
    { token: 'number', foreground: '0000FF', fontStyle: 'bold' },
    { token: 'number.float', foreground: '0000FF', fontStyle: 'bold' },
    { token: 'number.hex', foreground: '0000FF', fontStyle: 'bold' },
    { token: 'number.dax', foreground: '0000FF', fontStyle: 'bold' },
    { token: 'number.float.dax', foreground: '0000FF', fontStyle: 'bold' },

    // Strings - bright red
    { token: 'string', foreground: 'CC0000', fontStyle: 'bold' },
    { token: 'string.quote', foreground: 'CC0000', fontStyle: 'bold' },
    { token: 'string.format', foreground: 'B8860B', fontStyle: 'italic bold' },
    { token: 'string.dax', foreground: 'CC0000', fontStyle: 'bold' },
    { token: 'string.escape', foreground: 'FF0000' },
    { token: 'string.escape.invalid', foreground: 'FF0000' },
    { token: 'string.invalid', foreground: 'FF0000', fontStyle: 'underline' },

    // Operators
    { token: 'operator', foreground: '000000' },
    { token: 'operator.arithmetic', foreground: '000000' },
    { token: 'operator.comparison.dax', foreground: '000000' },
    { token: 'operator.logical.dax', foreground: '0000FF' },
    { token: 'operator.arithmetic.dax', foreground: '000000' },
    { token: 'operator.concatenation.dax', foreground: '000000' },

    // Delimiters
    { token: 'delimiter', foreground: '000000' },
    { token: 'delimiter.colon', foreground: 'FF8C00', fontStyle: 'bold' },
    { token: 'delimiter.dax.start', foreground: 'FF8C00', fontStyle: 'bold' },
    { token: 'delimiter.dax.end', foreground: 'FF8C00', fontStyle: 'bold' },
    { token: 'delimiter.dax', foreground: '000000' },
    { token: 'delimiter.bracket', foreground: '000000' },
    { token: 'delimiter.bracket.dax', foreground: '000000' },
    { token: 'delimiter.curly', foreground: '000000' },
    { token: 'delimiter.parenthesis', foreground: '000000' },
    { token: 'delimiter.parenthesis.dax', foreground: '000000' },

    // Identifiers
    { token: 'identifier', foreground: '001080' },
    { token: 'identifier.dax', foreground: '001080' },

    // Other
    { token: 'text.dax', foreground: '000000' },
  ],
  colors: {
    'editor.background': '#FFFFFF',
    'editor.foreground': '#000000',
    'editorLineNumber.foreground': '#237893',
    'editorLineNumber.activeForeground': '#0B216F',
    'editorIndentGuide.background': '#D3D3D3',
    'editorIndentGuide.activeBackground': '#939393',
    'editor.selectionBackground': '#ADD6FF',
    'editor.selectionHighlightBackground': '#ADD6FF4D',
    'editor.inactiveSelectionBackground': '#E5EBF1',
    'editorBracketMatch.background': '#0064001a',
    'editorBracketMatch.border': '#B9B9B9',
    'editorCursor.foreground': '#000000',
    'editorWhitespace.foreground': '#BFBFBF',
    'editorError.foreground': '#FF0000',
    'editorWarning.foreground': '#FFA500',
    'editorInfo.foreground': '#1E90FF',
    'editor.findMatchBackground': '#A8AC94',
    'editor.findMatchHighlightBackground': '#EA5C004D',
    'editor.findRangeHighlightBackground': '#B4B4B44D',
    'editorGutter.background': '#F7F7F7',
    'editorGutter.modifiedBackground': '#1E90FF',
    'editorGutter.addedBackground': '#587C0C',
    'editorGutter.deletedBackground': '#AD0707'
  }
}

// Enhanced dark theme configuration for Copper language
export const copperDarkTheme: monaco.editor.IStandaloneThemeData = {
  base: 'vs-dark',
  inherit: true, // Restore inheritance to get basic syntax highlighting back
  rules: [
    // Comments - FORCE subtle gray with custom token names
    { token: 'copper-comment', foreground: 'AAAAAA', fontStyle: 'italic' },
    { token: 'copper-comment-dax', foreground: 'AAAAAA', fontStyle: 'italic' },

    // Copper language keywords - very bright colors
    { token: 'keyword', foreground: 'FF69B4' },
    { token: 'keyword.declaration', foreground: '00BFFF', fontStyle: 'bold' },      // Deep sky blue for model/view/dimension/measure
    { token: 'keyword.property', foreground: 'FF8C00', fontStyle: 'bold' },        // Dark orange for type/expression/etc
    { token: 'keyword.join', foreground: 'FF69B4', fontStyle: 'bold' },
    { token: 'keyword.relationship', foreground: 'DA70D6', fontStyle: 'bold' },

    // Entity names
    { token: 'entity.name', foreground: '4FC1FF', fontStyle: 'bold' },
    { token: 'entity.name.table', foreground: '87CEEB', fontStyle: 'bold' },
    { token: 'entity.name.column', foreground: '98FB98' },

    // Data types - bright cyan
    { token: 'type', foreground: '00FFFF', fontStyle: 'bold' },

    // Constants and literals
    { token: 'constant.format', foreground: 'FFFF00', fontStyle: 'bold' },          // Bright yellow
    { token: 'constant.boolean', foreground: 'FF4500', fontStyle: 'bold' },        // Orange-red for yes/no
    { token: 'constant.boolean.dax', foreground: 'FF4500', fontStyle: 'bold' },
    { token: 'constant.array', foreground: 'DDA0DD' },
    { token: 'constant.array.dax', foreground: 'DDA0DD' },
    { token: 'constant.date', foreground: 'FFA07A' },
    { token: 'constant.blank.dax', foreground: '708090', fontStyle: 'italic' },

    // DAX functions by category
    { token: 'support.function.aggregation', foreground: 'FFD700', fontStyle: 'bold' },
    { token: 'support.function.filter', foreground: 'FF6347', fontStyle: 'bold' },
    { token: 'support.function.relationship', foreground: '32CD32', fontStyle: 'bold' },
    { token: 'support.function.table', foreground: '87CEFA', fontStyle: 'bold' },
    { token: 'support.function.iterator', foreground: 'DDA0DD', fontStyle: 'bold' },
    { token: 'support.function.logical', foreground: 'FF69B4', fontStyle: 'bold' },
    { token: 'support.function.math', foreground: '20B2AA', fontStyle: 'bold' },
    { token: 'support.function.text', foreground: 'F4A460', fontStyle: 'bold' },
    { token: 'support.function.datetime', foreground: 'FFA500', fontStyle: 'bold' },
    { token: 'support.function.timeintel', foreground: 'FFB6C1', fontStyle: 'bold' },
    { token: 'support.function.info', foreground: 'B0C4DE', fontStyle: 'bold' },

    // DAX keywords
    { token: 'keyword.dax', foreground: 'DA70D6', fontStyle: 'bold' },

    // Table and column references - bright light blue
    { token: 'variable.table-column', foreground: '87CEFA', fontStyle: 'bold' },

    // Numbers - bright light green
    { token: 'number', foreground: '90EE90', fontStyle: 'bold' },
    { token: 'number.float', foreground: '90EE90', fontStyle: 'bold' },
    { token: 'number.hex', foreground: '90EE90', fontStyle: 'bold' },
    { token: 'number.dax', foreground: '90EE90', fontStyle: 'bold' },
    { token: 'number.float.dax', foreground: '90EE90', fontStyle: 'bold' },

    // Strings - bright salmon
    { token: 'string', foreground: 'FFA07A', fontStyle: 'bold' },
    { token: 'string.quote', foreground: 'FFA07A', fontStyle: 'bold' },
    { token: 'string.format', foreground: 'FFFF00', fontStyle: 'italic bold' },
    { token: 'string.dax', foreground: 'FFA07A', fontStyle: 'bold' },
    { token: 'string.escape', foreground: 'D7BA7D' },
    { token: 'string.escape.invalid', foreground: 'F44747' },
    { token: 'string.invalid', foreground: 'F44747', fontStyle: 'underline' },

    // Operators
    { token: 'operator', foreground: 'D4D4D4' },
    { token: 'operator.arithmetic', foreground: 'D4D4D4' },
    { token: 'operator.comparison.dax', foreground: 'D4D4D4' },
    { token: 'operator.logical.dax', foreground: 'C586C0' },
    { token: 'operator.arithmetic.dax', foreground: 'D4D4D4' },
    { token: 'operator.concatenation.dax', foreground: 'D4D4D4' },

    // Delimiters
    { token: 'delimiter', foreground: 'D4D4D4' },
    { token: 'delimiter.colon', foreground: 'FFD700', fontStyle: 'bold' },
    { token: 'delimiter.dax.start', foreground: 'FFD700', fontStyle: 'bold' },
    { token: 'delimiter.dax.end', foreground: 'FFD700', fontStyle: 'bold' },
    { token: 'delimiter.dax', foreground: 'D4D4D4' },
    { token: 'delimiter.bracket', foreground: 'D4D4D4' },
    { token: 'delimiter.bracket.dax', foreground: 'D4D4D4' },
    { token: 'delimiter.curly', foreground: 'D4D4D4' },
    { token: 'delimiter.parenthesis', foreground: 'D4D4D4' },
    { token: 'delimiter.parenthesis.dax', foreground: 'D4D4D4' },

    // Identifiers
    { token: 'identifier', foreground: '9CDCFE' },
    { token: 'identifier.dax', foreground: '9CDCFE' },

    // Other
    { token: 'text.dax', foreground: 'D4D4D4' },
  ],
  colors: {
    'editor.background': '#1e1e1e',
    'editor.foreground': '#d4d4d4',
    'editorLineNumber.foreground': '#858585',
    'editorIndentGuide.background': '#404040',
    'editorIndentGuide.activeBackground': '#707070',
    'editor.selectionBackground': '#264f78',
    'editor.selectionHighlightBackground': '#ADD6FF26',
    'editorBracketMatch.background': '#0064001a',
    'editorBracketMatch.border': '#888888',
  }
}

// Autocomplete and IntelliSense data
const copperKeywords = [
  // Block types
  'model', 'view', 'dimension', 'measure', 'join', 'parameter',
  // Properties
  'type', 'expression', 'label', 'description', 'value_format',
  'primary_key', 'hidden', 'tiers', 'sql_latitude', 'sql_longitude',
  'units', 'relationship', 'from', 'extends', 'extension', 'required'
]

const copperDataTypes = [
  'string', 'number', 'count', 'count_distinct', 'sum', 'average',
  'median', 'min', 'max', 'date', 'date_time', 'duration', 'yesno',
  'tier', 'location', 'zipcode', 'distance', 'time'
]

const copperValueFormats = [
  'usd', 'eur', 'gbp', 'jpy', 'cad', 'aud', 'chf', 'cny',
  'percent', 'percent_0', 'percent_1', 'percent_2', 'percent_3', 'percent_4',
  'decimal_0', 'decimal_1', 'decimal_2', 'decimal_3', 'decimal_4',
  'id', 'email', 'url', 'phone', 'miles', 'kilometers', 'scientific'
]

const daxFunctions = [
  // Most commonly used DAX functions with descriptions
  { name: 'SUM', detail: 'SUM(column)', documentation: 'Adds all the numbers in a column.' },
  { name: 'COUNT', detail: 'COUNT(column)', documentation: 'Counts the number of non-empty cells in a column.' },
  { name: 'COUNTROWS', detail: 'COUNTROWS(table)', documentation: 'Counts the number of rows in the specified table.' },
  { name: 'AVERAGE', detail: 'AVERAGE(column)', documentation: 'Returns the average (arithmetic mean) of all the numbers in a column.' },
  { name: 'MIN', detail: 'MIN(column)', documentation: 'Returns the smallest value in a column.' },
  { name: 'MAX', detail: 'MAX(column)', documentation: 'Returns the largest value in a column.' },
  { name: 'CALCULATE', detail: 'CALCULATE(expression, filter1, filter2, ...)', documentation: 'Evaluates an expression in a modified filter context.' },
  { name: 'FILTER', detail: 'FILTER(table, filter)', documentation: 'Returns a table that represents a subset of another table or expression.' },
  { name: 'RELATED', detail: 'RELATED(column)', documentation: 'Returns a related value from another table.' },
  { name: 'VALUES', detail: 'VALUES(column)', documentation: 'Returns a one-column table that contains the distinct values from the specified column.' },
  { name: 'DISTINCT', detail: 'DISTINCT(column)', documentation: 'Returns a one-column table that contains the distinct values from the specified column.' },
  { name: 'DISTINCTCOUNT', detail: 'DISTINCTCOUNT(column)', documentation: 'Counts the number of distinct values in a column.' },
  { name: 'IF', detail: 'IF(logical_test, value_if_true, value_if_false)', documentation: 'Checks whether a condition is met, and returns one value if TRUE, and another value if FALSE.' },
  { name: 'SWITCH', detail: 'SWITCH(expression, value1, result1, value2, result2, ...)', documentation: 'Evaluates an expression against a list of values and returns one of multiple possible result expressions.' },
  { name: 'DATE', detail: 'DATE(year, month, day)', documentation: 'Returns the specified date in datetime format.' },
  { name: 'YEAR', detail: 'YEAR(date)', documentation: 'Returns the year of a date as a four digit integer.' },
  { name: 'MONTH', detail: 'MONTH(date)', documentation: 'Returns the month as a number from 1 (January) to 12 (December).' },
  { name: 'DAY', detail: 'DAY(date)', documentation: 'Returns the day of the month, a number from 1 to 31.' },
  { name: 'WEEKDAY', detail: 'WEEKDAY(date, return_type)', documentation: 'Returns a number from 1 to 7 identifying the day of the week of a date.' },
  { name: 'DATEADD', detail: 'DATEADD(dates, number_of_intervals, interval)', documentation: 'Returns a table that contains a column of dates, shifted either forward or backward in time.' },
  { name: 'SAMEPERIODLASTYEAR', detail: 'SAMEPERIODLASTYEAR(dates)', documentation: 'Returns a table that contains a column of dates shifted one year back in time.' },
  { name: 'TOTALYTD', detail: 'TOTALYTD(expression, dates, filter)', documentation: 'Evaluates the year-to-date value of the expression in the current context.' }
]

// Completion item provider
const completionProvider: monaco.languages.CompletionItemProvider = {
  provideCompletionItems: (model, position) => {
    const word = model.getWordUntilPosition(position)
    const range = {
      startLineNumber: position.lineNumber,
      endLineNumber: position.lineNumber,
      startColumn: word.startColumn,
      endColumn: word.endColumn
    }

    const line = model.getLineContent(position.lineNumber)
    const beforeCursor = line.substring(0, position.column - 1)
    
    const suggestions: monaco.languages.CompletionItem[] = []

    // Check if we're in a DAX expression (after a colon)
    const inDAXExpression = /:\s*[^;]*$/.test(beforeCursor) && !beforeCursor.includes(';;')
    
    if (inDAXExpression) {
      // Provide DAX function suggestions
      daxFunctions.forEach(func => {
        suggestions.push({
          label: func.name,
          kind: monaco.languages.CompletionItemKind.Function,
          detail: func.detail,
          documentation: func.documentation,
          insertText: func.name + '(',
          range: range
        })
      })
    } else {
      // Check context for better suggestions
      const isAfterColon = /:\s*$/.test(beforeCursor)
      const isInTypeContext = /type\s*:\s*$/.test(beforeCursor)
      const isInValueFormatContext = /value_format\s*:\s*$/.test(beforeCursor)
      
      if (isInTypeContext) {
        // Suggest data types
        copperDataTypes.forEach(type => {
          suggestions.push({
            label: type,
            kind: monaco.languages.CompletionItemKind.TypeParameter,
            detail: `Data type: ${type}`,
            insertText: type,
            range: range
          })
        })
      } else if (isInValueFormatContext) {
        // Suggest value formats
        copperValueFormats.forEach(format => {
          suggestions.push({
            label: format,
            kind: monaco.languages.CompletionItemKind.Constant,
            detail: `Value format: ${format}`,
            insertText: format,
            range: range
          })
        })
      } else if (!isAfterColon) {
        // Suggest Copper keywords
        copperKeywords.forEach(keyword => {
          const insertText = ['model', 'view', 'dimension', 'measure', 'join', 'parameter'].includes(keyword) 
            ? `${keyword}: \${1:name} {\n\t$0\n}`
            : keyword + ': '
          
          suggestions.push({
            label: keyword,
            kind: monaco.languages.CompletionItemKind.Keyword,
            detail: `Copper keyword: ${keyword}`,
            insertText: insertText,
            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            range: range
          })
        })
      }

      // Always provide boolean values
      if (isAfterColon) {
        ['yes', 'no', 'true', 'false'].forEach(bool => {
          suggestions.push({
            label: bool,
            kind: monaco.languages.CompletionItemKind.Constant,
            detail: `Boolean value: ${bool}`,
            insertText: bool,
            range: range
          })
        })
      }
    }

    return { suggestions }
  }
}

// Hover provider
const hoverProvider: monaco.languages.HoverProvider = {
  provideHover: (model, position) => {
    const word = model.getWordAtPosition(position)
    if (!word) return null

    const wordText = word.word.toUpperCase()
    
    // Find DAX function documentation
    const daxFunc = daxFunctions.find(f => f.name === wordText)
    if (daxFunc) {
      return {
        range: new monaco.Range(position.lineNumber, word.startColumn, position.lineNumber, word.endColumn),
        contents: [
          { value: `**${daxFunc.name}**` },
          { value: daxFunc.detail },
          { value: daxFunc.documentation }
        ]
      }
    }

    // Provide basic information for Copper keywords
    if (copperKeywords.includes(word.word)) {
      const descriptions: Record<string, string> = {
        'model': 'Defines a data model with dimensions and measures',
        'view': 'Defines a view that can join multiple models',
        'dimension': 'Defines a dimension (attribute) in a model',
        'measure': 'Defines a measure (calculation) in a model',
        'join': 'Defines how to join tables in a view',
        'type': 'Specifies the data type of a dimension or measure',
        'expression': 'Defines the DAX expression for the field',
        'label': 'Human-readable label for the field',
        'description': 'Detailed description of the field',
        'value_format': 'Formatting template for displaying values'
      }

      const description = descriptions[word.word] || `Copper keyword: ${word.word}`
      
      return {
        range: new monaco.Range(position.lineNumber, word.startColumn, position.lineNumber, word.endColumn),
        contents: [
          { value: `**${word.word}**` },
          { value: description }
        ]
      }
    }

    return null
  }
}

// Register the Copper language with Monaco
export function registerCopperLanguage() {
  console.log('Registering Copper language...')
  
  try {
    // Use a unique language ID to avoid caching issues
    const languageId = 'copper-lang-' + Date.now()
    
    // Register the language with unique ID
    monaco.languages.register({ 
      id: languageId,
      extensions: ['.copper'],
      aliases: ['Copper', 'copper'],
      mimetypes: ['text/copper']
    })
    
    // Also register with static 'copper' ID
    try {
      monaco.languages.register({ 
        id: 'copper',
        extensions: ['.copper'],
        aliases: ['Copper', 'copper'],
        mimetypes: ['text/copper']
      })
    } catch(e) {
      console.log('Static copper registration failed (expected if already registered)')
    }
    console.log('Copper language registration called')
    
    // Immediately verify registration
    const verifyLanguages = monaco.languages.getLanguages()
    const isNowRegistered = verifyLanguages.some(lang => lang.id === 'copper')
    console.log('Registration verification:', isNowRegistered)
    
    if (!isNowRegistered) {
      console.error('❌ Language registration failed - copper not found in languages list')
      return false
    } else {
      console.log('✅ Language registration successful')
    }
    
  } catch (error) {
    console.error('Error registering Copper language:', error)
    return false
  }

  // Set language configuration
  monaco.languages.setLanguageConfiguration('copper', {
    comments: {
      lineComment: '#',
    },
    brackets: [
      ['{', '}'],
      ['[', ']'],
      ['(', ')']
    ],
    autoClosingPairs: [
      { open: '{', close: '}' },
      { open: '[', close: ']' },
      { open: '(', close: ')' },
      { open: '"', close: '"' },
    ],
    surroundingPairs: [
      { open: '{', close: '}' },
      { open: '[', close: ']' },
      { open: '(', close: ')' },
      { open: '"', close: '"' },
    ],
    indentationRules: {
      increaseIndentPattern: /^.*\{[^}]*$/,
      decreaseIndentPattern: /^((?!.*?\/\*).*\s*)?\}.*$/
    },
    folding: {
      markers: {
        start: /^\s*\/\*\s*#region\b/,
        end: /^\s*\*\/\s*#endregion\b/
      }
    }
  })

  // Set monarch tokenizer
  try {
    monaco.languages.setMonarchTokensProvider('copper', copperLanguageDefinition)
    console.log('Monarch tokenizer set for Copper')
  } catch (error) {
    console.error('Error setting Monarch tokenizer:', error)
  }

  // Define themes
  try {
    console.log('Defining Copper themes...')
    monaco.editor.defineTheme('copper-light', copperLightTheme)
    monaco.editor.defineTheme('copper-dark', copperDarkTheme)
    console.log('Copper themes defined: copper-light, copper-dark')
    
    // Also set the tokenizer for plaintext to use our copper tokenizer
    // This is a fallback in case the language setting doesn't work
    monaco.languages.setMonarchTokensProvider('plaintext', copperLanguageDefinition)
    console.log('Applied Copper tokenizer to plaintext as fallback')
  } catch (error) {
    console.error('Error defining themes:', error)
  }

  // Register completion provider
  monaco.languages.registerCompletionItemProvider('copper', completionProvider)

  // Register hover provider
  monaco.languages.registerHoverProvider('copper', hoverProvider)

  // Register folding range provider
  monaco.languages.registerFoldingRangeProvider('copper', {
    provideFoldingRanges: (model) => {
      const ranges: monaco.languages.FoldingRange[] = []
      const lines = model.getLinesContent()
      
      let blockStack: Array<{ startLine: number, type: string }> = []
      
      for (let i = 0; i < lines.length; i++) {
        const line = lines[i].trim()
        
        // Start of a block (model, view, dimension, measure, join)
        const blockMatch = line.match(/^(model|view|dimension|measure|join|parameter):\s*\w+\s*\{?/)
        if (blockMatch) {
          blockStack.push({ startLine: i, type: blockMatch[1] })
        }
        
        // Opening brace on its own line
        if (line === '{' && blockStack.length > 0) {
          // Update the last block's start line if needed
          const lastBlock = blockStack[blockStack.length - 1]
          if (lastBlock.startLine === i - 1) {
            // The opening brace is on the line after the declaration
            // Keep the same start line
          }
        }
        
        // Closing brace
        if (line === '}' || line.endsWith('}')) {
          if (blockStack.length > 0) {
            const block = blockStack.pop()!
            if (i > block.startLine) {
              ranges.push({
                start: block.startLine + 1,
                end: i,
                kind: monaco.languages.FoldingRangeKind.Region
              })
            }
          }
        }
        
        // Multi-line DAX expressions
        if (line.includes(':') && !line.includes(';;')) {
          // This might be the start of a multi-line DAX expression
          let endLine = i
          for (let j = i + 1; j < lines.length; j++) {
            if (lines[j].includes(';;')) {
              endLine = j
              break
            }
          }
          
          if (endLine > i + 1) {
            ranges.push({
              start: i + 1,
              end: endLine,
              kind: monaco.languages.FoldingRangeKind.Comment
            })
          }
        }
        
        // Comment blocks
        if (line.startsWith('#')) {
          let endLine = i
          for (let j = i + 1; j < lines.length; j++) {
            if (!lines[j].trim().startsWith('#') && lines[j].trim() !== '') {
              break
            }
            if (lines[j].trim().startsWith('#')) {
              endLine = j
            }
          }
          
          if (endLine > i + 1) {
            ranges.push({
              start: i + 1,
              end: endLine,
              kind: monaco.languages.FoldingRangeKind.Comment
            })
            i = endLine // Skip ahead
          }
        }
      }
      
      return ranges
    }
  })

  console.log('Copper language registration completed successfully')
  return true
}