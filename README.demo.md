# Copper Parser Demo

This demo provides a live web interface for parsing and validating Copper language files.

## Features

- **Live Parsing**: Real-time syntax validation as you type
- **Syntax Highlighting**: Custom Monaco Editor configuration for Copper language
- **Example Files**: All example Copper files are preloaded and selectable
- **Parse Results**: Detailed validation results with error reporting
- **Statistics**: Model, view, dimension, measure, and join counts
- **REST API**: FastAPI backend for programmatic access

## Quick Start

```bash
# Run the complete demo (API + Webapp)
./start.sh
```

This will:
1. Install Python dependencies for the API
2. Install Node.js dependencies for the webapp
3. Start the API server on http://localhost:8000
4. Start the webapp on http://localhost:3000

## Manual Setup

### API Backend

```bash
cd api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

### Webapp Frontend

```bash
cd webapp
npm install
npm run dev
```

## API Endpoints

- `GET /` - API information
- `GET /health` - Health check
- `POST /parse` - Parse Copper content
- `GET /examples` - List all example files
- `GET /examples/{name}` - Get specific example

### Example API Usage

```bash
# Parse Copper content
curl -X POST http://localhost:8000/parse \
  -H "Content-Type: application/json" \
  -d '{"content": "model: test { dimension: id { type: string } }"}'

# Get all examples
curl http://localhost:8000/examples

# Get specific example
curl http://localhost:8000/examples/Ecommerce%20Orders
```

## Architecture

### Backend (FastAPI)
- `api/main.py` - FastAPI application with CORS enabled
- `api/copper_parser.py` - Simple Copper language parser
- `api/requirements.txt` - Python dependencies

### Frontend (React + Vite)
- `webapp/src/App.tsx` - Main React application
- `webapp/src/copper-language.ts` - Monaco Editor language definition
- `webapp/src/index.css` - Dark theme styling
- `webapp/package.json` - Node.js dependencies

### Parser Features
- Model and view declarations
- Dimension, measure, and join parsing
- Property extraction (type, expression, label, etc.)
- Basic syntax validation
- Error and warning reporting

## Supported Copper Syntax

The parser recognizes:
- **Models**: `model: name { ... }`
- **Views**: `view: name { ... }`
- **Dimensions**: `dimension: name { type: string, expression: ... }`
- **Measures**: `measure: name { type: sum, expression: ... }`
- **Joins**: `join: name { type: left_outer, relationship: many_to_one }`
- **Properties**: `label`, `description`, `value_format`, `primary_key`, etc.
- **DAX Expressions**: Expressions ending with `;;`

## Development

### Adding New Language Features

1. Update `api/copper_parser.py` to handle new syntax
2. Add new keywords to `webapp/src/copper-language.ts`
3. Update syntax highlighting rules
4. Test with example files

### Extending the API

The FastAPI backend can be extended with additional endpoints:
- Compilation to SQL/DAX
- Schema validation
- Metric dependency analysis
- Export to other formats

## Browser Support

The webapp requires a modern browser with:
- ES2020 support
- WebAssembly (for Monaco Editor)
- Fetch API
- CSS Grid and Flexbox