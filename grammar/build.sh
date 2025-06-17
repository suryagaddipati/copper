#!/bin/bash
#
# Universal build script for Copper ANTLR parsers
# Generates parsers for multiple programming languages
#

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ANTLR_DIR="$SCRIPT_DIR"
BUILD_DIR="$SCRIPT_DIR/build"
GRAMMAR_FILE="Copper.g4"

# Supported languages and their ANTLR targets
declare -A LANGUAGES=(
    ["java"]="Java"
    ["python"]="Python3"
    ["javascript"]="JavaScript"
    ["typescript"]="TypeScript"
    ["csharp"]="CSharp"
    ["go"]="Go"
    ["cpp"]="Cpp"
    ["swift"]="Swift"
)

# Function to print colored output
print_status() {
    local color=$1
    local message=$2
    echo -e "${color}${message}${NC}"
}

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to check prerequisites
check_prerequisites() {
    print_status $BLUE "Checking prerequisites..."
    
    if ! command_exists antlr4; then
        print_status $RED "✗ antlr4 command not found"
        echo "Please install ANTLR4:"
        echo "  - macOS: brew install antlr"
        echo "  - Ubuntu/Debian: apt-get install antlr4"
        echo "  - Manual: https://github.com/antlr/antlr4/blob/master/doc/getting-started.md"
        exit 1
    fi
    
    if [ ! -f "$ANTLR_DIR/$GRAMMAR_FILE" ]; then
        print_status $RED "✗ Grammar file not found: $ANTLR_DIR/$GRAMMAR_FILE"
        exit 1
    fi
    
    print_status $GREEN "✓ Prerequisites satisfied"
}

# Function to generate parser for a specific language
generate_parser() {
    local lang=$1
    local target=${LANGUAGES[$lang]}
    local output_dir="$BUILD_DIR/$lang"
    
    print_status $BLUE "Generating $lang parser..."
    
    # Create output directory
    mkdir -p "$output_dir"
    
    # Generate parser
    local cmd=(antlr4 -Dlanguage="$target" -visitor -listener -o "$output_dir")
    
    # Add language-specific options
    case $lang in
        "java")
            cmd+=(-package com.copper.parser)
            ;;
        "csharp")
            cmd+=(-package Copper.Parser)
            ;;
        "go")
            cmd+=(-package parser)
            ;;
        "typescript")
            cmd+=(-visitor -listener)
            ;;
    esac
    
    cmd+=("$ANTLR_DIR/$GRAMMAR_FILE")
    
    if "${cmd[@]}"; then
        print_status $GREEN "✓ $lang parser generated successfully"
        
        # Post-generation tasks
        case $lang in
            "java")
                generate_java_wrapper "$output_dir"
                ;;
            "python")
                generate_python_wrapper "$output_dir"
                ;;
            "javascript"|"typescript")
                generate_js_package "$output_dir" "$lang"
                ;;
        esac
    else
        print_status $RED "✗ Failed to generate $lang parser"
        return 1
    fi
}

# Function to generate Java wrapper
generate_java_wrapper() {
    local output_dir=$1
    
    cat > "$output_dir/CopperParserMain.java" << 'EOF'
package com.copper.parser;

import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;
import java.io.*;

public class CopperParserMain {
    public static void main(String[] args) throws Exception {
        if (args.length == 0) {
            System.err.println("Usage: java CopperParserMain <copper-file>");
            System.exit(1);
        }
        
        // Create input stream
        ANTLRInputStream input = new ANTLRInputStream(new FileInputStream(args[0]));
        
        // Create lexer
        CopperLexer lexer = new CopperLexer(input);
        CommonTokenStream tokens = new CommonTokenStream(lexer);
        
        // Create parser
        CopperParser parser = new CopperParser(tokens);
        
        // Parse starting from 'program' rule
        ParseTree tree = parser.program();
        
        // Print parse tree
        System.out.println(tree.toStringTree(parser));
    }
}
EOF
}

# Function to generate Python wrapper
generate_python_wrapper() {
    local output_dir=$1
    
    cat > "$output_dir/copper_parser_main.py" << 'EOF'
#!/usr/bin/env python3
"""
Copper ANTLR Parser - Python wrapper
"""

import sys
import argparse
from antlr4 import *
from CopperLexer import CopperLexer
from CopperParser import CopperParser
from CopperListener import CopperListener


class CopperPrintListener(CopperListener):
    """Example listener that prints parse events"""
    
    def enterProgram(self, ctx):
        print("Entering program")
    
    def exitProgram(self, ctx):
        print("Exiting program")
    
    def enterModelStatement(self, ctx):
        model_name = ctx.identifier().getText()
        print(f"Found model: {model_name}")
    
    def enterViewStatement(self, ctx):
        view_name = ctx.identifier().getText()
        print(f"Found view: {view_name}")


def main():
    parser = argparse.ArgumentParser(description='Parse Copper files')
    parser.add_argument('file', help='Copper file to parse')
    parser.add_argument('--tree', action='store_true', help='Print parse tree')
    parser.add_argument('--tokens', action='store_true', help='Print tokens')
    
    args = parser.parse_args()
    
    try:
        # Create input stream
        input_stream = FileStream(args.file)
        
        # Create lexer
        lexer = CopperLexer(input_stream)
        
        if args.tokens:
            # Print tokens
            tokens = CommonTokenStream(lexer)
            tokens.fill()
            for token in tokens.tokens:
                print(f"{token.type}: {token.text}")
            return
        
        # Create token stream and parser
        stream = CommonTokenStream(lexer)
        copper_parser = CopperParser(stream)
        
        # Parse starting from 'program' rule
        tree = copper_parser.program()
        
        if args.tree:
            # Print parse tree
            print(tree.toStringTree(recog=copper_parser))
        else:
            # Use listener
            listener = CopperPrintListener()
            walker = ParseTreeWalker()
            walker.walk(listener, tree)
    
    except Exception as e:
        print(f"Error parsing file: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
EOF
    
    chmod +x "$output_dir/copper_parser_main.py"
}

# Function to generate JavaScript/TypeScript package
generate_js_package() {
    local output_dir=$1
    local lang=$2
    
    cat > "$output_dir/package.json" << EOF
{
  "name": "copper-antlr-parser-$lang",
  "version": "1.0.0",
  "description": "ANTLR4-generated $lang parser for the Copper metadata language",
  "main": "index.js",
  "scripts": {
    "test": "node test.js",
    "parse": "node copper-parser.js"
  },
  "dependencies": {
    "antlr4": "^4.13.1"
  },
  "keywords": ["antlr", "parser", "copper", "metadata", "dax"],
  "author": "Copper Language Team",
  "license": "MIT"
}
EOF

    # Create main entry point
    cat > "$output_dir/index.js" << 'EOF'
const antlr4 = require('antlr4');
const CopperLexer = require('./CopperLexer').CopperLexer;
const CopperParser = require('./CopperParser').CopperParser;
const CopperListener = require('./CopperListener').CopperListener;

class CopperParserWrapper {
    static parse(input) {
        const chars = new antlr4.InputStream(input);
        const lexer = new CopperLexer(chars);
        const tokens = new antlr4.CommonTokenStream(lexer);
        const parser = new CopperParser(tokens);
        
        return parser.program();
    }
    
    static parseFile(filename) {
        const fs = require('fs');
        const input = fs.readFileSync(filename, 'utf8');
        return this.parse(input);
    }
}

module.exports = {
    CopperParserWrapper,
    CopperLexer,
    CopperParser,
    CopperListener
};
EOF

    # Create CLI tool
    cat > "$output_dir/copper-parser.js" << 'EOF'
#!/usr/bin/env node

const { CopperParserWrapper } = require('./index');

if (process.argv.length < 3) {
    console.error('Usage: node copper-parser.js <copper-file>');
    process.exit(1);
}

const filename = process.argv[2];

try {
    const tree = CopperParserWrapper.parseFile(filename);
    console.log('Parse successful!');
    console.log('Tree:', tree.toStringTree());
} catch (error) {
    console.error('Parse error:', error.message);
    process.exit(1);
}
EOF

    chmod +x "$output_dir/copper-parser.js"
}

# Function to test generated parsers
test_parsers() {
    print_status $BLUE "Testing generated parsers..."
    
    local example_file="../../examples/ecommerce_orders.copper"
    
    if [ ! -f "$example_file" ]; then
        print_status $YELLOW "⚠ No example files found for testing"
        return
    fi
    
    # Test Java parser
    if [ -d "$BUILD_DIR/java" ]; then
        print_status $BLUE "Testing Java parser..."
        # This would require compilation, skipping for now
        print_status $YELLOW "⚠ Java parser test requires compilation"
    fi
    
    # Test Python parser
    if [ -d "$BUILD_DIR/python" ]; then
        print_status $BLUE "Testing Python parser..."
        if command_exists python3; then
            cd "$BUILD_DIR/python"
            if python3 copper_parser_main.py "$example_file" --tree >/dev/null 2>&1; then
                print_status $GREEN "✓ Python parser test passed"
            else
                print_status $RED "✗ Python parser test failed"
            fi
            cd "$SCRIPT_DIR"
        fi
    fi
}

# Function to show usage
show_usage() {
    echo "Usage: $0 [COMMAND] [LANGUAGE...]"
    echo ""
    echo "Commands:"
    echo "  generate [lang...]  Generate parsers for specified languages (default: all)"
    echo "  clean              Clean build directory"
    echo "  test               Test generated parsers"
    echo "  help               Show this help"
    echo ""
    echo "Supported languages:"
    for lang in "${!LANGUAGES[@]}"; do
        echo "  $lang (${LANGUAGES[$lang]})"
    done | sort
    echo ""
    echo "Examples:"
    echo "  $0 generate java python    # Generate Java and Python parsers"
    echo "  $0 generate                 # Generate all parsers"
    echo "  $0 clean                    # Clean build directory"
}

# Main function
main() {
    local command=${1:-generate}
    shift || true
    
    case $command in
        "generate")
            check_prerequisites
            
            if [ $# -eq 0 ]; then
                # Generate all languages
                print_status $BLUE "Generating parsers for all languages..."
                for lang in "${!LANGUAGES[@]}"; do
                    generate_parser "$lang"
                done
            else
                # Generate specified languages
                for lang in "$@"; do
                    if [[ -n "${LANGUAGES[$lang]}" ]]; then
                        generate_parser "$lang"
                    else
                        print_status $RED "✗ Unsupported language: $lang"
                        exit 1
                    fi
                done
            fi
            
            print_status $GREEN "✓ Parser generation completed"
            ;;
        
        "clean")
            print_status $BLUE "Cleaning build directory..."
            rm -rf "$BUILD_DIR"
            print_status $GREEN "✓ Build directory cleaned"
            ;;
        
        "test")
            test_parsers
            ;;
        
        "help"|"-h"|"--help")
            show_usage
            ;;
        
        *)
            print_status $RED "✗ Unknown command: $command"
            show_usage
            exit 1
            ;;
    esac
}

# Run main function with all arguments
main "$@"