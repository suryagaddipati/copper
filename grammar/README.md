# Copper ANTLR Grammar

ANTLR4 grammar implementation for the Copper metadata language, enabling automatic parser generation for multiple programming languages.

## Overview

This directory contains the ANTLR4 grammar files and build system for generating Copper language parsers in various programming languages. The grammar is converted from the original EBNF specification and supports the complete Copper language syntax.

## Features

- **Complete Language Support**: Full Copper syntax including models, views, dimensions, measures
- **Multi-Language Generation**: Automatic parser generation for 8+ programming languages
- **DAX Expression Support**: Handles DAX expressions as blackbox strings with lexer modes
- **Context-Sensitive Parsing**: Proper handling of keywords used as identifiers
- **Build Automation**: Comprehensive build scripts for all target languages

## Supported Languages

| Language | ANTLR Target | Status | Generated Files |
|----------|--------------|--------|-----------------|
| Java | Java | ✅ | `*.java` |
| Python | Python3 | ✅ | `*.py` |
| JavaScript | JavaScript | ✅ | `*.js` |
| TypeScript | TypeScript | ✅ | `*.ts` |
| C# | CSharp | ✅ | `*.cs` |
| Go | Go | ✅ | `*.go` |
| C++ | Cpp | ✅ | `*.cpp`, `*.h` |
| Swift | Swift | ✅ | `*.swift` |

## Directory Structure

```
grammar/
├── Copper.g4             # Main Copper grammar
├── DAX.g4                # DAX lexer grammar (comprehensive)
├── build/                # Generated parsers (created during build)
│   ├── java/
│   ├── python/
│   ├── javascript/
│   └── ...
├── build.gradle          # Gradle build script (Java)
├── setup.py             # Python setuptools script
├── build.sh             # Universal build script
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Quick Start

### Prerequisites

1. **ANTLR4**: Install ANTLR4 command-line tool
   ```bash
   # macOS
   brew install antlr
   
   # Ubuntu/Debian
   apt-get install antlr4
   
   # Manual installation
   # Download from: https://www.antlr.org/download.html
   ```

2. **Language-Specific Tools**:
   - **Java**: JDK 11+ and Gradle
   - **Python**: Python 3.7+ and pip
   - **JavaScript/TypeScript**: Node.js 16+
   - **C#**: .NET SDK 6.0+
   - **Go**: Go 1.18+
   - **C++**: GCC 9+ or Clang 10+

### Generate All Parsers

```bash
# Navigate to grammar directory
cd grammar

# Generate parsers for all languages
./build.sh generate

# Or generate specific languages
./build.sh generate java python javascript
```

### Generate Java Parser (Gradle)

```bash
cd grammar
gradle generateGrammarSource
gradle build
```

### Generate Python Parser

```bash
cd grammar
python setup.py build_py
pip install -e .
```

## Grammar Features

### Main Language Constructs

The ANTLR grammar supports all Copper language features:

```antlr
// Models with dimensions and measures
modelStatement
    : MODEL COLON identifier LBRACE modelBody* RBRACE

// Views with joins and inheritance  
viewStatement
    : VIEW COLON identifier LBRACE viewBody* RBRACE

// Context-sensitive keyword handling
identifier
    : IDENTIFIER
    | contextualKeyword
```

### DAX Expression Handling

DAX expressions are handled using lexer modes for blackbox parsing:

```antlr
// Trigger DAX mode on these keywords
EXPRESSION      : 'expression' -> pushMode(DAX_MODE);
SQL_LATITUDE    : 'sql_latitude' -> pushMode(DAX_MODE);
SQL_LONGITUDE   : 'sql_longitude' -> pushMode(DAX_MODE);

// DAX mode captures everything until ';;'
mode DAX_MODE;
DAX_STRING      : ':' WS_DAX* (~[;] | ';' ~[;])+ -> popMode;
```

### Context-Sensitive Keywords

Handles keywords used as identifiers:

```antlr
contextualKeyword
    : STRING_TYPE | NUMBER_TYPE | ZIPCODE_TYPE
    | COUNT_TYPE | SUM_TYPE | AVERAGE_TYPE
    | LEFT_OUTER | INNER | MANY_TO_ONE
    | USD | EUR | MILES | KILOMETERS
    // ... etc
```

## Usage Examples

### Java

```java
import com.copper.parser.*;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;

// Parse Copper file
ANTLRInputStream input = new ANTLRInputStream(new FileInputStream("model.copper"));
CopperLexer lexer = new CopperLexer(input);
CommonTokenStream tokens = new CommonTokenStream(lexer);
CopperParser parser = new CopperParser(tokens);

ParseTree tree = parser.program();
System.out.println(tree.toStringTree(parser));
```

### Python

```python
from antlr4 import *
from CopperLexer import CopperLexer
from CopperParser import CopperParser

# Parse Copper file
input_stream = FileStream('model.copper')
lexer = CopperLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = CopperParser(stream)

tree = parser.program()
print(tree.toStringTree(recog=parser))
```

### JavaScript

```javascript
const antlr4 = require('antlr4');
const { CopperLexer } = require('./CopperLexer');
const { CopperParser } = require('./CopperParser');

// Parse Copper code
const input = "model: orders { dimension: id { type: string ... } }";
const chars = new antlr4.InputStream(input);
const lexer = new CopperLexer(chars);
const tokens = new antlr4.CommonTokenStream(lexer);
const parser = new CopperParser(tokens);

const tree = parser.program();
console.log(tree.toStringTree());
```

## Testing

### Validate Grammar

```bash
# Test against example files
./build.sh test

# Test specific file
java -cp "build/java/*" org.antlr.v4.gui.TestRig \
  com.copper.parser.Copper program -gui examples/orders.copper
```

### Python Testing

```bash
cd build/python
python copper_parser_main.py ../../examples/orders.copper --tree
```

### JavaScript Testing

```bash
cd build/javascript
node copper-parser.js ../../examples/orders.copper
```

## Build Scripts

### Universal Build Script (`build.sh`)

The main build script supports multiple commands:

```bash
# Generate all parsers
./build.sh generate

# Generate specific languages
./build.sh generate java python javascript

# Clean build directory
./build.sh clean

# Test parsers
./build.sh test

# Show help
./build.sh help
```

### Gradle Build (`build.gradle`)

For Java development:

```bash
# Generate Java parser
gradle generateGrammarSource

# Generate all language parsers
gradle generateAllParsers

# Run tests
gradle test

# Build JAR
gradle jar
```

### Python Setup (`setup.py`)

For Python distribution:

```bash
# Generate and install
python setup.py build_py
pip install -e .

# Create distribution
python setup.py sdist bdist_wheel
```

## Grammar Files

### `Copper.g4`

Main grammar file containing:
- **Parser rules**: Program structure, statements, expressions
- **Lexer rules**: Keywords, literals, delimiters
- **Lexer modes**: DAX expression handling
- **Context sensitivity**: Keyword-as-identifier support

### `DAX.g4`

Comprehensive DAX lexer grammar with:
- **Function names**: 200+ DAX functions across all categories
- **Operators**: Arithmetic, logical, comparison
- **Literals**: Numbers, strings, booleans, dates
- **References**: Tables, columns, measures
- **Keywords**: VAR, RETURN, IF, SWITCH, etc.

## Error Handling

The grammar includes comprehensive error handling:

- **Lexer errors**: Invalid characters, unterminated strings
- **Parser errors**: Syntax errors with position information
- **Recovery**: Automatic error recovery for partial parsing
- **Reporting**: Detailed error messages with context

## Performance

ANTLR4 provides excellent performance characteristics:

- **Linear parsing**: O(n) time complexity for most inputs
- **Memory efficient**: Minimal memory overhead
- **Incremental parsing**: Support for partial re-parsing
- **Caching**: Parse tree caching for repeated access

## Contributing

### Adding Language Support

1. Add language entry to `LANGUAGES` array in `build.sh`
2. Add language-specific options in `generate_parser()` function
3. Create wrapper generation function if needed
4. Test with example files

### Extending Grammar

1. Update `Copper.g4` with new syntax rules
2. Add corresponding lexer tokens
3. Update test files
4. Regenerate all parsers
5. Update documentation

### Testing Changes

```bash
# Validate grammar syntax
antlr4 -encoding UTF-8 Copper.g4

# Test against examples
./build.sh generate java
./build.sh test
```

## Migration from Python Parser

The ANTLR parsers provide the same functionality as the hand-written Python parser:

| Python Parser | ANTLR Equivalent |
|---------------|------------------|
| `CopperTokenizer` | Generated lexer |
| `CopperParser` | Generated parser |
| `ASTNode` classes | Parse tree nodes |
| `parse_file()` | Language-specific APIs |
| Error handling | Built-in error reporting |

### Migration Steps

1. Replace Python parser imports with ANTLR generated classes
2. Update AST traversal to use ANTLR visitors/listeners  
3. Adapt error handling to ANTLR error reporting
4. Test with existing Copper files

## Troubleshooting

### Common Issues

**Grammar compilation errors:**
```bash
# Check grammar syntax
antlr4 -encoding UTF-8 Copper.g4
```

**Missing ANTLR4:**
```bash
# Install ANTLR4 (varies by platform)
brew install antlr          # macOS
apt install antlr4          # Ubuntu
```

**Parser generation fails:**
```bash
# Check Java classpath includes ANTLR4
export CLASSPATH=".:$ANTLR_JAR:$CLASSPATH"
```

**Runtime errors:**
- Ensure ANTLR runtime version matches grammar version
- Check that generated files are in correct package/namespace
- Verify input encoding (UTF-8 recommended)

### Debug Mode

Enable ANTLR debug mode for troubleshooting:

```bash
# Generate with debug info
antlr4 -Dlanguage=Java -visitor -listener -Xlog Copper.g4
```

## License

This ANTLR grammar is released under the MIT License, same as the main Copper project.

## Resources

- [ANTLR4 Documentation](https://github.com/antlr/antlr4/blob/master/doc/index.md)
- [ANTLR4 Grammar Examples](https://github.com/antlr/grammars-v4)
- [Copper Language Specification](../spec/SPECIFICATION.md)
- [Original Python Parser](../parser/)