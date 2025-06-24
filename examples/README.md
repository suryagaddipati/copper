# Copper Language Examples

This directory contains example `.copper` files demonstrating the Copper language syntax for metadata-driven data modeling.

## Working Examples

The following examples demonstrate syntax that currently works with the parser:

### Simple Views

- **`simple_sales_view.copper`** - Basic view with `from` clause
- **`ecommerce_base_view.copper`** - Simple e-commerce base view  
- **`product_catalog_view.copper`** - Product catalog view
- **`customer_analysis_view.copper`** - Customer analysis view

### Example Usage

```copper
# Basic view syntax that works
view: simple_sales {
  from: orders
}
```

## Comprehensive Examples (Syntax Reference)

The following files demonstrate the intended full Copper syntax based on the specification, though they may not parse correctly with the current parser implementation:

### Models

- **`customers.copper`** - Customer data model with dimensions and measures
- **`ecommerce_orders.copper`** - E-commerce orders model with comprehensive analytics
- **`products.copper`** - Product catalog model with inventory metrics
- **`inventory_management.copper`** - Inventory tracking and forecasting model

### Views

- **`sales_analysis_view.copper`** - Complex view with multiple joins
- **`base_ecommerce_view.copper`** - Base view with inheritance pattern
- **`customer_analytics_view.copper`** - Customer behavior analysis view

### Model Example Structure

```copper
model: example {
  dimension: field_name {
    type: string
    expression: Table[Field] ;;
    label: "Display Name"
    description: "Field description"
  }
  
  measure: metric_name {
    type: sum
    expression: SUM(Table[Amount]) ;;
    value_format: usd
    label: "Total Amount"
  }
}
```

### View Example Structure

```copper
view: example_view {
  from: base_model
  
  join: related_model {
    type: left_outer
    relationship: many_to_one
    expression: BaseModel[ID] = RelatedModel[BaseID] ;;
  }
}
```

## Current Parser Limitations

The current ANTLR parser implementation has some limitations:

1. **DAX Expressions**: Complex DAX expressions may not parse correctly
2. **Model Definitions**: Full model syntax with dimensions and measures may have parsing issues
3. **Join Expressions**: Views with join expressions may not parse correctly
4. **Parameter Syntax**: Some parameter combinations may cause parser errors

## Testing Examples

To test example files with the parser:

```bash
# Test a specific example
make test

# Or test manually
cd app/api
python3 -c "
from antlr_parser import validate_copper_syntax
with open('../../examples/simple_sales_view.copper', 'r') as f:
    result = validate_copper_syntax(f.read())
print(f'Valid: {result[\"valid\"]}')
print(f'Errors: {result[\"errors\"]}')
"
```

## Syntax Guidelines

Based on current parser capabilities:

1. **Use simple view syntax** for working examples
2. **Avoid complex DAX expressions** until parser is improved
3. **Test syntax changes** with the parser before committing
4. **Refer to specification** (`spec/SPECIFICATION.md`) for intended full syntax

## Future Improvements

- Enhanced DAX expression parsing
- Complete model definition support
- View inheritance and complex joins
- Better error messages and recovery
- VS Code extension with syntax highlighting