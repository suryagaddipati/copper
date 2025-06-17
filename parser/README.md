# Copper Parser

A Python parser for the Copper metadata format, implementing the complete EBNF grammar specification.

## Features

- **Complete Grammar Support**: Implements the full Copper EBNF specification
- **DAX Expression Handling**: Treats DAX expressions as opaque strings (blackbox approach)
- **Comprehensive AST**: Builds a complete Abstract Syntax Tree
- **Error Handling**: Detailed error messages with line/column information
- **Context-Sensitive Tokenization**: Handles keywords used as identifiers correctly
- **Extensive Testing**: Full test suite with 23+ test cases

## Architecture

```
parser/
├── __init__.py           # Package initialization
├── tokenizer.py          # Lexical analysis (string → tokens)
├── ast_nodes.py          # AST node definitions
├── parser.py             # Syntax analysis (tokens → AST)
├── copper_parser.py      # Main parser interface
└── test_parser.py        # Comprehensive test suite
```

## Usage

### Python API

```python
from parser.copper_parser import parse_file, parse_string

# Parse a file
result = parse_file("model.copper")
if result.success:
    ast = result.ast
    print(f"Parsed {len(ast.statements)} statements")
else:
    print(f"Parse error: {result.error}")

# Parse a string
result = parse_string('''
model: orders {
    dimension: order_id {
        type: string
        expression: Orders[OrderID] ;;
        primary_key: yes
    }
}
''')
```

### Command Line Interface

```bash
# Validate files
python3 copper_parse.py validate examples/*.copper

# Parse and show AST
python3 copper_parse.py parse examples/orders.copper

# Parse and output JSON
python3 copper_parse.py parse examples/orders.copper --format json
```

## Supported Constructs

### Models
- Dimensions with all types (string, number, date, etc.)
- Measures with all types (count, sum, average, etc.)
- All parameters (primary_key, value_format, label, etc.)
- Tiers (both string and numeric)
- Geographic fields (sql_latitude, sql_longitude, units)

### Views
- From clauses
- Join definitions with types and relationships
- View inheritance (extends)
- Extension templates

### DAX Expressions
- Complete DAX expression parsing as opaque strings
- Multi-line expression support
- Proper handling in expression, sql_latitude, sql_longitude

## Testing

Run the comprehensive test suite:

```bash
# Run all tests
python3 parser/test_parser.py

# Validate example files
python3 parser/test_parser.py --validate-examples

# Test specific file
python3 parser/test_parser.py --file examples/orders.copper
```

## Implementation Details

### Tokenization
- Context-sensitive keyword handling
- Structural keywords vs. type keywords
- Special DAX expression tokenization
- Proper handling of keywords as identifiers

### Parsing
- Recursive descent parser
- Comprehensive error recovery
- Position tracking for debugging
- AST node creation with metadata

### Error Handling
- Detailed error messages with position
- Graceful handling of malformed input
- Clear distinction between tokenization and parsing errors

## Validation Results

All example files parse successfully:
- ✓ base_ecommerce_view.copper (6 views)
- ✓ ecommerce_orders.copper (1 model)
- ✓ customers.copper (1 model)
- ✓ products.copper (1 model)
- ✓ sales_analysis_view.copper (1 view)

## Future Enhancements

- Full DAX expression parsing (currently blackbox)
- Semantic validation beyond syntax
- Code generation capabilities
- Integration with other tools