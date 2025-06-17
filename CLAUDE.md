# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Copper is a metadata format for describing data dimensions and measures, inspired by LookML but using DAX expressions instead of SQL. This provides better compatibility with modern data processing tools like Spark and Dataflow.

## Repository Structure

```
/spec/          - Language specification documents
/grammar/       - Parser grammar definition (EBNF)
/examples/      - Sample .copper files demonstrating syntax
/docs/          - Documentation (future)
```

## Key Files

- `spec/SPECIFICATION.md` - Complete Copper language specification
- `grammar/copper.ebnf` - Formal grammar definition for Copper syntax
- `grammar/dax.ebnf` - Complete DAX expression grammar
- `examples/*.copper` - Example models and views demonstrating various features

## Copper Language Basics

**Models** define data structure with dimensions and measures:
```copper
model: orders {
  dimension: order_id {
    type: string
    expression: Orders[OrderID] ;;
    primary_key: yes
  }
  
  measure: total_revenue {
    type: sum
    expression: Orders[Amount] ;;
    value_format: usd
  }
}
```

**Views** define how to query and join models:
```copper
view: sales_analysis {
  from: orders
  
  join: customers {
    type: left_outer
    relationship: many_to_one
    expression: Orders[CustomerID] = Customers[CustomerID] ;;
  }
}
```

## Key Concepts

- **DAX expressions**: Use DAX syntax instead of SQL in `expression:` parameters
- **LookML types**: Supports all LookML dimension and measure types
- **View inheritance**: Views can extend other views using `extends: [view_name]`
- **Value formatting**: Supports both named formats (`usd`, `percent_2`) and custom format strings

## Development Tasks

When working on Copper:
1. Reference `spec/SPECIFICATION.md` for complete syntax details
2. Use `grammar/copper.ebnf` for parser development
3. Check `examples/` for syntax patterns and best practices
4. Maintain backward compatibility with LookML concepts where possible

## Configuration

- `.claude/settings.local.json` - Contains Claude Code permissions configuration