# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# Copper: The Universal Semantic Layer

## Project Overview

**Copper is a portable semantic layer that compiles metric definitions and queries into runtime code across multiple engines.** The project motto is "Define Once. Run Anywhere. ☄️"

This is a Python-based project that implements a DAX-like expression language parser and semantic modeling system with support for multiple execution engines (Pandas, SQL generation, with planned support for Spark, Apache Beam).

## Current State

✅ **Current Status**: Active Python semantic layer implementation:
- Complete Python semantic layer implementation using `src/` layout
- ANTLR4 grammar for DAX-like expressions (`grammar/Copper.g4`)
- SQL generation engine alongside Pandas execution
- UFC analytics example with real MMA fight data
- YAML-based semantic modeling with Pydantic validation
- Comprehensive Python test coverage using pytest

## Technology Stack

### Core Components
- **Grammar & Parser**: ANTLR4-based DAX expression parser (`grammar/Copper.g4`)
- **Python Core**: Expression parsing and semantic modeling (`src/parser/antlr_parser.py`)
- **Examples**: UFC analytics example with real data (`examples/ufc/`)

### Languages & Frameworks
- **Python**: Core semantic layer implementation (Python 3.8+)
- **Java**: ANTLR parser generation (build-time dependency)
- **ANTLR4**: Grammar definition and parser generation (v4.13.2)

### Build System
- **uv**: Modern Python package manager and environment manager
- **Makefile**: Comprehensive build automation
- **pyproject.toml**: Modern Python project configuration
- **ANTLR**: Grammar compilation to Python

## Development Workflow

### Build Commands

#### Essential Commands
```bash
# Development setup (run these first)
make sync           # Sync dependencies from uv.lock file
make dev-install    # Install with development dependencies  
make parser         # Generate ANTLR parser (requires Java)
make setup          # Full setup including parser generation

# Core development commands
make test           # Run pytest with coverage reporting
make format         # Code formatting with black
make typecheck      # Type checking with mypy  
make lint           # Run format and typecheck together
make clean          # Clean generated files and build artifacts

# Examples and demos
make example        # Run basic demo
make ufc-explore    # UFC analytics demonstration in examples/ufc/
```

#### Specific Test Commands
```bash
uv run python -m pytest                              # Run all tests
uv run python -m pytest tests/test_pandas_executor.py  # Run specific test file
uv run python -m pytest --cov=src                   # Run with coverage reporting
uv run python -m pytest -v                          # Verbose test output
uv run python -m pytest -m "not slow"               # Skip slow tests
```

#### UFC Example Commands
```bash
cd examples/ufc                                     # Navigate to UFC example
uv sync                                             # Install UFC example dependencies
uv run python explore.py                           # Run UFC data exploration
uv run python title_fight_analysis.py              # Run semantic model example
```

## Project Structure

```
copper/
├── src/                       # Main Python package (source code)
│   ├── __init__.py            # Package entry point with load() and Query() exports
│   ├── parser/                # ANTLR-based expression parser
│   │   ├── antlr_parser.py    # Main parser implementation with CopperParser class
│   │   └── ast_nodes.py       # AST node definitions using visitor pattern
│   ├── semantic/              # YAML schema and semantic model
│   │   ├── schema.py          # Pydantic model definitions (SemanticModel, Dimension, Measure)
│   │   └── loader.py          # YAML model loader with relationship parsing
│   ├── query/                 # Query builder and planning
│   │   └── builder.py         # Fluent query API with to_pandas() and to_sql() methods
│   └── executors/             # Execution engines
│       ├── pandas_executor.py # Pandas backend with AST visitor code generation
│       └── sql_generator.py   # Universal SQL generation with dialect support
├── grammar/
│   └── Copper.g4              # ANTLR grammar definition for DAX-like expressions
├── tests/                     # Python test suite with pytest
│   ├── test_semantic_model.py # YAML validation and loading tests
│   ├── test_query_builder.py  # Query API functionality tests
│   ├── test_pandas_executor.py # Pandas execution engine tests
│   └── test_sql_generator.py  # SQL generation tests
├── examples/                  # Example projects and real data
│   └── ufc/                   # UFC/MMA analytics with semantic models
│       ├── ufc_fights_all.csv # Real UFC fight dataset (7812 fights)
│       ├── fight_analysis.yaml # Complete semantic model with measures
│       ├── explore.py         # UFC data exploration script
│       ├── title_fight_analysis.py # Semantic model usage example
│       └── pyproject.toml     # UFC example dependencies
├── pyproject.toml             # Modern Python project configuration
├── uv.lock                    # Dependency lock file
├── Makefile                   # Build automation with uv integration
├── README.md                  # Main project documentation
└── CLAUDE.md                  # This file
```

## Architecture Overview

Copper implements a **4-layer architecture** transforming YAML semantic models into executable code:

### 1. Semantic Layer (`src/semantic/`)
- **Purpose**: YAML model definitions and validation
- **Key Files**: `schema.py` (Pydantic models), `loader.py` (YAML loading)
- **Data Flow**: YAML files → Pydantic validation → SemanticModel objects

### 2. Parser Layer (`src/parser/`)
- **Purpose**: ANTLR-based DAX expression parsing 
- **Key Files**: `antlr_parser.py` (CopperParser), `ast_nodes.py` (AST definitions)
- **Data Flow**: Expression strings → ANTLR parse tree → Typed AST nodes

### 3. Query Layer (`src/query/`)
- **Purpose**: Fluent query building API
- **Key Files**: `builder.py` (Query class with chainable methods)
- **Data Flow**: Fluent API calls → Query objects → Execution delegation

### 4. Execution Layer (`src/executors/`)
- **Purpose**: Multi-engine code generation using visitor pattern
- **Key Files**: `pandas_executor.py` (Pandas code gen), `sql_generator.py` (SQL gen)
- **Data Flow**: AST + Query → Engine-specific code → Results

### Core Design Patterns
- **Visitor Pattern**: AST nodes accept visitors for multi-engine code generation
- **Strategy Pattern**: Different execution engines (Pandas, SQL) with common interface
- **Fluent Interface**: Query builder methods return `self` for method chaining
- **Pydantic Validation**: Type-safe semantic model definitions with automatic validation

## UFC Analytics Example

The UFC example demonstrates real-world usage with actual MMA fight data:

### Dataset Overview
- **File**: `examples/ufc/ufc_fights_all.csv` (7,812 fights from UFC 1 to present)
- **Semantic Model**: `examples/ufc/fight_analysis.yaml` 
- **Key Measures**: `title_fight_count`, `finish_rate`, `knockout_rate`, `submission_rate`

### Working with UFC Data
```python
# Load UFC semantic model and data
import pandas as pd
import yaml

# Load the semantic model
with open('examples/ufc/fight_analysis.yaml') as f:
    model = yaml.safe_load(f)

# Load the dataset  
df = pd.read_csv('examples/ufc/ufc_fights_all.csv')

# Calculate title fight count (from semantic model expression)
title_fight_count = df[df['title_fight'] == True].shape[0]  # Result: 302 title fights
```

### Semantic Model Structure
```yaml
# examples/ufc/fight_analysis.yaml
dimensions:
  weight_class:
    expression: ufc_fights.weight_class
    type: string
  
  is_title_fight:
    expression: ufc_fights.title_fight
    type: boolean

measures:
  title_fight_count:
    expression: COUNT(ufc_fights.fight_id WHERE ufc_fights.title_fight = true)
    type: number
    
  finish_rate:
    expression: COUNT(ufc_fights.fight_id WHERE ufc_fights.method != "Decision") / COUNT(ufc_fights.fight_id) * 100
    type: number
    format: "%.1f%%"
```

## Key Dependencies

### Python Libraries
- **antlr4-python3-runtime**: Expression parsing (>=4.9.0)
- **pyyaml**: YAML file processing (>=6.0)
- **pandas**: Data manipulation and analysis (>=1.3.0)
- **pydantic**: Data validation and parsing (>=1.8.0)

### Development Tools
- **uv**: Fast Python package manager and environment manager
- **pytest**: Testing framework (>=6.0)
- **black**: Code formatting (>=21.0)
- **mypy**: Type checking (>=0.910)
- **Java 8+**: Required for ANTLR parser generation

### Optional Extensions
- **sqlalchemy**: SQL execution support (>=1.4.0)
- **apache-beam**: Streaming analytics (>=2.0.0)

## Testing Strategy

### Test Configuration
- **Framework**: pytest with coverage reporting
- **Configuration**: `pyproject.toml` with markers for slow/integration tests
- **Coverage**: Source coverage tracking with generated file exclusions

### Test Execution
```bash
make test                     # Run all tests via Makefile (recommended)
uv run python -m pytest      # Direct pytest execution
uv run python -m pytest --cov=src  # With coverage reporting
uv run python -m pytest -v   # Verbose output
uv run python -m pytest tests/test_pandas_executor.py  # Specific test file
```

The test suite includes:
- **Parser validation**: Expression parsing and AST generation
- **Semantic model loading**: YAML validation and relationship parsing
- **Query execution**: End-to-end Pandas and SQL generation workflows
- **Real data testing**: UFC analytics with actual MMA datasets

## Prerequisites & Setup

### Required Tools
- **Python 3.8+** with modern features support
- **uv package manager** (replaces pip/poetry for faster dependency management)
- **Java 8+** for ANTLR parser generation
- **ANTLR 4.13.2** complete JAR (downloaded automatically by Makefile)

### Setup Process
```bash
# 1. Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Sync dependencies from lock file
make sync

# 3. Install development dependencies
make dev-install

# 4. Generate ANTLR parser (requires Java)
make parser

# 5. Verify installation with tests
make test
```

### Important Notes
- The project uses **uv** instead of pip for dependency management
- All Python commands should run through `uv run python` for proper environment isolation
- ANTLR parser generation creates files in `copper/parser/generated/` (path inconsistency noted)
- The project uses `src/` layout with package discovery via `pyproject.toml`

## Common Development Tasks

### Working with Semantic Models
```bash
# Validate YAML semantic models
uv run python -c "
import yaml
from src.semantic.loader import load_from_file
model = load_from_file('examples/ufc/fight_analysis.yaml')
print(f'Loaded model: {model.name}')
"

# Explore UFC data directly
cd examples/ufc
uv run python explore.py
```

### Parser Development
```bash
# Regenerate ANTLR parser after grammar changes
make parser

# Test expression parsing manually
uv run python -c "
from src.parser.antlr_parser import CopperParser
parser = CopperParser()
ast = parser.parse('SUM(Orders.total_amount)')
print(ast)
"
```

### Code Quality
```bash
# Format code and run type checking
make lint

# Individual quality checks
make format        # Black code formatting
make typecheck     # MyPy type checking
```

## Expression Language Features

The DAX-like expression syntax supports:

### Aggregation Functions
- Standard aggregations: `COUNT()`, `SUM()`, `AVG()`, `MIN()`, `MAX()`
- Filter contexts: `COUNT(Orders.id WHERE Orders.status = "shipped")`

### Conditional Logic
- Conditional expressions: `IF(condition, value1, value2)`
- Multi-way conditionals: `SWITCH()`, `CASE WHEN ... THEN ... ELSE`

### Boolean and Arithmetic Operations
- Boolean operators: `AND`, `OR`, `NOT`
- Comparison operators: `=`, `<>`, `<`, `>`, `<=`, `>=`
- Arithmetic operators: `+`, `-`, `*`, `/`

### Column References
- Table-qualified: `fight_results.weight_class`
- Unqualified: `weight_class` (resolved via context)

## Architecture Notes

### Expression Execution Flow
1. **YAML Loading**: Pydantic validates semantic models (`src/semantic/loader.py:10-18`)
2. **Query Building**: Fluent API constructs query objects (`src/query/builder.py:7-17`)
3. **Expression Parsing**: ANTLR converts expressions to AST (`src/parser/antlr_parser.py:18-54`)
4. **Code Generation**: Visitor pattern generates engine-specific code (`src/executors/`)
5. **Execution**: Engine executes generated code and returns results

### Multi-Engine Support
- **Pandas Executor**: Direct DataFrame operations for in-memory data (`src/executors/pandas_executor.py`)
- **SQL Generator**: Universal SQL output for any dialect (`src/executors/sql_generator.py`)
- **Extensible Design**: New engines can be added by implementing the visitor interface

### Data Join Resolution
- Automatic relationship traversal based on semantic model definitions
- Support for star/snowflake schema patterns
- Join logic implemented in both Pandas and SQL execution engines