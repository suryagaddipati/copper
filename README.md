# Copper: The Universal Semantic Layer ☄️

**Define Once. Run Anywhere.**

Copper is a portable semantic layer that compiles metric definitions and queries into runtime code across multiple execution engines.

## 🚀 Quick Start

```python
import src as copper

# Load semantic model from YAML
model = copper.load("examples/ufc/model.yaml")

# Build and execute query
query = copper.Query(model) \
    .dimensions(["weight_class"]) \
    .measures(["total_fights", "finish_rate"]) \
    .filters(["finish_method = 'KO/TKO'"])

# Execute on Pandas with real UFC data
df = query.to_pandas()
print(df)
```

## 📋 Features

### ✅ Expression Language
- **DAX-like syntax** with functions: `SUM()`, `COUNT()`, `IF()`, `SWITCH()`, `CASE`
- **Boolean logic** and conditional expressions
- **Filter context**: `COUNT(Orders.id WHERE Orders.status = "shipped")`
- **Nested expressions** and function composition

### ✅ Semantic Modeling
- **YAML-based schema** for dimensions, measures, relationships
- **Type system**: string, number, currency, boolean, date types
- **Relationship modeling**: Star/snowflake schema support
- **Automatic joins** based on defined relationships

### ✅ Query Builder
- **Fluent API**: Chain `.dimensions()`, `.measures()`, `.filters()`
- **Validation**: Real-time expression and model validation
- **Multiple backends**: Pandas execution and SQL generation

### ✅ SQL Generation
- **Universal SQL**: Generate SQL from Copper expressions
- **Database portability**: Run on PostgreSQL, BigQuery, Snowflake, etc.
- **Clean output**: Readable, optimized SQL with proper formatting
- **Join automation**: Automatic JOIN generation from relationships

## 🏗️ Project Structure

```
copper/
├── src/                       # Main Python package
│   ├── parser/                # ANTLR-based expression parser
│   ├── semantic/              # YAML schema and model validation
│   ├── query/                 # Query builder and planning
│   └── executors/             # Execution engines (Pandas, Spark, etc)
├── grammar/                   # ANTLR grammar definition
├── tests/                     # Comprehensive test suite
├── examples/                  # Sample models and demos
│   ├── ecommerce/             # E-commerce analytics example
│   │   ├── datasources.yaml   # Data source definitions
│   │   └── model.yaml         # Semantic model
│   ├── saas/                  # SaaS metrics example
│   │   ├── datasources.yaml   # Data source definitions  
│   │   └── model.yaml         # Semantic model
│   ├── ufc/                   # UFC/MMA analytics with real data
│   │   ├── data/              # Real UFC fight datasets
│   │   ├── datasources.yaml   # UFC data source definitions
│   │   ├── model.yaml         # MMA analytics semantic model
│   │   └── data_loader.py     # UFC data loading utilities
│   ├── basic_demo.py          # Simple demo script
│   ├── ufc_demo.py            # UFC analytics demonstration
│   └── load_example.py        # File loading demonstration
└── Makefile                   # Build automation
```

## 📊 Example Models

### UFC/MMA Analytics (Real Data)

**Data Sources** (`examples/ufc/datasources.yaml`):
```yaml
datasources:
  fighters:
    type: table
    table: ufc_fighter_details
    description: Fighter profiles and physical attributes
    
  fight_results:
    type: table
    table: ufc_fight_results
    description: Fight outcomes and basic match information
    
  events:
    type: table
    table: ufc_events
    description: UFC event information including venues
```

**Semantic Model** (`examples/ufc/model.yaml`):
```yaml
name: ufc_analytics

includes:
  - datasources.yaml

dimensions:
  weight_class:
    expression: fight_results.weight_class
    type: string
    
  nationality:
    expression: fighters.nationality
    type: string

measures:
  total_fights:
    expression: COUNT(fight_results.fight_id)
    type: number
    
  finish_rate:
    expression: COUNT(fight_results.fight_id WHERE fight_results.method != "Decision") / COUNT(fight_results.fight_id) * 100
    type: number
    format: "%.1f%%"
```

### E-commerce Analytics

**Data Sources** (`examples/ecommerce/datasources.yaml`):
```yaml
datasources:
  orders:
    type: table
    table: orders
    database: analytics
    schema: ecommerce
    description: Customer order transactions
    
  customers:
    type: table
    table: customers
    database: analytics
    schema: ecommerce
    description: Customer master data
```

**Semantic Model** (`examples/ecommerce/model.yaml`):
```yaml
name: ecommerce_analytics

includes:
  - datasources.yaml

relationships:
  - orders.customer_id → customers.id

dimensions:
  customer_region:
    expression: customers.region
    type: string
    
measures:
  total_revenue:
    expression: SUM(orders.total_amount)
    type: currency
```

### SaaS Business Metrics

**Data Sources** (`examples/saas/datasources.yaml`):
```yaml
datasources:
  subscriptions:
    type: table
    table: subscriptions
    description: Customer subscription records
    
  users:
    type: table  
    table: users
    description: User account information
    
  # Example of other data source types
  customer_events:
    type: view
    sql: |
      SELECT customer_id, event_type, event_timestamp
      FROM raw.customer_events
    
  monthly_metrics:
    type: api
    endpoint: "https://api.company.com/metrics/monthly"
    refresh_schedule: daily
```

**Semantic Model** (`examples/saas/model.yaml`):
```yaml
name: saas_business_metrics

includes:
  - datasources.yaml

measures:
  monthly_recurring_revenue:
    expression: SUM(subscriptions.monthly_value WHERE subscriptions.status = "active")
    type: currency
    label: Monthly Recurring Revenue (MRR)
```

## 🛠️ Development

### Prerequisites
- Python 3.8+
- Java 8+ (for ANTLR parser generation)

### Setup
```bash
# Install dependencies
pip install -e .

# Generate ANTLR parser (requires Java)
make parser

# Run tests
pytest

# Run example
python examples/basic_demo.py
```

### Build Commands
```bash
# Generate parser from grammar
make parser

# Clean generated files
make clean

# Run tests with coverage
make test

# Format code
make format

# Type checking
make typecheck
```

## 🎯 Use Cases

### 1. Business Intelligence
- Define metrics once in YAML
- Query across different data sources
- Consistent calculations across teams

### 2. Data Engineering
- Semantic layer for data pipelines
- Cross-engine portability (Pandas → SQL → any database)
- Expression validation and optimization

### 3. Analytics Engineering
- Metric definitions as code
- Version control for business logic
- Automated testing of calculations

## 🧪 Examples

### UFC Fighter Analysis
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

# Execute with Pandas
result = query.to_pandas(ufc_data)
print(result)

# Or generate SQL
sql = query.to_sql()
print(sql)
```

### Basic Aggregation
```python
import src as copper

# Create semantic model
model_def = {
    'name': 'sales',
    'datasources': {
        'orders': {'type': 'table', 'table': 'orders'}
    },
    'dimensions': {
        'region': {'expression': 'customers.region', 'type': 'string'}
    },
    'measures': {
        'revenue': {'expression': 'SUM(orders.total_amount)', 'type': 'currency'}
    }
}

model = copper.SemanticModelLoader.load_from_dict(model_def)
query = copper.Query(model).dimensions(['region']).measures(['revenue'])

# Execute with Pandas
result = query.to_pandas(data_source)

# Generate SQL for any database
sql = query.to_sql()
print(sql)
# Output:
# SELECT
#   customers.region AS region,
#   SUM(orders.total_amount) AS revenue
# FROM
#   orders
#   LEFT JOIN customers
#     ON orders.customer_id = customers.id
# GROUP BY
#   customers.region
```

### SQL Generation Examples
```python
import src as copper

# Load UFC model
model = copper.load("examples/ufc/model.yaml")

# Complex query with filters
query = copper.Query(model) \
    .dimensions(['weight_class', 'nationality']) \
    .measures(['total_fights', 'finish_rate']) \
    .filters(['event_year >= 2020', 'finish_method != "Decision"'])

# Generate SQL for PostgreSQL
sql = query.to_sql(dialect="postgresql")
print(sql)

# Use the SQL with any database connection
import psycopg2
conn = psycopg2.connect("postgresql://user:pass@host/db")
result = pd.read_sql(sql, conn)
```

### Advanced Expressions
```yaml
measures:
  high_value_customers:
    expression: COUNT(DISTINCT customers.id WHERE customers.lifetime_value > 1000)
    type: number
    
  conversion_rate:
    expression: COUNT(orders.id WHERE orders.status = "completed") / COUNT(orders.id) * 100
    type: number
    format: "%.2f%%"
    
  customer_segment:
    expression: CASE
      WHEN customers.lifetime_value > 1000 THEN "High Value"
      WHEN customers.lifetime_value > 500 THEN "Medium Value"  
      ELSE "Low Value"
    type: string
```

## 🚧 Roadmap

### Phase 1: Core Foundation ✅
- [x] ANTLR expression parser
- [x] YAML semantic modeling
- [x] Pandas execution engine
- [x] Query builder API

### Phase 2: Multi-Engine Support 🚧
- [x] SQL generation (PostgreSQL dialect)
- [ ] Additional SQL dialects (BigQuery, Snowflake, etc.)
- [ ] Apache Beam streaming support

### Phase 3: Developer Experience 📋
- [ ] YAML file includes for modular models
- [ ] API and streaming data source support
- [ ] Web-based modeling interface
- [ ] Advanced validation and suggestions
- [ ] Performance optimization
- [ ] Documentation and tutorials

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make changes and add tests
4. Run the test suite: `pytest`
5. Commit changes: `git commit -m 'Add amazing feature'`
6. Push to branch: `git push origin feature/amazing-feature`
7. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙋 Support

- 📖 Documentation: See `CLAUDE.md` for detailed development notes
- 🐛 Issues: Please use the GitHub issue tracker
- 💬 Discussions: Open a GitHub discussion for questions

---

**Copper: The Universal Semantic Layer** - Making data semantics portable across the modern data stack.