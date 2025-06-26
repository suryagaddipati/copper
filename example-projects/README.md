# Copper Example Projects

This directory contains organized example projects demonstrating the Copper language syntax for metadata-driven data modeling.

## Project Structure

Each subdirectory represents a complete project with related Copper files:

### 📚 `basic-tutorial/`
**Learning Copper basics**
- `minimal.copper` - Minimal model definition
- `simple.copper` - Simple model with DAX expressions

Perfect for getting started with Copper syntax and understanding basic model definitions.

### 🛒 `ecommerce-demo/`
**Complete e-commerce semantic layer**
- `customers.copper` - Customer demographics model
- `complete_example.copper` - Product model with analytics view
- `orders_view.copper` - Order view definitions
- `with_expressions.copper` - Advanced DAX expression examples

Shows how to build a realistic semantic layer for an e-commerce business with multiple related models and views.

### 🥊 `ufc-analytics/`
**Real-world analytics with sample data**
- `ufc_fighters.copper` - Fighter demographics and performance
- `ufc_fights.copper` - Fight outcomes and methods
- `ufc_events.copper` - Event venues and dates
- `ufc_analytics.copper` - Analytics views with complex joins
- `create_ufc_data.py` - Sample data generator
- `ufc_sample.db` - DuckDB database with sample data

Demonstrates a complete analytics use case with complex joins, measures, and actual sample data for testing.

## Using with Copper Studio

### Load as Projects
1. Start Copper Studio: `make dev`
2. Go to http://localhost:3000
3. Click "Projects" tab
4. Load project path: `/path/to/copper/example-projects/basic-tutorial`
5. Open the project and explore the files

### Work with Sample Data
For the UFC analytics project:
1. Load the `ufc-analytics` project
2. Use Database Explorer to connect to `ufc_sample.db`
3. Generate SQL from the Copper views
4. Execute queries against the sample data

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