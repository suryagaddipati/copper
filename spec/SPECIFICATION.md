# Copper Language Specification

Copper is a metadata format for describing data dimensions and measures, inspired by LookML but using DAX expressions instead of SQL. This provides better compatibility with modern data processing tools like Spark and Dataflow.

## Overview

Copper consists of two main constructs:
- **Models**: Define data structure with dimensions and measures
- **Views**: Define how to query and join models together

## Models

Models define the structure of your data using dimensions and measures.

### Basic Model Syntax

```copper
model: model_name {
  dimension: dimension_name {
    type: dimension_type
    expression: DAX_EXPRESSION ;;
    # Optional parameters
  }
  
  measure: measure_name {
    type: measure_type  
    expression: DAX_EXPRESSION ;;
    # Optional parameters
  }
}
```

### Dimension Types

| Type | Description | Example |
|------|-------------|---------|
| `string` | Text values (default) | Customer names, categories |
| `number` | Numeric values | Prices, quantities |
| `date` | Date values | Order dates, birth dates |
| `date_time` | DateTime values | Timestamps, created_at |
| `yesno` | Boolean values | Is active, has discount |
| `tier` | Categorical buckets | Age groups, revenue tiers |
| `location` | Geographic coordinates | Store locations |
| `zipcode` | Postal codes | Shipping addresses |
| `distance` | Distance measurements | Shipping distance |

### Measure Types

| Type | Description | DAX Example |
|------|-------------|-------------|
| `count` | Count of records | `COUNTROWS(Orders)` |
| `sum` | Sum of values | `SUM(Orders[Amount])` |
| `average` | Average of values | `AVERAGE(Orders[Amount])` |
| `min` | Minimum value | `MIN(Orders[Amount])` |
| `max` | Maximum value | `MAX(Orders[Amount])` |
| `count_distinct` | Count unique values | `DISTINCTCOUNT(Orders[CustomerID])` |
| `median` | Median value | `MEDIAN(Orders[Amount])` |
| `number` | Custom calculation | Complex DAX expressions |

### Dimension Parameters

- `type`: Dimension type (required)
- `expression`: DAX expression (required)
- `primary_key`: Mark as primary key (`yes`/`no`)
- `value_format`: Display format (e.g., `"$#,##0.00"`, `usd`, `"0.0%"`)
- `label`: Display name for UI
- `description`: Help text
- `hidden`: Hide from UI (`yes`/`no`)

### Measure Parameters

- `type`: Measure type (required)
- `expression`: DAX expression (required)
- `value_format`: Display format (e.g., `usd`, `"0.0%"`, `"#,##0"`)
- `label`: Display name for UI
- `description`: Help text
- `hidden`: Hide from UI (`yes`/`no`)

### Example Model

```copper
model: orders {
  dimension: order_id {
    type: string
    expression: Orders[OrderID] ;;
    primary_key: yes
    label: "Order ID"
  }
  
  dimension: order_date {
    type: date
    expression: Orders[OrderDate] ;;
    label: "Order Date"
  }
  
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
  
  dimension: is_weekend_order {
    type: yesno
    expression: WEEKDAY(Orders[OrderDate]) IN {1, 7} ;;
    label: "Weekend Order"
  }
  
  measure: total_orders {
    type: count
    expression: Orders[OrderID] ;;
    label: "Total Orders"
  }
  
  measure: total_revenue {
    type: sum
    expression: Orders[Amount] ;;
    value_format: usd
    label: "Total Revenue"
  }
  
  measure: avg_order_value {
    type: average
    expression: Orders[Amount] ;;
    value_format: usd
    label: "Average Order Value"
  }
  
  measure: unique_customers {
    type: count_distinct
    expression: Orders[CustomerID] ;;
    label: "Unique Customers"
  }
  
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
    label: "Revenue Growth YoY"
  }
}
```

## Views

Views define how to query models and combine them through joins.

### Basic View Syntax

```copper
view: view_name {
  from: base_model_name
  
  join: joined_model_name {
    type: join_type
    relationship: relationship_type
    expression: DAX_JOIN_CONDITION ;;
  }
}
```

### Join Types

| Type | Description |
|------|-------------|
| `left_outer` | Left outer join (default) |
| `inner` | Inner join |
| `full_outer` | Full outer join |
| `cross` | Cross join |

### Relationship Types

| Type | Description | Example |
|------|-------------|---------|
| `one_to_one` | Each row matches one row | User to UserProfile |
| `many_to_one` | Many rows match one row | Orders to Customer |
| `one_to_many` | One row matches many rows | Customer to Orders |
| `many_to_many` | Many rows match many rows | Students to Classes |

### View Parameters

- `from`: Base model name (required)
- `extends`: List of views to inherit from
- `extension`: Mark as template (`required`)

### Join Parameters

- `type`: Join type (defaults to `left_outer`)
- `relationship`: Relationship type (defaults to `many_to_one`)  
- `expression`: DAX join condition (required)

### View Inheritance

Views can extend other views to promote code reuse:

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

### Example View

```copper
view: sales_analysis {
  from: orders
  
  join: customers {
    type: left_outer
    relationship: many_to_one
    expression: Orders[CustomerID] = Customers[CustomerID] ;;
  }
  
  join: products {
    type: inner
    relationship: many_to_one
    expression: Orders[ProductID] = Products[ProductID] ;;
  }
  
  join: order_items {
    type: left_outer
    relationship: one_to_many
    expression: Orders[OrderID] = OrderItems[OrderID] ;;
  }
}
```

## DAX Expression Guidelines

### Basic DAX Syntax

DAX expressions in Copper follow standard DAX syntax:

- **Column references**: `TableName[ColumnName]`
- **Related data**: `RELATED(TableName[ColumnName])`
- **Aggregations**: `SUM()`, `COUNT()`, `AVERAGE()`, etc.
- **Filter context**: `CALCULATE()`, `FILTER()`, etc.
- **Variables**: `VAR variableName = expression RETURN result`

### Common DAX Patterns

**Simple aggregations:**
```dax
SUM(Orders[Amount])
COUNT(Orders[OrderID])
AVERAGE(Orders[Amount])
```

**Related table data:**
```dax
RELATED(Customers[CustomerName])
RELATED(Products[Category])
```

**Conditional logic:**
```dax
IF(Orders[Amount] > 1000, "Large", "Small")
SWITCH(TRUE(), condition1, result1, condition2, result2, default)
```

**Time intelligence:**
```dax
CALCULATE(SUM(Orders[Amount]), DATEADD(Orders[OrderDate], -1, YEAR))
TOTALYTD(SUM(Orders[Amount]), Orders[OrderDate])
```

**Complex calculations:**
```dax
VAR TotalOrders = COUNT(Orders[OrderID])
VAR UniqueCustomers = DISTINCTCOUNT(Orders[CustomerID])
RETURN DIVIDE(TotalOrders, UniqueCustomers)
```

## File Organization

Copper files should use the `.copper` extension and follow these conventions:

- One model or view per file
- File names should match the model/view name
- Use lowercase with underscores: `sales_orders.copper`
- Group related models in directories

## Comments

Copper supports line comments using `#`:

```copper
# This is a comment
model: orders {
  # Another comment
  dimension: order_id {
    type: string
    expression: Orders[OrderID] ;; # Inline comment
  }
}
```

## Value Formatting

Value formatting controls how data appears in reports and dashboards.

### Named Formats

- `usd` - US Dollar ($1,234.56)
- `eur` - Euro (€1,234.56) 
- `gbp` - British Pound (£1,234.56)
- `percent_1` - Percentage with 1 decimal (12.3%)
- `percent_2` - Percentage with 2 decimals (12.34%)
- `decimal_0` - No decimals (1,234)
- `decimal_1` - One decimal (1,234.5)
- `decimal_2` - Two decimals (1,234.56)

### Custom Formats

Use Excel-style format strings:
- `"$#,##0.00"` - Currency with commas
- `"0.0%"` - Percentage with 1 decimal
- `"#,##0"` - Numbers with commas, no decimals
- `"yyyy-mm-dd"` - Date format

## Best Practices

1. **Use descriptive names** for models, views, dimensions, and measures
2. **Group related fields** logically within models
3. **Document complex DAX expressions** with comments
4. **Use consistent naming conventions** (lowercase with underscores)
5. **Leverage view inheritance** to reduce code duplication
6. **Define appropriate relationships** for accurate aggregations
7. **Use proper value formatting** for better readability
8. **Test DAX expressions** in your BI tool before adding to Copper files

## Validation Rules

1. Model and view names must be unique within a project
2. Dimension and measure names must be unique within a model
3. DAX expressions must be syntactically valid
4. Join expressions must reference valid model relationships
5. Relationship types must match actual data relationships
6. Value formats must use valid format strings or named formats