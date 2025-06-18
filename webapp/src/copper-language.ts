import * as monaco from 'monaco-editor'

// Copper language syntax highlighting configuration
export const copperLanguageDefinition: monaco.languages.IMonarchLanguage = {
  // Set defaultToken to invalid to see what you do not tokenize yet
  defaultToken: 'invalid',
  
  // Keywords for the Copper language
  keywords: [
    'model', 'view', 'dimension', 'measure', 'join', 'parameter',
    'type', 'expression', 'label', 'description', 'value_format',
    'primary_key', 'hidden', 'tiers', 'sql_latitude', 'sql_longitude',
    'units', 'relationship', 'from', 'extends', 'extension'
  ],

  // Data types
  typeKeywords: [
    'string', 'number', 'count', 'count_distinct', 'sum', 'average',
    'median', 'min', 'max', 'date', 'date_time', 'duration', 'yesno',
    'tier', 'location', 'zipcode', 'distance'
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
    'usd', 'eur', 'gbp', 'percent', 'percent_0', 'percent_1', 'percent_2',
    'decimal_0', 'decimal_1', 'decimal_2', 'decimal_3', 'decimal_4',
    'id', 'email', 'url', 'phone', 'miles', 'kilometers'
  ],

  // Boolean values
  booleans: ['yes', 'no', 'true', 'false'],

  // DAX functions (common ones)
  daxFunctions: [
    'SUM', 'COUNT', 'COUNTROWS', 'AVERAGE', 'MIN', 'MAX', 'DIVIDE',
    'CALCULATE', 'FILTER', 'RELATED', 'RELATEDTABLE', 'VALUES',
    'DISTINCT', 'DISTINCTCOUNT', 'SUMX', 'AVERAGEX', 'MAXX', 'MINX',
    'IF', 'SWITCH', 'AND', 'OR', 'NOT', 'BLANK', 'ISBLANK',
    'DATE', 'DATEADD', 'DATEDIFF', 'YEAR', 'MONTH', 'DAY',
    'WEEKDAY', 'WEEKNUM', 'TODAY', 'NOW', 'EOMONTH',
    'SAMEPERIODLASTYEAR', 'PARALLELPERIOD', 'DATESBETWEEN',
    'TOTALYTD', 'TOTALMTD', 'TOTALQTD'
  ],

  // The main tokenizer for our languages
  tokenizer: {
    root: [
      // Comments
      [/#.*$/, 'comment'],

      // Model/View/Dimension/Measure declarations
      [/\b(model|view|dimension|measure|join|parameter)\s*:/, 'keyword.declaration'],

      // Keywords
      [/\b(?:type|expression|label|description|value_format|primary_key|hidden|tiers|sql_latitude|sql_longitude|units|relationship|from|extends|extension)\b/, 'keyword'],

      // Data types
      [/\b(?:string|number|count|count_distinct|sum|average|median|min|max|date|date_time|duration|yesno|tier|location|zipcode|distance)\b/, 'type'],

      // Join types
      [/\b(?:inner|left_outer|right_outer|full_outer|cross)\b/, 'keyword.join'],

      // Relationship types
      [/\b(?:one_to_one|one_to_many|many_to_one|many_to_many)\b/, 'keyword.relationship'],

      // Value formats
      [/\b(?:usd|eur|gbp|percent|percent_0|percent_1|percent_2|decimal_0|decimal_1|decimal_2|decimal_3|decimal_4|id|email|url|phone|miles|kilometers)\b/, 'constant.format'],

      // Boolean values
      [/\b(?:yes|no|true|false)\b/, 'constant.boolean'],

      // DAX functions
      [/\b(?:SUM|COUNT|COUNTROWS|AVERAGE|MIN|MAX|DIVIDE|CALCULATE|FILTER|RELATED|RELATEDTABLE|VALUES|DISTINCT|DISTINCTCOUNT|SUMX|AVERAGEX|MAXX|MINX|IF|SWITCH|AND|OR|NOT|BLANK|ISBLANK|DATE|DATEADD|DATEDIFF|YEAR|MONTH|DAY|WEEKDAY|WEEKNUM|TODAY|NOW|EOMONTH|SAMEPERIODLASTYEAR|PARALLELPERIOD|DATESBETWEEN|TOTALYTD|TOTALMTD|TOTALQTD)\b/, 'support.function.dax'],

      // DAX expressions (between colons and double semicolons)
      [/:/, { token: 'delimiter.dax', next: '@daxExpression' }],

      // Strings
      [/"([^"\\]|\\.)*$/, 'string.invalid'],  // non-teminated string
      [/"/, { token: 'string.quote', bracket: '@open', next: '@string' }],

      // Numbers
      [/\d*\.\d+([eE][\-+]?\d+)?/, 'number.float'],
      [/\d+/, 'number'],

      // Identifiers and arrays
      [/[a-z_$][\w$]*/, 'identifier'],
      [/[A-Z][\w\$]*/, 'type.identifier'],  // to show class names nicely

      // Brackets
      [/\[/, { token: 'delimiter.bracket', bracket: '@open' }],
      [/\]/, { token: 'delimiter.bracket', bracket: '@close' }],
      [/\{/, { token: 'delimiter.curly', bracket: '@open' }],
      [/\}/, { token: 'delimiter.curly', bracket: '@close' }],
      [/\(/, { token: 'delimiter.parenthesis', bracket: '@open' }],
      [/\)/, { token: 'delimiter.parenthesis', bracket: '@close' }],

      // Operators
      [/[=<>!]+/, 'operator'],
      [/[,;]/, 'delimiter'],
    ],

    daxExpression: [
      // End DAX expression with double semicolon
      [/;;/, { token: 'delimiter.dax', next: '@pop' }],
      
      // DAX functions within expression
      [/\b(?:SUM|COUNT|COUNTROWS|AVERAGE|MIN|MAX|DIVIDE|CALCULATE|FILTER|RELATED|RELATEDTABLE|VALUES|DISTINCT|DISTINCTCOUNT|SUMX|AVERAGEX|MAXX|MINX|IF|SWITCH|AND|OR|NOT|BLANK|ISBLANK|DATE|DATEADD|DATEDIFF|YEAR|MONTH|DAY|WEEKDAY|WEEKNUM|TODAY|NOW|EOMONTH|SAMEPERIODLASTYEAR|PARALLELPERIOD|DATESBETWEEN|TOTALYTD|TOTALMTD|TOTALQTD)\b/, 'support.function.dax'],
      
      // DAX keywords
      [/\b(?:VAR|RETURN|IF|THEN|ELSE|TRUE|FALSE)\b/, 'keyword.dax'],
      
      // Table and column references
      [/[A-Za-z_][A-Za-z0-9_]*\[[A-Za-z_][A-Za-z0-9_]*\]/, 'variable.table-column'],
      
      // Numbers in DAX
      [/\d*\.\d+([eE][\-+]?\d+)?/, 'number.float.dax'],
      [/\d+/, 'number.dax'],
      
      // Strings in DAX
      [/"([^"\\]|\\.)*"/, 'string.dax'],
      
      // Operators in DAX
      [/[=<>!&|+\-*/]+/, 'operator.dax'],
      
      // Parentheses and brackets in DAX
      [/[\(\)\[\],]/, 'delimiter.dax'],
      
      // Default for everything else in DAX
      [/[^\s;;]+/, 'variable.dax'],
      
      // Whitespace
      [/\s+/, 'white'],
    ],

    string: [
      [/[^\\"]+/, 'string'],
      [/\\./, 'string.escape.invalid'],
      [/"/, { token: 'string.quote', bracket: '@close', next: '@pop' }]
    ],
  },
}

// Theme configuration for Copper language
export const copperTheme: monaco.editor.IStandaloneThemeData = {
  base: 'vs-dark',
  inherit: true,
  rules: [
    { token: 'comment', foreground: '6A9955' },
    { token: 'keyword', foreground: 'C586C0' },
    { token: 'keyword.declaration', foreground: '569CD6', fontStyle: 'bold' },
    { token: 'keyword.join', foreground: 'DCDCAA' },
    { token: 'keyword.relationship', foreground: 'DCDCAA' },
    { token: 'type', foreground: '4EC9B0' },
    { token: 'constant.format', foreground: 'B5CEA8' },
    { token: 'constant.boolean', foreground: '569CD6' },
    { token: 'support.function.dax', foreground: 'DCDCAA', fontStyle: 'bold' },
    { token: 'keyword.dax', foreground: 'C586C0' },
    { token: 'variable.table-column', foreground: '9CDCFE' },
    { token: 'variable.dax', foreground: 'D4D4D4' },
    { token: 'number.dax', foreground: 'B5CEA8' },
    { token: 'string.dax', foreground: 'CE9178' },
    { token: 'operator.dax', foreground: 'D4D4D4' },
    { token: 'delimiter.dax', foreground: 'FFD700', fontStyle: 'bold' },
    { token: 'string', foreground: 'CE9178' },
    { token: 'number', foreground: 'B5CEA8' },
    { token: 'operator', foreground: 'D4D4D4' },
    { token: 'delimiter', foreground: 'D4D4D4' },
    { token: 'identifier', foreground: '9CDCFE' },
  ],
  colors: {}
}

// Register the Copper language with Monaco
export function registerCopperLanguage() {
  // Register language
  monaco.languages.register({ id: 'copper' })

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
    }
  })

  // Set monarch tokenizer
  monaco.languages.setMonarchTokensProvider('copper', copperLanguageDefinition)

  // Define theme
  monaco.editor.defineTheme('copper-dark', copperTheme)
}