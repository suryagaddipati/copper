# Sample Datasets

This directory contains sample datasets for testing Copper Studio database connections.

## UFC Sample Dataset

### Creating the Database

```bash
cd examples/datasets
python3 create_ufc_data.py
```

This creates `ufc_sample.db` with sample UFC data including:

- **fighters** - Fighter profiles with records and weight classes
- **fights** - Fight results with methods and rounds  
- **events** - UFC events with dates and venues

### Using with Studio

1. Start Copper Studio: `make dev`
2. Go to http://localhost:3000
3. Create new DuckDB connection:
   - Name: "UFC Sample Data"
   - Type: "duckdb" 
   - File Path: `/path/to/copper/examples/datasets/ufc_sample.db`
4. Connect and explore the tables

### Sample Queries

```sql
-- Top fighters by win rate
SELECT name, wins, losses, 
       ROUND(wins::FLOAT / (wins + losses) * 100, 1) as win_percentage
FROM fighters 
WHERE (wins + losses) > 0
ORDER BY win_percentage DESC;

-- Fights by finish method
SELECT method, COUNT(*) as count
FROM fights 
GROUP BY method
ORDER BY count DESC;

-- Events with fight counts
SELECT e.name, e.date, e.location, COUNT(f.fight_id) as fight_count
FROM events e
LEFT JOIN fights f ON e.event_id = f.event_id
GROUP BY e.event_id, e.name, e.date, e.location
ORDER BY e.date;
```

This dataset is just one example - Studio can connect to any DuckDB database or other supported database types.