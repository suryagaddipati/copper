# Copper

A metadata format for describing data dimensions and measures, inspired by LookML but using DAX expressions instead of SQL. This provides better compatibility with modern data processing tools like Spark and Dataflow.

## Why Copper?

### Built for Modern Data Stacks
Copper uses DAX expressions that work well with distributed computing environments:
- **Apache Spark** - Better compatibility with Spark's distributed processing
- **Google Dataflow** - Works with stream and batch processing pipelines
- **Azure Data Factory** - Integrates with Microsoft's data platform
- **Power BI & Tableau** - Native DAX support
- **dbt** - Reference Copper views in dbt models as compiled SQL

### LookML Syntax with DAX Expressions
Familiar LookML syntax combined with DAX's analytical capabilities:

```copper
model: sales_performance {
  measure: revenue_growth {
    type: number
    expression: 
      VAR CurrentRevenue = SUM(Orders[Amount])
      VAR PreviousRevenue = CALCULATE(
        SUM(Orders[Amount]),
        DATEADD(Orders[OrderDate], -1, YEAR)
      )
      RETURN DIVIDE(CurrentRevenue - PreviousRevenue, PreviousRevenue) ;;
    value_format: "0.0%"
  }
}
```

### Key Features

- **Time Intelligence** - Built-in functions like `SAMEPERIODLASTYEAR`, `TOTALYTD`
- **Context Awareness** - Automatic relationship traversal between tables
- **Measure Calculations** - Simple, readable aggregation syntax
- **Filter Context** - Intuitive filtering with `CALCULATE()` function

### Developer Experience

- **Familiar Syntax** - LookML-inspired structure
- **Multi-Language Parsers** - ANTLR4 grammar generates parsers for 8+ languages
- **Rich Examples** - Production-ready models included
- **Extensible** - View inheritance and modular design
- **Type Safe** - Comprehensive validation rules

### Enterprise Features

#### Performance at Scale
```copper
# Complex time-series analysis
measure: rolling_cohort_retention {
  type: number
  expression:
    AVERAGEX(
      SUMMARIZE(
        FILTER(Orders, Orders[OrderDate] >= DATE(2023,1,1)),
        Orders[CustomerCohort],
        "CohortRevenue", CALCULATE(SUM(Orders[Amount]))
      ),
      [CohortRevenue]
    ) ;;
}
```

#### Governance & Compliance
- **Centralized Definitions** - Single source of truth for business metrics
- **Audit Trail** - Version control for all metric definitions
- **Consistent Logic** - Reusable calculations across teams
- **Self-Documenting** - Built-in labels and descriptions

## Example

```copper
measure: customer_lifetime_value {
  type: number
  expression: 
    AVERAGEX(
      VALUES(Orders[CustomerID]),
      CALCULATE(SUM(Orders[Amount]))
    ) ;;
  value_format: usd
  label: "Customer Lifetime Value"
}
```

## Getting Started

### 1. Define Your Models
```copper
model: customers {
  dimension: customer_tier {
    type: tier
    expression: SWITCH(
      TRUE(),
      RELATED(Customers[TotalSpent]) > 10000, "VIP",
      RELATED(Customers[TotalSpent]) > 1000, "Premium",
      "Standard"
    ) ;;
    tiers: ["Standard", "Premium", "VIP"]
  }
  
  measure: lifetime_value {
    type: sum
    expression: Customers[TotalSpent] ;;
    value_format: usd
  }
}
```

### 2. Create Views
```copper
view: customer_analytics {
  from: customers
  
  join: orders {
    type: left_outer
    relationship: one_to_many
    expression: Customers[CustomerID] = Orders[CustomerID] ;;
  }
  
  join: products {
    type: inner
    relationship: many_to_one
    expression: Orders[ProductID] = Products[ProductID] ;;
  }
}
```

### 3. Use View Inheritance
```copper
view: base_sales {
  extension: required
  from: orders
  
  join: customers {
    type: left_outer
    relationship: many_to_one
    expression: Orders[CustomerID] = Customers[CustomerID] ;;
  }
}

view: retail_sales {
  extends: [base_sales]
  
  join: stores {
    type: left_outer
    relationship: many_to_one
    expression: Orders[StoreID] = Stores[StoreID] ;;
  }
}
```

### 4. Integrate with dbt
```sql
-- models/vip_customers.sql
{{ config(materialized='table') }}

select * from {{ copper.ref('customer_analytics') }}
where customer_tier = 'VIP'
  and total_spent > 10000
```

```yaml
# dbt_project.yml
on-run-start:
  - "{{ copper.compile_views() }}"

vars:
  copper:
    source_path: "copper/"  # Git submodule
    target_path: "target/copper_compiled/"
```

## Benefits by Role

### Data Engineers
- Better compatibility with distributed computing frameworks
- DAX expressions work well with modern data platforms
- Reduced complexity in metric definition and maintenance

### Analytics Engineers
- More concise expression of complex business logic
- Built-in time intelligence and context-aware calculations
- Familiar syntax with powerful analytical capabilities

### Business Users
- Self-documenting models with clear business terminology
- Readable metric definitions that match business concepts
- Consistent logic across different tools and reports

## Roadmap

### Parser & Tooling
- [x] **ANTLR4 Grammar** - Multi-language parser generation (Java, Python, JS, C#, Go, C++, Swift)
- [x] **Build System** - Automated parser generation for all supported languages
- [ ] **VS Code Extension** - Syntax highlighting, autocomplete, validation
- [ ] **CLI Tools** - Copper compiler, validator, and formatter
- [ ] **dbt Integration** - Reference Copper views in dbt models via git submodules
- [ ] **Looker Migration** - Automated LookML → Copper converter

### Future Plans
- [ ] **Live Compilation** - Real-time DAX → SQL/Spark translation
- [ ] **Semantic Layer API** - REST/GraphQL interface for metrics
- [ ] **Multi-dialect Support** - Target multiple execution engines
- [ ] **ML Integration** - Built-in support for predictive metrics

## Parser & Tools

Copper includes a comprehensive ANTLR4 grammar that generates parsers for multiple programming languages:

### Supported Languages
- **Java** - Enterprise applications, Spring Boot services
- **Python** - Data science, analytics, web APIs
- **JavaScript/TypeScript** - Web applications, Node.js services
- **C#** - .NET applications, Azure functions
- **Go** - Cloud services, microservices
- **C++** - High-performance applications
- **Swift** - iOS/macOS applications

### Quick Start

```bash
# Navigate to grammar directory
cd grammar

# Generate parsers for all languages
./build.sh generate

# Or generate specific languages
./build.sh generate java python javascript

# Test against example files
./build.sh test
```

See [Grammar Documentation](grammar/README.md) for detailed usage instructions.

## Contributing

Copper is open source and welcomes contributions:
- **Reporting bugs**
- **Suggesting features** 
- **Building tools**
- **Improving documentation**

Check out our [Contributing Guide](CONTRIBUTING.md) to get started.

## License

MIT License - see [LICENSE](LICENSE) for details.

---

**[Read the Specification](spec/SPECIFICATION.md)** | **[View Examples](examples/)** | **[Parser Documentation](grammar/README.md)** | **[Grammar Files](grammar/)**