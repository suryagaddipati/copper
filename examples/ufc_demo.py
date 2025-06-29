#!/usr/bin/env python3
"""
UFC Analytics Demo using Copper Semantic Layer

This demonstrates UFC/MMA analytics using real fight data with Copper's
semantic modeling and query capabilities.
"""

import sys
from pathlib import Path
import pandas as pd

# Add copper to path
sys.path.insert(0, str(Path(__file__).parent.parent))

import src as copper
from src.semantic.loader import SemanticModelLoader
from examples.ufc.data_loader import UFCDataLoader


def load_ufc_model():
    """Load UFC semantic model for analytics."""
    
    # For now, create a simplified model since includes aren't implemented yet
    model_def = {
        'name': 'ufc_analytics',
        'description': 'UFC/MMA analytics semantic model',
        
        'datasources': {
            'events': {
                'type': 'table',
                'table': 'ufc_events',
                'description': 'UFC event information'
            },
            'fighters': {
                'type': 'table',
                'table': 'ufc_fighter_details',
                'description': 'Fighter profiles and attributes'
            },
            'fight_results': {
                'type': 'table',
                'table': 'ufc_fight_results',
                'description': 'Fight outcomes and results'
            },
            'fight_details': {
                'type': 'table',
                'table': 'ufc_fight_details',
                'description': 'Detailed fight statistics'
            }
        },
        
        'relationships': [
            'fight_results.event_id → events.event_id',
            'fight_results.fighter_1_id → fighters.fighter_id',
            'fight_results.fighter_2_id → fighters.fighter_id',
            'fight_details.fight_id → fight_results.fight_id'
        ],
        
        'dimensions': {
            'fighter_name': {
                'sql': 'fighters.fighter_name',
                'type': 'string',
                'label': 'Fighter Name'
            },
            'nationality': {
                'sql': 'fighters.nationality',
                'type': 'string',
                'label': 'Nationality'
            },
            'weight_class': {
                'sql': 'fight_results.weight_class',
                'type': 'string',
                'label': 'Weight Class'
            },
            'finish_method': {
                'sql': 'fight_results.method',
                'type': 'string',
                'label': 'Finish Method'
            },
            'event_location': {
                'sql': 'events.location',
                'type': 'string',
                'label': 'Event Location'
            },
            'event_year': {
                'expression': 'YEAR(events.event_date)',
                'type': 'number',
                'label': 'Event Year'
            }
        },
        
        'measures': {
            'total_fights': {
                'expression': 'COUNT(fight_results.fight_id)',
                'type': 'number',
                'label': 'Total Fights'
            },
            'knockout_wins': {
                'expression': 'COUNT(fight_results.fight_id WHERE fight_results.method = "KO/TKO")',
                'type': 'number',
                'label': 'Knockout Wins'
            },
            'submission_wins': {
                'expression': 'COUNT(fight_results.fight_id WHERE fight_results.method = "Submission")',
                'type': 'number',
                'label': 'Submission Wins'
            },
            'finish_rate': {
                'expression': 'COUNT(fight_results.fight_id WHERE fight_results.method != "Decision") / COUNT(fight_results.fight_id) * 100',
                'type': 'number',
                'label': 'Finish Rate (%)'
            },
            'avg_significant_strikes': {
                'expression': 'AVG(fight_details.significant_strikes_landed)',
                'type': 'number',
                'label': 'Avg Significant Strikes Landed'
            }
        }
    }
    
    return SemanticModelLoader.load_from_dict(model_def)


def main():
    """Run the UFC analytics demonstration."""
    
    print("🥊 UFC Analytics with Copper Semantic Layer")
    print("=" * 50)
    
    # Load UFC data
    print("\n📊 Loading UFC data...")
    loader = UFCDataLoader()
    ufc_data = loader.load_all_data()
    
    print("UFC datasets loaded:")
    for table_name, df in ufc_data.items():
        print(f"  • {table_name}: {len(df)} rows")
    
    # Load semantic model
    print("\n🏗️  Loading UFC semantic model...")
    model = load_ufc_model()
    print(f"Model: {model.name}")
    print(f"Dimensions: {list(model.dimensions.keys())}")
    print(f"Measures: {list(model.measures.keys())}")
    
    # Example 1: Fight analysis by weight class
    print("\n" + "=" * 50)
    print("📈 Analysis 1: Fights by Weight Class")
    print("=" * 50)
    
    query1 = copper.Query(model) \
        .dimensions(['weight_class']) \
        .measures(['total_fights', 'finish_rate'])
    
    print(f"Query: {query1}")
    
    try:
        result1 = query1.to_pandas(ufc_data)
        print("\nResults:")
        print(result1)
    except Exception as e:
        print(f"❌ Error executing query: {e}")
        print("💡 Note: This is expected with the current simplified implementation")
    
    # Example 2: Finish methods analysis
    print("\n" + "=" * 50)
    print("📈 Analysis 2: Finish Methods Distribution")
    print("=" * 50)
    
    query2 = copper.Query(model) \
        .dimensions(['finish_method']) \
        .measures(['total_fights'])
    
    print(f"Query: {query2}")
    
    try:
        result2 = query2.to_pandas(ufc_data)
        print("\nResults:")
        print(result2)
    except Exception as e:
        print(f"❌ Error executing query: {e}")
    
    # Example 3: Geographic analysis
    print("\n" + "=" * 50)
    print("📈 Analysis 3: Events by Location")
    print("=" * 50)
    
    query3 = copper.Query(model) \
        .dimensions(['event_location']) \
        .measures(['total_fights'])
    
    print(f"Query: {query3}")
    
    try:
        result3 = query3.to_pandas(ufc_data)
        print("\nResults:")
        print(result3)
    except Exception as e:
        print(f"❌ Error executing query: {e}")
    
    # Direct data analysis (without Copper for comparison)
    print("\n" + "=" * 50)
    print("📊 Direct Data Analysis (for comparison)")
    print("=" * 50)
    
    print("\n🏆 Fighter Statistics:")
    try:
        stats = loader.get_fighter_stats("Jon Jones")
        for key, value in stats.items():
            print(f"  {key}: {value}")
    except ValueError:
        print("  Jon Jones not found in sample data")
    
    print("\n🎪 Event Analysis:")
    try:
        event_stats = loader.get_event_summary("UFC 300: Pereira vs Hill")
        for key, value in event_stats.items():
            print(f"  {key}: {value}")
    except ValueError:
        print("  Event not found in sample data")
    
    # Show data insights
    print("\n" + "=" * 50)
    print("🔍 Sample Data Insights")
    print("=" * 50)
    
    print(f"\n📊 Dataset Overview:")
    print(f"  • Total Events: {len(ufc_data['events'])}")
    print(f"  • Total Fighters: {len(ufc_data['fighters'])}")
    print(f"  • Total Fights: {len(ufc_data['fight_results'])}")
    
    # Weight class distribution
    weight_classes = ufc_data['fight_results']['weight_class'].value_counts()
    print(f"\n🏋️ Top Weight Classes:")
    for weight_class, count in weight_classes.head().items():
        print(f"  • {weight_class}: {count} fights")
    
    # Finish methods
    methods = ufc_data['fight_results']['method'].value_counts()
    print(f"\n🥊 Finish Methods:")
    for method, count in methods.items():
        print(f"  • {method}: {count} fights ({count/len(ufc_data['fight_results'])*100:.1f}%)")
    
    # Nationality representation
    nationalities = ufc_data['fighters']['nationality'].value_counts()
    print(f"\n🌍 Top Fighter Nationalities:")
    for country, count in nationalities.head().items():
        print(f"  • {country}: {count} fighters")
    
    print("\n🎯 Semantic Model Benefits:")
    print("✅ Standardized metrics across all analyses")
    print("✅ Reusable dimension and measure definitions")
    print("✅ Consistent business logic enforcement")
    print("✅ Easy cross-engine portability (Pandas → Spark → SQL)")
    print("✅ Self-documenting analytics with labels and descriptions")
    
    print(f"\n💡 Next Steps:")
    print("  • Implement includes functionality for modular YAML files")
    print("  • Add time-series analysis for fighter career progression")
    print("  • Create advanced metrics like P4P rankings")
    print("  • Build real-time fight night analytics")


if __name__ == "__main__":
    main()