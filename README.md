# Copper: Semantic Layer for Modern Data Platforms

**Copper** is a semantic layer that defines business logic and metrics using DAX expressions. It provides a unified interface for data modeling that works across modern data platforms and BI tools.

**[View Examples](examples/)** | **[Parser Documentation](grammar/README.md)** | **[Studio Interface](studio/)**

---

## What is Copper?

Copper is a semantic layer that bridges the gap between raw data and business insights. It uses familiar modeling concepts with DAX expressions to define reusable business logic as code.

Key benefits:
- **Universal compatibility** with any data platform or BI tool
- **Business logic centralization** - define metrics once, use everywhere  
- **DAX expressions** for complex calculations and time intelligence
- **Platform agnostic** - not tied to any specific query engine

## Core Features

*   **Semantic Models:** Define dimensions, measures, and business logic once
*   **DAX Expressions:** Full power of DAX for calculations and time intelligence  
*   **View Composition:** Build complex data models through joins and relationships
*   **Studio Interface:** Web-based development environment
*   **Multi-platform Parser:** ANTLR4 grammar supports multiple programming languages
*   **Platform Agnostic:** Works with any data platform or BI tool
*   **Code-First:** Version control friendly metadata definitions

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
}
```

### 3. Use Anywhere

Copper definitions can be consumed by:
- BI tools (Power BI, Tableau, Looker)
- Data platforms (Spark, Snowflake, BigQuery) 
- Applications (via generated code)
- Analytics frameworks (dbt, Malloy, etc.)



## Studio Development Environment

Copper includes a web-based development studio for building and testing semantic models:

```bash
# Start the development environment
make dev

# Access the studio at http://localhost:3000
# API available at http://localhost:8000
```

## Architecture

- **Parser:** ANTLR4-based grammar for Copper language parsing
- **Semantic Layer:** Business logic and metric definitions
- **Studio:** React-based development interface  
- **API:** FastAPI backend for live parsing and validation
- **Generators:** Output for data processing platforms (SQL, Spark, Dataflow)

## License

MIT License
