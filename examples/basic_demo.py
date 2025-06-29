#!/usr/bin/env python3
"""
Basic demo of Copper semantic layer functionality.

This example demonstrates:
1. Loading a semantic model from YAML
2. Building queries with the fluent API
3. Executing queries with Pandas backend
"""

import sys
from pathlib import Path
import pandas as pd

# Add copper to path
sys.path.insert(0, str(Path(__file__).parent.parent))

import copper
from copper.semantic.loader import SemanticModelLoader


def create_sample_data():
    """Create sample ecommerce data."""
    
    # Orders table
    orders = pd.DataFrame({
        'id': [1, 2, 3, 4, 5, 6, 7, 8],
        'customer_id': [1, 2, 1, 3, 2, 4, 1, 3],
        'total_amount': [100.0, 250.0, 75.0, 500.0, 125.0, 300.0, 50.0, 200.0],
        'status': ['shipped', 'pending', 'shipped', 'shipped', 'cancelled', 'shipped', 'shipped', 'pending'],
        'order_date': pd.to_datetime([
            '2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', 
            '2024-01-05', '2024-01-06', '2024-01-07', '2024-01-08'
        ])
    })
    
    # Customers table
    customers = pd.DataFrame({
        'id': [1, 2, 3, 4],
        'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
        'region': ['West', 'East', 'West', 'North'],
        'tier': ['Gold', 'Silver', 'Gold', 'Bronze'],
        'age': [25, 35, 45, 30]
    })
    
    return {'Orders': orders, 'Customers': customers}


def create_sample_model():
    """Create a sample semantic model."""
    
    model_def = {
        'name': 'ecommerce',
        'description': 'Sample ecommerce semantic model',
        
        'tables': {
            'Orders': {
                'table': 'orders',
                'description': 'Customer orders'
            },
            'Customers': {
                'table': 'customers', 
                'description': 'Customer information'
            }
        },
        
        'relationships': [
            'Orders.customer_id → Customers.id'
        ],
        
        'dimensions': {
            'region': {
                'sql': 'Customers.region',
                'type': 'string',
                'description': 'Customer region'
            },
            'customer_tier': {
                'sql': 'Customers.tier',
                'type': 'string',
                'description': 'Customer tier (Gold, Silver, Bronze)'
            },
            'order_status': {
                'sql': 'Orders.status',
                'type': 'string',
                'description': 'Order status'
            }
        },
        
        'measures': {
            'revenue': {
                'expression': 'SUM(Orders.total_amount)',
                'type': 'currency',
                'description': 'Total revenue'
            },
            'order_count': {
                'expression': 'COUNT(Orders.id)',
                'type': 'number',
                'description': 'Number of orders'
            },
            'avg_order_value': {
                'expression': 'AVG(Orders.total_amount)',
                'type': 'currency',
                'description': 'Average order value'
            }
        }
    }
    
    return SemanticModelLoader.load_from_dict(model_def)


def main():
    """Run the basic demo."""
    
    print("🚀 Copper Semantic Layer Demo")
    print("=" * 40)
    
    # Create sample data and model
    print("\n📊 Creating sample data...")
    data = create_sample_data()
    
    print("📋 Sample Orders:")
    print(data['Orders'].head())
    print("\n📋 Sample Customers:")
    print(data['Customers'].head())
    
    print("\n🏗️  Creating semantic model...")
    model = create_sample_model()
    
    print(f"Model: {model.name}")
    print(f"Dimensions: {list(model.dimensions.keys())}")
    print(f"Measures: {list(model.measures.keys())}")
    
    # Example 1: Revenue by region
    print("\n" + "=" * 40)
    print("📈 Example 1: Revenue by Region")
    print("=" * 40)
    
    query1 = copper.Query(model) \
        .dimensions(['region']) \
        .measures(['revenue', 'order_count'])
    
    print(f"Query: {query1}")
    
    try:
        result1 = query1.to_pandas(data)
        print("\nResults:")
        print(result1)
    except Exception as e:
        print(f"❌ Error executing query: {e}")
    
    # Example 2: Customer tier analysis
    print("\n" + "=" * 40)
    print("📈 Example 2: Customer Tier Analysis")
    print("=" * 40)
    
    query2 = copper.Query(model) \
        .dimensions(['customer_tier']) \
        .measures(['revenue', 'avg_order_value']) \
        .order_by(['revenue'], ascending=False)
    
    print(f"Query: {query2}")
    
    try:
        result2 = query2.to_pandas(data)
        print("\nResults:")
        print(result2)
    except Exception as e:
        print(f"❌ Error executing query: {e}")
    
    # Example 3: Filtered analysis
    print("\n" + "=" * 40)
    print("📈 Example 3: Shipped Orders Only")
    print("=" * 40)
    
    query3 = copper.Query(model) \
        .dimensions(['region']) \
        .measures(['revenue']) \
        .filters(['Orders.status = "shipped"'])
    
    print(f"Query: {query3}")
    
    try:
        result3 = query3.to_pandas(data)
        print("\nResults:")
        print(result3)
    except Exception as e:
        print(f"❌ Error executing query: {e}")
    
    print("\n🎉 Demo completed!")


if __name__ == "__main__":
    main()