# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Copper is a metadata format for describing data dimensions and measures, inspired by LookML but using DAX expressions instead of SQL. This provides better compatibility with modern data processing tools like Spark and Dataflow.

## Repository Structure

```
/spec/          - Language specification documents
/grammar/       - Parser grammar definition (ANTLR4)
/examples/      - Sample .copper files demonstrating syntax
/app/api/       - FastAPI backend for live parsing
/app/web/       - React TypeScript frontend with Monaco Editor
/docs/          - Documentation (future)
```

## Key Files

- `spec/SPECIFICATION.md` - Complete Copper language specification
- `grammar/Copper.g4` - ANTLR4 grammar definition for Copper syntax
- `grammar/DAX.g4` - Complete DAX expression grammar
- `examples/*.copper` - Example models and views demonstrating various features
- `app/web/src/App.tsx` - Main React frontend component with Monaco Editor
- `app/api/main.py` - FastAPI backend with live parsing endpoints
- `app/start.sh` - Simple startup script for the full development environment

## Copper Language Basics

**Models** define data structure with dimensions and measures:
```copper
model: orders {
  dimension: order_id {
    type: string
    expression: Orders[OrderID] ;;
    primary_key: yes
  }
  
  measure: total_revenue {
    type: sum
    expression: Orders[Amount] ;;
    value_format: usd
  }
}
```

**Views** define how to query and join models:
```copper
view: sales_analysis {
  from: orders
  
  join: customers {
    type: left_outer
    relationship: many_to_one
    expression: Orders[CustomerID] = Customers[CustomerID] ;;
  }
}
```

## Key Concepts

- **DAX expressions**: Use DAX syntax instead of SQL in `expression:` parameters
- **LookML types**: Supports all LookML dimension and measure types
- **View inheritance**: Views can extend other views using `extends: [view_name]`
- **Value formatting**: Supports both named formats (`usd`, `percent_2`) and custom format strings

## Development Tasks

When working on Copper:
1. Reference `spec/SPECIFICATION.md` for complete syntax details
2. Use `grammar/Copper.g4` and `grammar/DAX.g4` for parser development
3. Check `examples/` for syntax patterns and best practices
4. Maintain backward compatibility with LookML concepts where possible

## Build Commands

### Quick Start - Full Development Environment
```bash
# Start both API and webapp using Makefile (recommended)
make dev

# This will:
# 1. Generate ANTLR parser from grammar
# 2. Install webapp dependencies if needed
# 3. Start FastAPI server on localhost:8000
# 4. Start React webapp on localhost:3000
# Press Ctrl+C to stop both servers, or run 'make stop'

# Alternative targets:
make all     # Build everything and start
make build   # Just build parser and install dependencies
make stop    # Stop running servers
make clean   # Clean generated files
make test    # Test parser functionality
```

### Webapp Development
```bash
cd app/web

# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Lint TypeScript/React code
npm run lint

# Type checking without compilation
npm run type-check
```

### API Development
```bash
cd app/api

# Install Python dependencies
pip install -r requirements.txt

# Start development server with auto-reload
python3 main.py

# Or start manual server (used by start.sh)
python3 server-manual.py

# Or use uvicorn directly
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Parser Generation
```bash
# Generate Python parser for API (using Makefile)
make parser

# Manual parser generation using ANTLR4 directly
cd app/api
antlr4 -Dlanguage=Python3 -o generated ../../grammar/Copper.g4

# The generated parser files will be in app/api/generated/:
# - CopperLexer.py
# - CopperParser.py  
# - CopperListener.py
```

## Development Environment Setup

### Python Environment
```bash
# API development requires Python virtual environment
cd app/api
python3 -m venv venv
source venv/bin/activate     # Linux/Mac
# venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

### Node.js Environment
```bash
# Webapp development requires Node.js
cd app/web
npm install
```

### Parser Development
```bash
# ANTLR4 grammar development
cd grammar
pip install -r requirements.txt  # Install ANTLR4 tools
```

## Dual Parser Architecture

This project uses two complementary parsing approaches:

1. **Live Demo Parser** (`app/api/antlr_parser.py`):
   - ANTLR-based Python parser for real-time web demo
   - Fast parsing for immediate feedback in Monaco Editor
   - Used by FastAPI backend for live validation

2. **Production Parser System** (`grammar/` directory):
   - Complete ANTLR4 grammar definitions for Copper language
   - DAX expression handling with lexer modes
   - Currently generates Python parser, extensible to other languages
   - Parser files generated in `app/api/generated/` directory

## Architecture

### Live Parsing System
- **FastAPI Backend**: `app/api/main.py` provides REST endpoints for real-time parsing
- **React Frontend**: `app/web/src/App.tsx` with Monaco Editor and custom Copper syntax highlighting
- **Monaco Integration**: `app/web/src/copper-language.ts` provides advanced syntax highlighting for Copper
- **Real-time Validation**: Live parsing results with error reporting and statistics

### Multi-Language Parser System
- **ANTLR4 Grammar**: `grammar/Copper.g4` defines the complete Copper syntax
- **DAX Grammar**: `grammar/DAX.g4` handles DAX expressions as blackbox strings using lexer modes
- **Build System**: Makefile-based parser generation for Python (extensible to other languages)
- **Python Integration**: `app/api/antlr_parser.py` wraps generated Python parser for API use
- **Generated Files**: Parser files are created in `app/api/generated/` directory

### Frontend Architecture
- **Vite + React**: Modern development setup with hot module replacement
- **TypeScript**: Full type safety throughout the webapp
- **Monaco Editor**: VS Code-quality editing experience with custom language support
- **Axios**: HTTP client for API communication with error handling

### Grammar Structure
- **Context-Sensitive Parsing**: Keywords can be used as identifiers when contextually appropriate
- **Lexer Modes**: DAX expressions triggered by `expression:`, `sql_latitude:`, `sql_longitude:` keywords
- **Error Recovery**: Comprehensive error handling with position information and automatic recovery

### Generated Parser Features
- **Visitors and Listeners**: ANTLR generates both visitor and listener patterns for AST traversal
- **Multi-Package Support**: Language-specific package structure (e.g., `com.copper.parser` for Java)
- **CLI Wrappers**: Generated main classes for testing parsers against Copper files

## Testing

### Frontend Testing
```bash
cd app/web
npm run lint        # ESLint TypeScript/React checking
npm run type-check  # TypeScript type checking without compilation
npm run build       # Test production build
```

### Parser Testing
```bash
# Test parser functionality using Makefile
make test

# Manual testing of parser
cd app/api
python3 -c "from antlr_parser import validate_copper_syntax; print(validate_copper_syntax('view: test { from: orders }'))"

# Test with example files
cd app/api
python3 -c "
from antlr_parser import validate_copper_syntax
with open('../../examples/customers.copper', 'r') as f:
    result = validate_copper_syntax(f.read())
    print(f'Valid: {result[\"valid\"]}, Models: {result[\"statistics\"][\"total_models\"]}, Views: {result[\"statistics\"][\"total_views\"]}')
"
```

### API Testing
```bash
cd app/api
# Test live parsing endpoints
curl -X POST "http://localhost:8000/parse" \
  -H "Content-Type: application/json" \
  -d '{"code": "model: test { dimension: id { type: string } }"}'

# Or use the Makefile test target
make test
```

## Configuration

### Key Configuration Files
- `.claude/settings.local.json` - Claude Code permissions configuration
- `app/web/vite.config.ts` - Vite dev server configuration (port 3000)
- `app/web/tsconfig.json` - TypeScript strict mode with React JSX
- `app/web/package.json` - Dependencies: React, Monaco Editor, Vite, ESLint
- `app/api/requirements.txt` - Python dependencies: FastAPI, uvicorn, pydantic
- `Makefile` - Development environment automation and build system
- `grammar/Copper.g4` - Complete ANTLR4 grammar for Copper language
- `grammar/DAX.g4` - DAX expression grammar for lexer modes

### Port Configuration
- **Webapp**: http://localhost:3000 (Vite dev server)
- **API**: http://localhost:8000 (FastAPI server)
- **CORS**: API configured to accept requests from webapp

## Troubleshooting

### Common Issues

**"Command not found: antlr4"**
```bash
cd grammar
pip install -r requirements.txt  # Install ANTLR4 tools
```

**"Module not found" errors in API**
```bash
cd app/api
source venv/bin/activate  # Activate Python virtual environment
pip install -r requirements.txt
```

**Port already in use**
```bash
# Kill processes on ports 3000 or 8000
lsof -ti:3000 | xargs kill -9
lsof -ti:8000 | xargs kill -9
```

**Monaco Editor syntax highlighting not working**
- Check `app/web/src/copper-language.ts` for language definition
- Verify Monaco Editor is properly imported in `App.tsx`
- Check browser console for JavaScript errors

**Parser generation fails**
```bash
# Clean and regenerate parser
make clean
make parser

# Check if ANTLR4 is installed
antlr4 --version
```