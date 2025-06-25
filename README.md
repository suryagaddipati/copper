# Copper: A LookML-inspired data modeling language using DAX

**Copper** is a metadata format for describing data dimensions and measures, inspired by LookML but using DAX expressions instead of SQL. This provides better compatibility with modern data processing tools like Spark and Dataflow.

**[Read the Specification](spec/SPECIFICATION.md)** | **[View Examples](examples/)** | **[Parser Documentation](grammar/README.md)**

---

## What is Copper?

Copper is a data modeling language that combines the familiar, easy-to-read syntax of LookML with the powerful analytical capabilities of DAX (Data Analysis Expressions). It is designed to work with modern, distributed data processing environments like Apache Spark and Google Dataflow, and it provides native support for tools like Power BI and Tableau.

By using DAX, Copper allows you to define complex business logic and time-series analysis in a way that is both expressive and compatible with a wide range of data platforms.

## Core Features

*   **LookML-inspired Syntax:** A familiar, easy-to-learn syntax for defining data models.
*   **DAX Expressions:** Use the full power of DAX for complex calculations and analysis.
*   **Time Intelligence:** Built-in functions for time-based analysis, such as `SAMEPERIODLASTYEAR` and `TOTALYTD`.
*   **Context Awareness:** Automatic relationship traversal between tables.
*   **View Inheritance:** An extensible, modular design that allows you to reuse code and build on existing models.
*   **Multi-language Parsers:** The ANTLR4 grammar can be used to generate parsers for over 8 programming languages.
*   **dbt Integration:** Reference Copper views in your dbt models as compiled SQL.

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

### 3. Integrate with dbt

```sql
-- models/vip_customers.sql
{{ config(materialized='table') }}

select * from {{ copper.ref('customer_analytics') }}
where customer_tier = 'VIP'
  and total_spent > 10000
```



## Tooling

Copper includes a comprehensive ANTLR4 grammar that can be used to generate parsers for a variety of languages. See the [Grammar Documentation](grammar/README.md) for more information.

## Contributing

Copper is open source and welcomes contributions. Please see the [Contributing Guide](CONTRIBUTING.md) to get started.

## License

MIT License
