# Copper - Universal Semantic Layer

## Project Overview

**Copper is a portable semantic layer that compiles metric definitions and queries into runtime code across multiple engines.** The project motto is "Define Once. Run Anywhere. ☄️"

This is a complex multi-language project that implements a DAX-like expression language parser and semantic modeling system with support for multiple execution engines (Pandas, Spark, SQL, Apache Beam).

## Current State

⚠️ **Important**: The codebase was recently stripped down (commit `079fa45 remove everything`). The current branch `ui/barebones` contains only:
- `prd.md` - Comprehensive project requirements document
- `studio/.next/` - Next.js build artifacts from the previous web interface
- `.claude/settings.local.json` - Claude configuration with extensive permissions
- `.gitignore` - Multi-language ignore patterns

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
- **Spark**: Planned distributed processing support  
- **SQL**: BigQuery dialect code generation
- **Apache Beam**: Streaming analytics with windowing

### Developer Experience
- **Web Studio**: Visual interface for model development
- **Validation**: Real-time expression and schema validation
- **Auto-complete**: YAML schema assistance
- **Error handling**: Detailed error messages and suggestions

## Development Workflow

### Build Commands (from historical Makefile)
```bash
# Generate ANTLR parser
make generate-parser

# Build web interface
cd studio && npm run dev

# Run API server
cd api && python main.py

# Run tests
python -m pytest tests/

# Start full development environment
./start.sh  # or ./start-manual.sh
```

### Current Project Structure
```
copper/
├── src/                       # Main Python package (source code)
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
├── examples/                  # Example models and demos
│   ├── basic_demo.py          # Working demo script
│   ├── ecommerce.copper       # Ecommerce semantic model
│   └── saas_metrics.copper    # SaaS business metrics model
├── setup.py                   # Python package configuration
├── requirements.txt           # Python dependencies
├── pytest.ini                # Test configuration
└── Makefile                   # Build automation
```

## Use Cases & Examples

### Basic Aggregation
```yaml
measures:
  revenue:
    expression: SUM(Orders.total_amount)
    type: number

dimensions:
  region:
    sql: Customers.region
    type: string
```

```python
import src as copper
model = copper.load("model.yaml")
query = copper.Query(model).dimensions(["region"]).measures(["revenue"])
df = query.to_pandas()
```

### Conditional Logic
```yaml
measures:
  is_premium:
    expression: IF(Customers.tier = "Gold", 1, 0)
    type: number
```

### Relationships & Joins
```yaml
relationships:
  Orders.customer_id → Customers.id

dimensions:
  customer_region:
    sql: Customers.region
    type: string
```

## Development Environment Setup

### Prerequisites
- **Python 3.8+** with pip
- **Node.js 16+** with npm/yarn
- **Java 8+** for ANTLR
- **ANTLR 4.13.1** CLI tool

### Dependencies
- **Python**: FastAPI, pandas, pytest, ANTLR4 runtime
- **Node.js**: Next.js, React, Monaco Editor, Tailwind CSS
- **Java**: ANTLR complete JAR for parser generation

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

## Recovery Notes

To restore the project from the current bare state, you would need to:
1. Check out the commit before "remove everything" (`8b56a55`)
2. Restore the full directory structure
3. Reinstall dependencies (Python packages, npm modules)
4. Regenerate ANTLR parsers
5. Rebuild the Next.js application

The comprehensive `.gitignore` and build configurations suggest this was a mature, production-ready development environment before the recent reset.