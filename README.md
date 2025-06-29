# Copper - Universal Semantic Layer ☄️

**Define Once. Run Anywhere.**

Copper is a portable semantic layer that compiles metric definitions and queries into runtime code across multiple execution engines.

## 🚀 Quick Start

```python
import src as copper

# Load semantic model from YAML
model = copper.load("examples/ecommerce/model.yaml")

# Build and execute query
query = copper.Query(model) \
    .dimensions(["region"]) \
    .measures(["revenue", "order_count"]) \
    .filters(["order_status = 'completed'"])

# Execute on Pandas (built-in mock data)
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
- **Multiple backends**: Pandas (implemented), Spark/SQL (planned)

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
│   ├── basic_demo.py          # Simple demo script
│   └── load_example.py        # File loading demonstration
└── Makefile                   # Build automation
```

## 📊 Example Models

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
    sql: customers.region
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
- Cross-engine portability (Pandas → Spark)
- Expression validation and optimization

### 3. Analytics Engineering
- Metric definitions as code
- Version control for business logic
- Automated testing of calculations

## 🧪 Examples

### Basic Aggregation
```python
import src as copper

# Create semantic model
model_def = {
    'name': 'sales',
    'dimensions': {
        'region': {'sql': 'customers.region', 'type': 'string'}
    },
    'measures': {
        'revenue': {'expression': 'SUM(orders.total_amount)', 'type': 'currency'}
    }
}

model = copper.SemanticModelLoader.load_from_dict(model_def)
query = copper.Query(model).dimensions(['region']).measures(['revenue'])
result = query.to_pandas(data_source)
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
- [ ] Spark execution engine
- [ ] SQL generation (BigQuery, PostgreSQL)
- [ ] Apache Beam streaming support

### Phase 3: Developer Experience 📋
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

**Copper** - Making data semantics portable across the modern data stack.