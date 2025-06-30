# Copper - Universal Semantic Layer

## Project Overview

**Copper is a portable semantic layer that compiles metric definitions and queries into runtime code across multiple engines.** The project motto is "Define Once. Run Anywhere. ☄️"

This is a complex multi-language project that implements a DAX-like expression language parser and semantic modeling system with support for multiple execution engines (Pandas, Spark, SQL, Apache Beam).

## Current State

✅ **Current Status**: The project has been rebuilt with a focused UFC analytics example implementation. The current branch `ui/barebones` contains:
- Complete Python semantic layer implementation using src/ layout
- ANTLR4 grammar for DAX-like expressions (`grammar/Copper.g4`)
- Comprehensive UFC analytics example with real MMA data
- YAML-based semantic modeling with Pydantic validation
- Query builder API with Pandas execution engine
- Full test suite and development utilities
- Comprehensive schema reference documentation

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
- **Pandas**: Primary implementation with groupby, agg, join operations
- **SQL Generation**: PostgreSQL dialect with support for additional dialects planned
- **Apache Beam**: Streaming analytics with windowing (planned)

### Developer Experience
- **Web Studio**: Visual interface for model development
- **Validation**: Real-time expression and schema validation
- **Auto-complete**: YAML schema assistance
- **Error handling**: Detailed error messages and suggestions

## Development Workflow

### Build Commands
```bash
# Install dependencies
pip install -e .

# Generate ANTLR parser (requires Java)
make parser

# Run tests
pytest

# Run UFC analytics demo
python examples/ufc_demo.py

# Format code
make format

# Type checking
make typecheck

# Clean generated files
make clean
```

### Current Project Structure
```
copper/
├── src/                       # Main Python package (source code)
│   ├── __init__.py            # Package entry point
│   ├── parser/                # ANTLR-based expression parser
│   │   ├── antlr_parser.py    # Python parser implementation
│   │   └── ast_nodes.py       # AST node definitions
│   ├── semantic/              # YAML schema and semantic model
│   │   ├── schema.py          # Pydantic model definitions
│   │   └── loader.py          # YAML model loader
│   ├── query/                 # Query builder and planning
│   │   └── builder.py         # Fluent query API
│   └── executors/             # Execution engines
│       └── pandas_executor.py # Pandas backend implementation
├── grammar/
│   └── Copper.g4              # ANTLR grammar definition
├── tests/                     # Comprehensive test suite
│   ├── test_semantic_model.py
│   ├── test_query_builder.py
│   └── test_pandas_executor.py
├── examples/                  # UFC analytics demonstration
│   ├── ufc/                   # UFC/MMA analytics with real data
│   │   ├── data/              # Real UFC fight datasets (CSV)
│   │   ├── datasources.yaml   # UFC data source definitions
│   │   ├── model.yaml         # MMA analytics semantic model
│   │   └── data_loader.py     # UFC data loading utilities
│   └── ufc_demo.py            # UFC analytics demonstration script
├── setup.py                   # Python package configuration
├── requirements.txt           # Python dependencies
├── pytest.ini                # Test configuration
├── Makefile                   # Build automation
├── README.md                  # Project documentation
├── SCHEMA_REFERENCE.md        # Comprehensive schema documentation
└── prd.md                     # Project requirements document
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
from examples.ufc.data_loader import UFCDataLoader

# Load real UFC data
loader = UFCDataLoader()
ufc_data = loader.load_all_data()

# Load semantic model
model = copper.load("examples/ufc/model.yaml")

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
- **Node.js 16+** with npm/yarn
- **Java 8+** for ANTLR
- **ANTLR 4.13.1** CLI tool

### Dependencies
- **Python**: pandas, pydantic, pytest, ANTLR4 runtime, PyYAML
- **Java**: ANTLR complete JAR for parser generation
- **Data**: Real UFC fight data in CSV format for demonstrations

## Testing Strategy

The project includes comprehensive testing:
- **Unit tests**: Parser validation with edge cases
- **Integration tests**: End-to-end query execution
- **Cross-engine validation**: Equivalent outputs across Pandas/Spark/SQL
- **Performance tests**: Scale testing with mock datasets

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

## Documentation

- **SCHEMA_REFERENCE.md**: Comprehensive documentation of all Copper semantic modeling components
- **README.md**: Quick start guide and project overview
- **prd.md**: Complete project requirements and roadmap
- **examples/ufc/**: Working UFC analytics demonstration with real MMA data

## Next Steps

- Implement includes functionality for modular YAML files
- Generate ANTLR parser from grammar (requires Java setup)
- Add time-series analysis capabilities for fighter career progression
- Implement multi-engine execution (Spark, SQL, Beam)
- Create advanced MMA metrics like pound-for-pound rankings