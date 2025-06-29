#!/usr/bin/env python3
"""
Example of loading Copper models from YAML files.

This demonstrates loading models that are split across multiple files
with separate datasource definitions.
"""

import sys
from pathlib import Path
import pandas as pd

# Add copper to path
sys.path.insert(0, str(Path(__file__).parent.parent))

import src as copper
from src.semantic.loader import SemanticModelLoader


def load_ecommerce_example():
    """Load the ecommerce example with separate files."""
    
    print("🏪 Loading E-commerce Model")
    print("=" * 40)
    
    try:
        # Note: This would work if we implement the includes functionality
        # For now, we'll load the main model file
        model_path = Path(__file__).parent / "ecommerce" / "model.yaml"
        print(f"Loading model from: {model_path}")
        
        # Currently our loader doesn't support includes, so we'll show the structure
        print("\nModel structure:")
        print("├── ecommerce/")
        print("│   ├── datasources.yaml  # Data source definitions")
        print("│   └── model.yaml        # Semantic model")
        
        # For demonstration, create a simplified model
        model_def = {
            'name': 'ecommerce_analytics',
            'description': 'E-commerce analytics model',
            'datasources': {
                'orders': {
                    'type': 'table',
                    'table': 'orders',
                    'description': 'Customer orders'
                },
                'customers': {
                    'type': 'table', 
                    'table': 'customers',
                    'description': 'Customer information'
                }
            },
            'relationships': [
                'orders.customer_id → customers.id'
            ],
            'dimensions': {
                'customer_region': {
                    'sql': 'customers.region',
                    'type': 'string',
                    'label': 'Customer Region'
                }
            },
            'measures': {
                'total_revenue': {
                    'expression': 'SUM(orders.total_amount)',
                    'type': 'currency',
                    'label': 'Total Revenue'
                }
            }
        }
        
        model = SemanticModelLoader.load_from_dict(model_def)
        print(f"\n✅ Loaded model: {model.name}")
        print(f"   Dimensions: {list(model.dimensions.keys())}")
        print(f"   Measures: {list(model.measures.keys())}")
        
        return model
        
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return None


def load_saas_example():
    """Load the SaaS example with separate files."""
    
    print("\n💼 Loading SaaS Model")  
    print("=" * 40)
    
    try:
        model_path = Path(__file__).parent / "saas" / "model.yaml"
        print(f"Loading model from: {model_path}")
        
        print("\nModel structure:")
        print("├── saas/")
        print("│   ├── datasources.yaml  # Data source definitions")
        print("│   └── model.yaml        # Semantic model")
        
        # For demonstration, create a simplified SaaS model
        model_def = {
            'name': 'saas_business_metrics',
            'description': 'SaaS business analytics model',
            'datasources': {
                'subscriptions': {
                    'type': 'table',
                    'table': 'subscriptions',
                    'description': 'Customer subscriptions'
                },
                'users': {
                    'type': 'table',
                    'table': 'users', 
                    'description': 'User accounts'
                }
            },
            'relationships': [
                'subscriptions.user_id → users.id'
            ],
            'dimensions': {
                'subscription_plan': {
                    'sql': 'subscriptions.plan_type',
                    'type': 'string',
                    'label': 'Subscription Plan'
                }
            },
            'measures': {
                'monthly_recurring_revenue': {
                    'expression': 'SUM(subscriptions.monthly_value WHERE subscriptions.status = "active")',
                    'type': 'currency',
                    'label': 'Monthly Recurring Revenue (MRR)'
                }
            }
        }
        
        model = SemanticModelLoader.load_from_dict(model_def)
        print(f"\n✅ Loaded model: {model.name}")
        print(f"   Dimensions: {list(model.dimensions.keys())}")
        print(f"   Measures: {list(model.measures.keys())}")
        
        return model
        
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return None


def demonstrate_file_structure():
    """Show the new file structure with separate YAML files."""
    
    print("\n📁 New File Structure")
    print("=" * 40)
    
    examples_dir = Path(__file__).parent
    
    print("examples/")
    for example_dir in ['ecommerce', 'saas']:
        if (examples_dir / example_dir).exists():
            print(f"├── {example_dir}/")
            for file in (examples_dir / example_dir).iterdir():
                if file.is_file():
                    print(f"│   ├── {file.name}")
                    
    print("\nBenefits of separate files:")
    print("✅ Better organization and modularity")
    print("✅ Reusable datasource definitions") 
    print("✅ Easier collaboration (different people can work on different files)")
    print("✅ Clear separation of concerns")
    print("✅ Standard YAML extension for better IDE support")


def main():
    """Run the file loading demonstration."""
    
    print("🚀 Copper YAML File Structure Demo")
    print("=" * 50)
    
    demonstrate_file_structure()
    
    # Load examples
    ecommerce_model = load_ecommerce_example()
    saas_model = load_saas_example()
    
    if ecommerce_model:
        print(f"\n🎯 E-commerce model ready for queries!")
        print("   Example: copper.Query(model).dimensions(['customer_region']).measures(['total_revenue'])")
    
    if saas_model:
        print(f"\n🎯 SaaS model ready for queries!")
        print("   Example: copper.Query(model).dimensions(['subscription_plan']).measures(['monthly_recurring_revenue'])")
    
    print("\n💡 Future Enhancement:")
    print("   Implement 'includes' functionality to automatically load referenced files")
    print("   Example: includes: [datasources.yaml, shared/common_dimensions.yaml]")


if __name__ == "__main__":
    main()