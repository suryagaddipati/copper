# Copper - Universal Semantic Layer Project Plan

## 🎯 Project Goal

**Build a portable semantic layer that compiles metric definitions and queries into runtime code across multiple engines.**

**Copper = Define Once. Run Anywhere. ☄️**

---

## ✅ Success Criteria

To verify whether Copper is meeting its goal, the following must be testable and demonstrable:

1. **Expression Fidelity**

   * [ ] Can the parser correctly transform a representative set of DAX-style expressions into ASTs?
   * [ ] Are all supported functions outputting expected results?
   * [ ] Are edge cases (nulls, type errors, logical precedence) handled consistently?

2. **Semantic Modeling Consistency**

   * [ ] Can YAML definitions fully describe dimensions, measures, and relationships?
   * [ ] Is there type validation and relationship enforcement?
   * [ ] Does the same YAML behave consistently across execution engines?

3. **Query Portability**

   * [ ] Can the same query be executed across Pandas, Spark, SQL, and Beam?
   * [ ] Are output results equivalent across engines (within rounding margin)?
   * [ ] Does performance remain reasonable at scale?

4. **Developer Experience**

   * [ ] Can users build and validate models quickly using YAML and code?
   * [ ] Do error messages help guide resolution?
   * [ ] Is the API intuitive and fluent?

---

## 📘 Use Cases

### 1. Basic Aggregation

**Goal:** Validate core group-by aggregation using semantic definitions.

**Example:**

```yaml
measures:
  revenue:
    expression: SUM(Orders.total_amount)
    type: number

dimensions:
  region:
    sql: Customers.region
    type: string
```

```python
query = layer.dimensions(["region"]).measures(["revenue"])
df = query.to_pandas()
```

### 2. Conditional Logic

**Goal:** Support `IF`, `SWITCH`, and boolean logic in expressions.

**Example:**

```yaml
measures:
  is_premium:
    expression: IF(Customers.tier = "Gold", 1, 0)
    type: number
```

```python
query = layer.measures(["is_premium"])
df = query.to_pandas()
```

### 3. Filter Context

**Goal:** Apply filters at query-time and within measures.

**Example:**

```yaml
measures:
  shipped_orders:
    expression: COUNT(Orders.id WHERE Orders.status = "shipped")
    type: number
```

```python
query = layer.measures(["shipped_orders"]).filters(["region = 'West'"])
df = query.to_pandas()
```

### 4. Joins + Relationship Navigation

**Goal:** Validate dimension table joins and field traversal.

**Example:**

```yaml
relationships:
  Orders.customer_id → Customers.id

dimensions:
  customer_region:
    sql: Customers.region
    type: string
```

```python
query = layer.dimensions(["customer_region"]).measures(["revenue"])
df = query.to_pandas()
```

### 5. Calculated Columns / Derived Dimensions

**Goal:** Create new columns using case logic.

**Example:**

```yaml
dimensions:
  age_group:
    expression: CASE
      WHEN Customers.age < 18 THEN "minor"
      ELSE "adult"
    type: string
```

```python
query = layer.dimensions(["age_group"]).measures(["customer_count"])
df = query.to_pandas()
```

### 6. Nested Expressions

* `IF(..., SUM(...), COUNT(...))`
* Composition of functions in AST

### 7. Multi-Engine Execution

* Execute same query across Pandas, Spark, SQL
* Validate outputs are logically equivalent

### 8. Streaming Support (Beam)

* Apply windowing + grouped aggregations
* e.g., `SUM(revenue) per region per day`

### 9. Time-Based Aggregations

* `DATE_TRUNC`, `YEAR`, `MONTH`, rolling metrics
* e.g., `Revenue rolling 7-day average`

### 10. YAML Modeling Coverage

* Measures with expressions
* Dimensions with labels and types
* Relationships with cardinality

---

## Phase 1: Core Foundations

### 1.1 Expression Language: DAX Subset

* [ ] Analyze DAX grammar files (Microsoft ANTLR, community grammars)
* [ ] Define supported expression subset (basic aggregations, conditionals)
* [ ] Build parser + AST (Scala or Python-based)
* [ ] Unit test common patterns + edge cases

**Output:** Robust DAX-like expression → AST converter

### 1.2 Semantic Layer Modeling

* [ ] Define Copper YAML schema for dimensions, measures, relationships
* [ ] Implement schema loader and validator
* [ ] Establish internal type system (string, number, currency, boolean, etc.)
* [ ] Model support for joins (star/snowflake, optional pathing)

**Output:** YAML → in-memory semantic model

### 1.3 Query Builder API

* [ ] Design fluent API for query construction
* [ ] Integrate semantic model with AST-based expression logic
* [ ] Support dimension selection, measure computation, and filters

**Output:**

```python
query = (
  layer
    .dimensions(["region"])
    .measures(["revenue"])
    .filters(["year = 2024"])
)
```

### 1.4 Pandas Execution Engine

* [ ] Translate semantic query + AST to Pandas code
* [ ] Implement `groupby`, `agg`, `join`, `filter`, `calculated fields`
* [ ] Basic performance tests on mock datasets

**Output:** Working `.to_pandas()` method for Copper queries

---

## Phase 2: Engine Generalization + Developer Tooling

### 2.1 Multi-Engine Support

* [ ] Add Spark, SQL (BigQuery dialect) code generators
* [ ] Standardize engine interface: `.to_pandas()`, `.to_spark()`, `.to_sql()`
* [ ] Validate consistency of outputs across engines

### 2.2 Streaming + Beam Integration

* [ ] Build `CopperTransform` for Scio (Scala) pipelines
* [ ] Support dimension/measures windowing and joins in streaming context

### 2.3 Developer Tooling + UX

* [ ] Auto-complete helper for YAML
* [ ] Linting and schema suggestion engine
* [ ] REPL/Playground demo app for query building

---

## 🗂 Repository Structure (Proposed)

```
copper/
├── copper/
│   ├── parser/            # DAX parser and AST
│   ├── semantic/          # YAML schema and in-memory model
│   ├── query/             # Query builder and planning logic
│   ├── executors/         # pandas, spark, sql engines
│   └── beam/              # Beam/Scio integration (Scala)
├── tests/
├── examples/
├── docs/
└── setup.py
```

---

## 🚀 Milestone 1: End-to-End Demo (Pandas)

### Scope:

* [ ] Write YAML schema for mock ecommerce dataset
* [ ] Support expressions using `IF`, `SUM`, `COUNT`, `SWITCH`
* [ ] Parse expression → build AST → generate Pandas code
* [ ] Join dimensions, filter data, group by region

### Success Test:

```python
# metrics.yaml has defined measures and dimensions
layer = copper.load("metrics.yaml")
query = layer.dimensions(["region"]).measures(["revenue"])
df = query.to_pandas()
assert set(df.columns) == {"region", "revenue"}
```

---
