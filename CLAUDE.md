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
# Start both API and webapp with one command
cd app && ./start.sh

# This will:
# 1. Install webapp dependencies if needed
# 2. Start FastAPI server on localhost:8000
# 3. Start React webapp on localhost:3000
# Press Ctrl+C to stop both servers
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
# Navigate to grammar directory first
cd grammar

# Generate parsers for all languages (Java, Python, JavaScript, TypeScript, C#, Go, C++, Swift)
./build.sh generate

# Generate specific language parsers
./build.sh generate java python javascript

# Clean build directory
./build.sh clean

# Test generated parsers against example files
./build.sh test
```

### Java Parser (Gradle)
```bash
cd grammar
gradle generateGrammarSource  # Generate Java parser only
gradle generateAllParsers     # Generate all language parsers
gradle build                  # Build Java parser
gradle test                   # Run Java tests
```

### Python Parser
```bash
cd grammar
python setup.py build_py     # Generate Python parser
pip install -e .             # Install in development mode
```

## Development Environment Setup

### Python Environment
```bash
# API development requires Python virtual environment
cd api
python3 -m venv venv
source venv/bin/activate     # Linux/Mac
# venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

### Node.js Environment
```bash
# Webapp development requires Node.js
cd webapp
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

1. **Live Demo Parser** (`api/antlr_parser.py`):
   - ANTLR-based Python parser for real-time web demo
   - Fast parsing for immediate feedback in Monaco Editor
   - Used by FastAPI backend for live validation

2. **Production Parser System** (`grammar/` directory):
   - Complete ANTLR4 grammar generating parsers for 8+ languages
   - Full AST generation with visitors and listeners
   - Comprehensive error recovery and position tracking
   - Used for production tooling and language integrations

## Architecture

### Live Parsing System
- **FastAPI Backend**: `api/main.py` provides REST endpoints for real-time parsing
- **React Frontend**: `webapp/src/App.tsx` with Monaco Editor and custom Copper syntax highlighting
- **Monaco Integration**: `webapp/src/copper-language.ts` provides advanced syntax highlighting for Copper
- **Real-time Validation**: Live parsing results with error reporting and statistics

### Multi-Language Parser System
- **ANTLR4 Grammar**: `grammar/Copper.g4` defines the complete Copper syntax
- **DAX Grammar**: `grammar/DAX.g4` handles DAX expressions as blackbox strings using lexer modes
- **Build System**: Universal `build.sh` script generates parsers for 8+ programming languages
- **Language Targets**: Java, Python, JavaScript, TypeScript, C#, Go, C++, Swift
- **Python Integration**: `api/antlr_parser.py` wraps generated Python parser for API use

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
cd webapp
npm run lint        # ESLint TypeScript/React checking
npm run type-check  # TypeScript type checking without compilation
npm run build       # Test production build
```

### Parser Testing
```bash
cd grammar
./build.sh test     # Test all generated parsers against example files
gradle test         # Run Java parser tests
```

### API Testing
```bash
cd api
# Test live parsing endpoints
curl -X POST "http://localhost:8000/parse" \
  -H "Content-Type: application/json" \
  -d '{"code": "model: test { dimension: id { type: string } }"}'
```

## Configuration

### Key Configuration Files
- `.claude/settings.local.json` - Claude Code permissions configuration
- `webapp/vite.config.ts` - Vite dev server configuration (port 3000)
- `webapp/tsconfig.json` - TypeScript strict mode with React JSX
- `webapp/package.json` - Dependencies: React, Monaco Editor, Vite, ESLint
- `api/requirements.txt` - Python dependencies: FastAPI, uvicorn, pydantic
- `grammar/build.gradle` - Multi-language ANTLR4 parser generation
- `grammar/requirements.txt` - ANTLR4 development tools

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
cd api
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
- Check `webapp/src/copper-language.ts` for language definition
- Verify Monaco Editor is properly imported in `App.tsx`
- Check browser console for JavaScript errors

**Parser generation fails**
```bash
cd grammar
./build.sh clean    # Clean build directory
./build.sh generate # Regenerate all parsers
```