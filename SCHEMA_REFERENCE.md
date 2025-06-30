# Copper: The Universal Semantic Layer - Schema Reference

## Overview

Copper uses YAML-based semantic models to define data sources, dimensions, measures, and relationships. This document provides comprehensive documentation for all schema components and their usage.

## Table of Contents

1. [Semantic Model Structure](#semantic-model-structure)
2. [Data Sources](#data-sources)
3. [Dimensions](#dimensions)
4. [Measures](#measures)
5. [Relationships](#relationships)
6. [Data Types](#data-types)
7. [Expressions](#expressions)
8. [Advanced Features](#advanced-features)
9. [Best Practices](#best-practices)
10. [Complete Examples](#complete-examples)

## Semantic Model Structure

### Top-Level Schema

```yaml
name: string                    # Required: Model name
description: string             # Optional: Model description
datasources: object             # Data source definitions
dimensions: object              # Dimension definitions
measures: object                # Measure definitions
relationships: array            # Relationship definitions
```

### Example Top-Level Structure

```yaml
name: sports_analytics
description: Professional sports analytics semantic model
datasources: { ... }
dimensions: { ... }
measures: { ... }
relationships: [ ... ]
```

## Data Sources

Data sources define the underlying data tables and views that the semantic model operates on.

### DataSource Schema

```yaml
datasourceName:
  type: string                  # Required: table, view
  table: string                 # Table name (for type: table)
  sql: string                   # Custom SQL (for type: view)
  database: string              # Optional: Database name
  schema: string                # Optional: Schema name
  description: string           # Optional: Data source description
  columns: array                # Optional: Column definitions
```

### Data Source Types

#### Table Data Source
```yaml
fighters:
  type: table
  table: ufc_fighter_details
  database: sports_db
  schema: ufc
  description: Fighter profiles and statistics
  columns:
    - name: fighter_id
      type: number
      description: Unique fighter identifier
    - name: fighter_name
      type: string
      description: Fighter's full name
    - name: weight_class
      type: string
      description: Primary fighting weight class
```

#### View Data Source
```yaml
active_fighters:
  type: view
  sql: |
    SELECT f.*, COUNT(fr.fight_id) as total_fights
    FROM fighters f
    LEFT JOIN fight_results fr ON f.fighter_id = fr.fighter_1_id OR f.fighter_id = fr.fighter_2_id
    WHERE f.status = 'active'
    GROUP BY f.fighter_id
  description: Active fighters with fight counts
```

## Dimensions

Dimensions are categorical or descriptive attributes used to slice and dice data in analysis.

### Dimension Schema

```yaml
dimensionName:
  expression: string            # Required: Copper expression
  type: DataType               # Required: Data type
  label: string                # Optional: Display label
  description: string          # Optional: Description
  format: string               # Optional: Display format
```

### Dimension Types

#### Simple Column Reference
```yaml
weight_class:
  expression: fighters.weight_class
  type: string
  label: Weight Class
  description: Fighter's primary weight division
```

#### Expression-Based Dimension
```yaml
age_group:
  expression: CASE
    WHEN fighters.age < 25 THEN "Young (Under 25)"
    WHEN fighters.age < 30 THEN "Prime (25-29)"
    WHEN fighters.age < 35 THEN "Veteran (30-34)"
    ELSE "Elder (35+)"
  type: string
  label: Age Group
  description: Fighter age categorization
```

#### Date/Time Dimensions
```yaml
event_year:
  expression: YEAR(events.event_date)
  type: number
  label: Event Year
  description: Year when event occurred

event_quarter:
  expression: CASE
    WHEN MONTH(events.event_date) <= 3 THEN "Q1"
    WHEN MONTH(events.event_date) <= 6 THEN "Q2"
    WHEN MONTH(events.event_date) <= 9 THEN "Q3"
    ELSE "Q4"
  type: string
  label: Event Quarter
  description: Calendar quarter of event
```

#### Boolean Dimensions
```yaml
title_fight_status:
  expression: CASE
    WHEN fight_results.is_title_fight = true THEN "Title Fight"
    ELSE "Regular Fight"
  type: string
  label: Title Fight Status
  description: Whether fight was for a championship
```

## Measures

Measures are quantitative metrics that can be aggregated and calculated across dimensions.

### Measure Schema

```yaml
measureName:
  expression: string            # Required: Copper expression
  type: DataType               # Required: Data type
  aggregation: AggregationType # Optional: Default aggregation
  label: string                # Optional: Display label
  description: string          # Optional: Description
  format: string               # Optional: Display format
```

### Aggregation Types
- `sum`: Sum values
- `count`: Count records
- `avg`: Average values
- `min`: Minimum value
- `max`: Maximum value

### Basic Measures

#### Count Measures
```yaml
total_fights:
  expression: COUNT(fight_results.fight_id)
  type: number
  aggregation: count
  label: Total Fights
  description: Total number of fights

unique_fighters:
  expression: COUNT(DISTINCT fighters.fighter_id)
  type: number
  aggregation: count
  label: Unique Fighters
  description: Number of distinct fighters
```

#### Sum Measures
```yaml
total_prize_money:
  expression: SUM(fight_results.prize_amount)
  type: currency
  aggregation: sum
  format: "$,.2f"
  label: Total Prize Money
  description: Sum of all prize money awarded
```

#### Average Measures
```yaml
avg_fight_duration:
  expression: AVG(fight_results.duration_seconds)
  type: number
  aggregation: avg
  format: "%.1f seconds"
  label: Average Fight Duration
  description: Mean fight duration in seconds
```

### Conditional Measures

#### Filtered Counts
```yaml
knockout_wins:
  expression: COUNT(fight_results.fight_id WHERE fight_results.method = "KO/TKO")
  type: number
  label: Knockout Wins
  description: Number of knockout victories

title_fight_count:
  expression: COUNT(fight_results.fight_id WHERE fight_results.is_title_fight = true)
  type: number
  label: Title Fights
  description: Number of championship bouts
```

#### Percentage Measures
```yaml
finish_rate:
  expression: COUNT(fight_results.fight_id WHERE fight_results.method != "Decision") / COUNT(fight_results.fight_id) * 100
  type: number
  format: "%.1f%%"
  label: Finish Rate
  description: Percentage of fights ending in finishes

win_rate:
  expression: COUNT(fight_results.fight_id WHERE fight_results.winner_id = fighters.fighter_id) / COUNT(fight_results.fight_id) * 100
  type: number
  format: "%.1f%%"
  label: Win Rate
  description: Percentage of fights won
```

### Advanced Measures

#### Complex Conditional Logic
```yaml
performance_score:
  expression: CASE
    WHEN fight_results.method = "KO/TKO" AND fight_results.round = 1 THEN 100
    WHEN fight_results.method = "KO/TKO" THEN 85
    WHEN fight_results.method = "Submission" THEN 80
    WHEN fight_results.method = "Decision" AND fight_results.winner_id = fighters.fighter_id THEN 70
    ELSE 0
  type: number
  label: Performance Score
  description: Weighted performance scoring system
```

#### Statistical Measures
```yaml
striking_accuracy:
  expression: AVG(fight_details.significant_strikes_landed / fight_details.significant_strikes_attempted) * 100
  type: number
  format: "%.1f%%"
  label: Striking Accuracy
  description: Average percentage of strikes that land

takedown_defense:
  expression: AVG(1 - (fight_details.takedowns_landed / fight_details.takedowns_attempted)) * 100
  type: number
  format: "%.1f%%"
  label: Takedown Defense
  description: Percentage of takedowns successfully defended
```

## Relationships

Relationships define how data sources are connected through foreign key relationships.

### Relationship Schema

```yaml
relationships:
  - fromTable.fromColumn → toTable.toColumn
  # OR
  - from: fromTable
    to: toTable
    from_column: fromColumn
    to_column: toColumn
    cardinality: many_to_one     # Optional: one_to_one, one_to_many, many_to_one, many_to_many
```

### Relationship Examples

#### Simple String Format
```yaml
relationships:
  - fight_results.event_id → events.event_id
  - fight_results.fighter_1_id → fighters.fighter_id
  - fight_results.fighter_2_id → fighters.fighter_id
  - fight_details.fight_id → fight_results.fight_id
```

#### Object Format with Cardinality
```yaml
relationships:
  - from: fight_results
    to: events
    from_column: event_id
    to_column: event_id
    cardinality: many_to_one
  - from: fighters
    to: weight_classes
    from_column: weight_class
    to_column: class_name
    cardinality: many_to_one
```

## Data Types

### Supported Data Types

- `string`: Text data
- `number`: Numeric data (integers and decimals)
- `boolean`: True/false values
- `date`: Date values
- `currency`: Monetary values

### Data Type Examples

```yaml
dimensions:
  fighter_name:
    expression: fighters.name
    type: string
    
  height_cm:
    expression: fighters.height
    type: number
    
  is_champion:
    expression: fighters.is_current_champion
    type: boolean
    
  debut_date:
    expression: fighters.professional_debut
    type: date
    
measures:
  total_earnings:
    expression: SUM(fight_results.prize_money)
    type: currency
    format: "$,.2f"
```

## Expressions

Copper supports a DAX-like expression language for creating calculated dimensions and measures.

### Supported Functions

#### Aggregation Functions
- `SUM(column)`: Sum values
- `COUNT(column)`: Count non-null values
- `AVG(column)`: Average values
- `MIN(column)`: Minimum value
- `MAX(column)`: Maximum value
- `COUNT(DISTINCT column)`: Count unique values

#### Conditional Functions
- `IF(condition, true_value, false_value)`: Simple conditional
- `CASE WHEN condition THEN value ELSE other_value`: Complex conditional
- `SWITCH(expr, val1, result1, val2, result2, default)`: Multi-way conditional

#### Date Functions
- `YEAR(date)`: Extract year
- `MONTH(date)`: Extract month
- `DAY(date)`: Extract day
- `DATE_TRUNC(unit, date)`: Truncate to time unit

#### String Functions
- `COALESCE(val1, val2, ...)`: Return first non-null value
- `ISNULL(value)`: Check if value is null
- `ISBLANK(value)`: Check if value is blank

#### Mathematical Operators
- `+`, `-`, `*`, `/`: Basic arithmetic
- `=`, `!=`, `<>`: Equality operators
- `<`, `>`, `<=`, `>=`: Comparison operators
- `AND`, `OR`, `NOT`: Logical operators

### Expression Examples

#### Simple Expressions
```yaml
# Basic calculation
total_revenue:
  expression: SUM(orders.amount)
  type: currency

# Conditional counting
high_value_orders:
  expression: COUNT(orders.id WHERE orders.amount > 1000)
  type: number
```

#### Complex Expressions
```yaml
# Multi-condition case statement
fighter_tier:
  expression: CASE
    WHEN fighters.total_fights > 20 AND fighters.win_rate > 80 THEN "Elite"
    WHEN fighters.total_fights > 10 AND fighters.win_rate > 70 THEN "Veteran"
    WHEN fighters.total_fights > 5 THEN "Experienced"
    ELSE "Newcomer"
  type: string

# Percentage calculation with null handling
finish_percentage:
  expression: COALESCE(
    COUNT(fights.id WHERE fights.method != "Decision") / NULLIF(COUNT(fights.id), 0) * 100,
    0
  )
  type: number
  format: "%.1f%%"
```

#### Nested Expressions
```yaml
# Complex performance metric
composite_score:
  expression: IF(
    fighters.is_active = true,
    (
      (COUNT(fights.id WHERE fights.winner_id = fighters.fighter_id) * 10) +
      (COUNT(fights.id WHERE fights.method = "KO/TKO" AND fights.winner_id = fighters.fighter_id) * 5) +
      (COUNT(fights.id WHERE fights.is_title_fight = true) * 3)
    ) / NULLIF(COUNT(fights.id), 0),
    0
  )
  type: number
  format: "%.2f"
```

## Advanced Features

### Large Model Organization

For large models, consider organizing definitions into logical groups within the same file:

```yaml
# Organize by functional area
name: comprehensive_sports_model
datasources:
  # Event data sources
  events: { ... }
  venues: { ... }
  
  # Fighter data sources  
  fighters: { ... }
  rankings: { ... }

dimensions:
  # Event dimensions
  event_name: { ... }
  event_location: { ... }
  
  # Fighter dimensions
  fighter_name: { ... }
  nationality: { ... }
```

### Column Definitions

Define detailed column metadata:

```yaml
datasources:
  fighters:
    type: table
    table: fighter_profiles
    columns:
      - name: fighter_id
        type: number
        description: Unique identifier for fighter
        primary_key: true
      - name: reach_cm
        type: number
        description: Fighter reach in centimeters
        nullable: true
        min_value: 150
        max_value: 250
```

### Future Data Source Types

The following data source types are planned for future releases:
- **API sources**: External REST APIs with authentication
- **Stream sources**: Real-time data from Kafka or other streaming platforms
- **File sources**: CSV, Parquet, and other file formats

## Best Practices

### Naming Conventions

1. **Descriptive Names**: Use clear, descriptive names
   ```yaml
   # Good
   knockout_finish_rate:
     expression: COUNT(...) / COUNT(...) * 100
   
   # Avoid
   ko_rate:
     expression: COUNT(...) / COUNT(...) * 100
   ```

2. **Consistent Prefixes**: Group related items
   ```yaml
   # Fighter dimensions
   fighter_name: { ... }
   fighter_nationality: { ... }
   fighter_weight_class: { ... }
   
   # Event dimensions
   event_name: { ... }
   event_location: { ... }
   event_date: { ... }
   ```

### Documentation

Always include descriptions and labels:

```yaml
finish_rate:
  expression: COUNT(fights.id WHERE fights.method != "Decision") / COUNT(fights.id) * 100
  type: number
  format: "%.1f%%"
  label: Finish Rate
  description: Percentage of fights that end before going to the judges' scorecards
```

### Performance Optimization

1. **Avoid Complex Nested Calculations** in frequently-used measures
2. **Use Appropriate Data Types** for storage efficiency
3. **Consider Aggregation Types** for better query planning

### Data Quality

1. **Handle Null Values**:
   ```yaml
   safe_percentage:
     expression: COALESCE(numerator / NULLIF(denominator, 0), 0) * 100
   ```

2. **Validate Relationships**:
   ```yaml
   relationships:
     - fighters.weight_class → weight_classes.class_name  # Ensure referential integrity
   ```

## Complete Examples

### UFC Analytics Model

```yaml
name: ufc_comprehensive_analytics
description: Complete UFC analytics semantic model

datasources:
  events:
    type: table
    table: ufc_events
    description: UFC event information
  fighters:
    type: table
    table: ufc_fighter_details
    description: Fighter profiles and statistics
  fight_results:
    type: table
    table: ufc_fight_results
    description: Fight outcomes and results
  fight_details:
    type: table
    table: ufc_fight_details
    description: Detailed fight statistics

relationships:
  - fight_results.event_id → events.event_id
  - fight_results.fighter_1_id → fighters.fighter_id
  - fight_results.fighter_2_id → fighters.fighter_id
  - fight_results.winner_id → fighters.fighter_id
  - fight_details.fight_id → fight_results.fight_id
  - fight_details.fighter_id → fighters.fighter_id

dimensions:
  # Fighter attributes
  fighter_name:
    expression: fighters.fighter_name
    type: string
    label: Fighter Name
    
  nationality:
    expression: fighters.nationality
    type: string
    label: Nationality
    
  weight_class:
    expression: fight_results.weight_class
    type: string
    label: Weight Class
    
  # Performance categorization
  experience_level:
    expression: CASE
      WHEN fighters.total_fights >= 20 THEN "Veteran (20+ fights)"
      WHEN fighters.total_fights >= 10 THEN "Experienced (10-19 fights)"
      WHEN fighters.total_fights >= 5 THEN "Developing (5-9 fights)"
      ELSE "Newcomer (Under 5 fights)"
    type: string
    label: Experience Level
    
  # Event attributes
  event_location:
    expression: events.location
    type: string
    label: Event Location
    
  venue_type:
    expression: CASE
      WHEN events.venue LIKE "%Arena%" THEN "Arena"
      WHEN events.venue LIKE "%Center%" THEN "Center"
      WHEN events.venue LIKE "%Garden%" THEN "Garden"
      ELSE "Other Venue"
    type: string
    label: Venue Type

measures:
  # Basic counts
  total_fights:
    expression: COUNT(fight_results.fight_id)
    type: number
    label: Total Fights
    description: Total number of fights
    
  unique_fighters:
    expression: COUNT(DISTINCT fighters.fighter_id)
    type: number
    label: Unique Fighters
    description: Number of distinct fighters
    
  # Performance metrics
  finish_rate:
    expression: COUNT(fight_results.fight_id WHERE fight_results.method != "Decision") / COUNT(fight_results.fight_id) * 100
    type: number
    format: "%.1f%%"
    label: Finish Rate
    description: Percentage of fights ending in finishes
    
  knockout_percentage:
    expression: COUNT(fight_results.fight_id WHERE fight_results.method = "KO/TKO") / COUNT(fight_results.fight_id) * 100
    type: number
    format: "%.1f%%"
    label: Knockout Percentage
    description: Percentage of fights ending in knockouts
    
  submission_percentage:
    expression: COUNT(fight_results.fight_id WHERE fight_results.method = "Submission") / COUNT(fight_results.fight_id) * 100
    type: number
    format: "%.1f%%"
    label: Submission Percentage
    description: Percentage of fights ending in submissions
    
  # Advanced metrics
  avg_significant_strikes:
    expression: AVG(fight_details.significant_strikes_landed)
    type: number
    format: "%.1f"
    label: Avg Significant Strikes
    description: Average significant strikes landed per fight
    
  striking_accuracy:
    expression: AVG(fight_details.significant_strikes_landed / NULLIF(fight_details.significant_strikes_attempted, 0)) * 100
    type: number
    format: "%.1f%%"
    label: Striking Accuracy
    description: Average striking accuracy percentage
    
  takedown_success_rate:
    expression: AVG(fight_details.takedowns_landed / NULLIF(fight_details.takedowns_attempted, 0)) * 100
    type: number
    format: "%.1f%%"
    label: Takedown Success Rate
    description: Average takedown success percentage
    
  # Title fight metrics
  title_fight_finish_rate:
    expression: COUNT(fight_results.fight_id WHERE fight_results.is_title_fight = true AND fight_results.method != "Decision") / NULLIF(COUNT(fight_results.fight_id WHERE fight_results.is_title_fight = true), 0) * 100
    type: number
    format: "%.1f%%"
    label: Title Fight Finish Rate
    description: Finish rate specifically for championship bouts
```

This comprehensive schema reference provides all the information needed to create sophisticated semantic models with Copper. For additional examples and implementation details, refer to the UFC analytics example in the `examples/` directory.