# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# Copper: The Universal Semantic Layer

## Project Overview

**Copper is a portable semantic layer that compiles metric definitions and queries into runtime code across multiple engines.** The project motto is "Define Once. Run Anywhere. ☄️"

This is a Python-based project that implements a DAX-like expression language parser and semantic modeling system with support for multiple execution engines (Pandas, SQL generation, with planned support for Spark, Apache Beam).

## Current State

✅ **Current Status**: Active Python semantic layer implementation:
- Complete Python semantic layer implementation using src/ layout
- ANTLR4 grammar for DAX-like expressions (`grammar/Copper.g4`)
- SQL generation engine alongside Pandas execution
- UFC analytics example with real MMA fight data
- YAML-based semantic modeling with Pydantic validation
- Comprehensive Python test coverage

⚠️ **Note**: The project previously had a Next.js web studio component, but it's not currently present in the codebase. The CLAUDE.md file contains historical references to frontend components that may have been removed.

## Technology Stack

### Core Components
- **Grammar & Parser**: ANTLR4-based DAX expression parser (`grammar/Copper.g4`)
- **Python Core**: Expression parsing and semantic modeling (`src/parser/antlr_parser.py`)
- **Examples**: UFC analytics example with real data

### Languages & Frameworks
- **Python**: Core semantic layer implementation
- **Java**: ANTLR parser generation (build-time dependency)
- **ANTLR4**: Grammar definition and parser generation

### Build System
- **Makefile**: Comprehensive build automation
- **ANTLR**: Grammar compilation to Python
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

#### Python Development
```bash
# Development setup
make sync           # Sync dependencies from lock file
make dev-install    # Install with development dependencies
make setup          # Full setup including parser generation

# Core development commands
make parser         # Generate ANTLR parser (requires Java)
make test           # Run pytest with coverage
make format         # Code formatting with black
make typecheck      # Type checking with mypy
make lint           # Run format and typecheck
make clean          # Clean generated files

# Demo and examples
make example        # Run basic demo
make ufc-explore    # UFC analytics demonstration
```

#### Specific Test Commands
```bash
uv run python -m pytest                              # Run all tests
uv run python -m pytest tests/test_pandas_executor.py  # Run specific test file
uv run python -m pytest --cov=src                   # Run with coverage reporting
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
├── grammar/
│   └── Copper.g4              # ANTLR grammar definition
├── tests/                     # Python test suite
│   ├── test_semantic_model.py # YAML validation and loading
│   ├── test_query_builder.py  # Query API functionality
│   ├── test_pandas_executor.py # Pandas execution engine
│   └── test_sql_generator.py  # SQL generation
├── examples/                  # Example projects
│   └── ufc/                   # UFC/MMA analytics
│       ├── ufc_fights_all.csv # Real UFC fight dataset
│       ├── explore.py         # UFC data exploration script
│       └── README.md          # UFC example documentation
├── docs/                      # Documentation (currently empty)
├── setup.py                   # Python package configuration
├── requirements.txt           # Python dependencies
├── pytest.ini                # Test configuration
├── Makefile                   # Build automation
├── README.md                  # Main project documentation
├── SCHEMA_REFERENCE.md        # Comprehensive schema documentation
└── CLAUDE.md                  # This file
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

# Load semantic model (when available)
# model = copper.load("examples/ufc/model.yaml")

# For now, explore the UFC data directly
# See examples/ufc/explore.py for current UFC data exploration
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

## Key Dependencies

### Python Libraries
- **pandas**: Data manipulation and analysis
- **pydantic**: Data validation and parsing
- **pytest**: Testing framework
- **ANTLR4 runtime**: Expression parsing
- **PyYAML**: YAML file processing

### Development Tools
- **uv**: Fast Python package manager and environment manager
- **black**: Code formatting
- **mypy**: Type checking
- **Java**: Required for ANTLR parser generation

## Testing Strategy

### Python Tests
```bash
pytest                    # Run all Python tests
pytest tests/test_pandas_executor.py  # Run specific test file
pytest --cov=src         # Run with coverage reporting
make test                 # Run tests via Makefile
```

The project includes comprehensive testing:
- **Python unit tests**: Parser validation, semantic model loading, query execution
- **Integration tests**: End-to-end query execution workflows
- **Real data testing**: UFC analytics with actual MMA datasets

## Git Workflow

- **main**: Primary development branch (current)

## Prerequisites & Setup

### Required Tools
- **Python 3.8+** with uv package manager
- **Java 8+** for ANTLR parser generation
- **ANTLR 4.9.3** complete JAR (downloaded automatically by Makefile)

### Setup Process
1. `make sync` - Sync dependencies from lock file
2. `make dev-install` - Install with development dependencies
3. `make parser` - Generate ANTLR parser (requires Java)
4. `make test` - Verify installation

### Important Notes
- The project uses **uv** for Python dependency management
- All Python commands run through `uv run python` for proper environment isolation
- The Makefile references `copper/` directory for source code, but actual source is in `src/`
- ANTLR parser generation creates files in `copper/parser/generated/` (may need adjustment)

## Common Development Tasks

### Working with Semantic Models
```bash
# Load and validate a YAML model (when model files exist)
# uv run python -c "import src as copper; model = copper.load('examples/ufc/model.yaml')"

# Explore UFC data directly
make ufc-explore
```

### Parser Development
```bash
# Regenerate ANTLR parser after grammar changes
make parser

# Test expression parsing
uv run python -c "from src.parser.antlr_parser import CopperExpressionParser; parser = CopperExpressionParser()"
```

### Package Development
```bash
# Sync dependencies and install in development mode
make sync
make dev-install

# Or just sync from lock file
make sync
```

## Architecture Notes

### Query Execution Flow
1. **YAML Model Loading**: Pydantic validation of semantic models
2. **Query Building**: Fluent API constructs query objects
3. **SQL Generation**: Universal SQL output for any dialect
4. **Pandas Execution**: Direct DataFrame operations for in-memory data

### Core Components

#### Parser (`src/parser/`)
- **antlr_parser.py**: Main ANTLR-based expression parser
- **ast_nodes.py**: AST node definitions for parsed expressions

#### Semantic Layer (`src/semantic/`)
- **schema.py**: Pydantic model definitions for YAML validation
- **loader.py**: YAML model loading and validation

#### Query Builder (`src/query/`)
- **builder.py**: Fluent API for building queries

#### Executors (`src/executors/`)
- **pandas_executor.py**: Pandas-based execution engine
- **sql_generator.py**: SQL generation for multiple dialects

### Expression Language
The DAX-like expression syntax supports:
- Standard aggregations: `COUNT()`, `SUM()`, `AVG()`, `MIN()`, `MAX()`
- Conditional logic: `IF()`, `SWITCH()`, `CASE`
- Filter contexts: `COUNT(table.field WHERE condition)`
- Boolean operators and nested expressions