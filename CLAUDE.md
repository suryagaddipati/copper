# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# Copper: The Universal Semantic Layer

## Project Overview

**Copper is a portable semantic layer that compiles metric definitions and queries into runtime code across multiple engines.** The project motto is "Define Once. Run Anywhere. ☄️"

This is a complex multi-language project that implements a DAX-like expression language parser and semantic modeling system with support for multiple execution engines (Pandas, Spark, SQL, Apache Beam).

## Current State

✅ **Current Status**: The project is actively developed with both Python semantic layer and Next.js web studio:
- Complete Python semantic layer implementation using src/ layout
- ANTLR4 grammar for DAX-like expressions (`grammar/Copper.g4`)
- Next.js web studio with comprehensive UI (`studio/`)
- SQL generation engine alongside Pandas execution
- UFC analytics example with real MMA fight data
- YAML-based semantic modeling with Pydantic validation
- Full test coverage for both Python and TypeScript components

## Historical Architecture (from git history)

The project previously had a rich multi-component architecture:

### Core Components
- **Grammar & Parser**: ANTLR4-based DAX expression parser (`grammar/Copper.g4`)
- **Python Core**: Expression parsing and semantic modeling (`src/parser/antlr_parser.py`)
- **Web Studio**: Next.js-based development interface with Monaco editor
- **API Backend**: Python FastAPI server for semantic model management
- **Examples**: Multiple demo projects showcasing capabilities

### Technology Stack

#### Languages & Frameworks
- **Python**: Core semantic layer implementation, API backend
- **TypeScript/JavaScript**: Next.js web interface, React components
- **Java**: ANTLR parser generation
- **ANTLR4**: Grammar definition and parser generation

#### Frontend (Next.js Studio)
- **Framework**: Next.js with TypeScript
- **Editor**: Monaco Editor with custom Copper language support
- **UI**: React components for dashboard, model explorer, validation
- **Styling**: Tailwind CSS
- **State Management**: Custom hooks for connections, projects, parsing

#### Backend (Python API)
- **Framework**: FastAPI
- **Features**: Connection management, project storage, query execution
- **Database**: JSON-based storage for projects and connections
- **Execution Engines**: Pandas (with planned Spark, SQL, Beam support)

#### Build System
- **Makefile**: Comprehensive build automation
- **ANTLR**: Grammar compilation to multiple target languages
- **npm/yarn**: Frontend dependency management
- **pip**: Python dependency management

## Key Features (from PRD)

### Expression Language
- DAX-like syntax with functions: `SUM()`, `COUNT()`, `IF()`, `SWITCH()`, `CASE`
- Boolean logic and conditional expressions
- Filter context support: `COUNT(Orders.id WHERE Orders.status = "shipped")`
- Nested expressions and function composition

### Semantic Modeling
- **YAML-based schema** for dimensions, measures, relationships
- **Type system**: string, number, currency, boolean types
- **Relationship modeling**: Star/snowflake schema support
- **Join logic**: Automatic relationship traversal

### Multi-Engine Execution
- **Pandas**: Complete implementation with groupby, agg, join operations
- **SQL Generation**: Universal SQL generation for multiple dialects
- **Apache Beam**: Streaming analytics with windowing (planned)
- **DuckDB**: Client-side WASM execution in web studio (partially integrated)

### Developer Experience
- **Web Studio**: Visual interface for model development
- **Validation**: Real-time expression and schema validation
- **Auto-complete**: YAML schema assistance
- **Error handling**: Detailed error messages and suggestions

## Development Workflow

### Build Commands

#### Python Backend
```bash
# Development setup
make dev-install     # Install with development dependencies
make setup          # Full setup including parser generation

# Core development commands
make parser         # Generate ANTLR parser (requires Java)
make test           # Run pytest with coverage
make format         # Code formatting with black
make typecheck      # Type checking with mypy
make clean          # Clean generated files

# Demo and examples
make example        # Run basic demo
python examples/ufc_demo.py  # UFC analytics demonstration
```

#### Frontend Studio
```bash
cd studio
npm install         # Install dependencies
npm run dev         # Development server (port 3001)
npm run build       # Production build
npm run test        # Jest test suite
npm run lint        # ESLint checking
```

### Current Project Structure
```
copper/
├── src/                       # Main Python package (source code)
│   ├── __init__.py            # Package entry point with exports
│   ├── parser/                # ANTLR-based expression parser
│   │   ├── antlr_parser.py    # Python parser implementation
│   │   └── ast_nodes.py       # AST node definitions
│   ├── semantic/              # YAML schema and semantic model
│   │   ├── schema.py          # Pydantic model definitions
│   │   └── loader.py          # YAML model loader
│   ├── query/                 # Query builder and planning
│   │   └── builder.py         # Fluent query API
│   └── executors/             # Execution engines
│       ├── pandas_executor.py # Pandas backend implementation
│       └── sql_generator.py   # Universal SQL generation
├── studio/                    # Next.js web application
│   ├── src/
│   │   ├── app/               # Next.js app router pages
│   │   ├── components/        # React UI components
│   │   │   ├── DataVisualization.tsx  # Chart rendering
│   │   │   ├── ProjectPanel.tsx       # Project browsing
│   │   │   ├── QueryBuilder.tsx       # Query execution
│   │   │   └── Sidebar.tsx            # Field selection
│   │   └── lib/               # Utilities and core logic
│   ├── public/                # Static assets and example projects
│   ├── package.json           # Node.js dependencies
│   └── jest.config.js         # Frontend test configuration
├── grammar/
│   └── Copper.g4              # ANTLR grammar definition
├── tests/                     # Python test suite
│   ├── test_semantic_model.py # YAML validation and loading
│   ├── test_query_builder.py  # Query API functionality
│   ├── test_pandas_executor.py # Pandas execution engine
│   └── test_sql_generator.py  # SQL generation
├── example-projects/          # Modular example projects
│   ├── ufc/                   # UFC/MMA analytics
│   │   ├── data/              # Real UFC fight datasets (CSV)
│   │   ├── datasources.yaml   # Data source definitions
│   │   ├── model.yaml         # Semantic model
│   │   ├── project.yaml       # Project configuration
│   │   └── data_loader.py     # UFC data loading utilities
│   └── analytics-example/     # General analytics example
├── setup.py                   # Python package configuration
├── requirements.txt           # Python dependencies
├── pytest.ini                # Test configuration
├── Makefile                   # Build automation
└── SCHEMA_REFERENCE.md        # Comprehensive schema documentation
```

## UFC Analytics Example

### UFC Data Model
```yaml
name: ufc_analytics
description: UFC/MMA analytics semantic model

datasources:
  events:
    type: table
    table: ufc_events
    description: UFC event information
  fighters:
    type: table
    table: ufc_fighter_details
    description: Fighter profiles
  fight_results:
    type: table
    table: ufc_fight_results
    description: Fight outcomes

relationships:
  - fight_results.event_id → events.event_id
  - fight_results.fighter_1_id → fighters.fighter_id
  - fight_results.fighter_2_id → fighters.fighter_id

dimensions:
  weight_class:
    expression: fight_results.weight_class
    type: string
    label: Weight Class
    
  nationality:
    expression: fighters.nationality
    type: string
    label: Nationality

measures:
  total_fights:
    expression: COUNT(fight_results.fight_id)
    type: number
    label: Total Fights
    
  finish_rate:
    expression: COUNT(fight_results.fight_id WHERE fight_results.method != "Decision") / COUNT(fight_results.fight_id) * 100
    type: number
    format: "%.1f%%"
    label: Finish Rate
```

### Query Examples
```python
import src as copper
from example_projects.ufc.data_loader import UFCDataLoader

# Load real UFC data
loader = UFCDataLoader()
ufc_data = loader.load_all_data()

# Load semantic model
model = copper.load("example-projects/ufc/model.yaml")

# Analyze finish rates by weight class
query = copper.Query(model) \
    .dimensions(['weight_class']) \
    .measures(['total_fights', 'finish_rate'])

result = query.to_pandas(ufc_data)
print(result)
```

### Advanced UFC Analytics
```yaml
# Fighter performance metrics
striking_accuracy:
  expression: AVG(fight_details.significant_strikes_landed / fight_details.significant_strikes_attempted) * 100
  type: number
  format: "%.1f%%"
  label: Striking Accuracy

# Title fight analysis  
title_fight_finish_rate:
  expression: COUNT(fight_results.fight_id WHERE fight_results.is_title_fight = true AND fight_results.method != "Decision") / COUNT(fight_results.fight_id WHERE fight_results.is_title_fight = true) * 100
  type: number
  format: "%.1f%%"
  label: Title Fight Finish Rate
```

## Development Environment Setup

### Prerequisites
- **Python 3.8+** with pip
- **Node.js 18+** with npm
- **Java 8+** for ANTLR parser generation
- **ANTLR 4.9.3** complete JAR

### Dependencies
- **Python**: pandas, pydantic, pytest, ANTLR4 runtime, PyYAML
- **Java**: ANTLR complete JAR for parser generation
- **Data**: Real UFC fight data in CSV format for demonstrations

## Testing Strategy

### Python Tests
```bash
pytest                    # Run all Python tests
pytest tests/test_pandas_executor.py  # Run specific test file
pytest --cov=src         # Run with coverage reporting
```

### Frontend Tests
```bash
cd studio
npm test                 # Run Jest test suite
npm test -- --watch     # Run tests in watch mode
```

The project includes comprehensive testing:
- **Python unit tests**: Parser validation, semantic model loading, query execution
- **Frontend tests**: Expression parsing, semantic processing, validation logic
- **Integration tests**: End-to-end query execution workflows
- **Real data testing**: UFC analytics with actual MMA datasets

## Git Workflow

- **main**: Primary development branch
- **ui/barebones**: Current stripped-down branch
- **feature/api-webapp**: API development branch
- **ui/ufc**: Alternative UI branch

## Claude Configuration

The project has extensive Claude permissions configured in `.claude/settings.local.json` including:
- File system operations
- Git operations  
- Build system execution
- Web development tools
- Python/npm package management
- Playwright browser automation

## Common Development Tasks

### Working with Semantic Models
```bash
# Load and validate a YAML model
python -c "import src as copper; model = copper.load('example-projects/ufc/model.yaml')"

# Test query execution with real data
python example-projects/ufc/data_loader.py
```

### Web Studio Development
```bash
# Start development server
cd studio && npm run dev

# Access at http://localhost:3001
# Project data is served from studio/public/example-projects/
```

### Parser Development
```bash
# Regenerate ANTLR parser after grammar changes
make parser

# Test expression parsing
python -c "from src.parser.antlr_parser import CopperExpressionParser; parser = CopperExpressionParser()"
```

## Architecture Notes

### Query Execution Flow
1. **YAML Model Loading**: Pydantic validation of semantic models
2. **Query Building**: Fluent API constructs query objects
3. **SQL Generation**: Universal SQL output for any dialect
4. **Pandas Execution**: Direct DataFrame operations for in-memory data
5. **DuckDB Integration**: WASM-based execution in web browser

### Web Studio Components
- **ProjectPanel**: Dynamic project loading from any URL
- **Sidebar**: Dimension/measure field selection with drag-and-drop
- **QueryBuilder**: SQL query execution and result display
- **DataVisualization**: Multi-format chart rendering (bar, line, pie, scatter)

### Expression Language
The DAX-like expression syntax supports:
- Standard aggregations: `COUNT()`, `SUM()`, `AVG()`, `MIN()`, `MAX()`
- Conditional logic: `IF()`, `SWITCH()`, `CASE`
- Filter contexts: `COUNT(table.field WHERE condition)`
- Boolean operators and nested expressions