#!/usr/bin/env python3
"""
UI Test Script

Tests the Copper UI components without requiring Streamlit runtime.
"""

import sys
from pathlib import Path

# Add src to path for imports
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from copper_interface import CopperInterface
from charts import ChartManager
import pandas as pd


def test_interface():
    """Test the CopperInterface functionality."""
    print("🧪 Testing CopperInterface...")
    
    interface = CopperInterface()
    
    # Test model discovery
    models = interface.get_available_models()
    print(f"✅ Found {len(models)} models: {list(models.keys())}")
    
    if not models:
        print("❌ No models found")
        return False
    
    # Test model loading
    model_name, model_path = next(iter(models.items()))
    print(f"🔄 Testing model: {model_name}")
    
    try:
        # Load model (this will show warnings about streamlit cache)
        model = interface.load_semantic_model(model_path)
        print(f"✅ Loaded model: {model.name}")
        
        # Load data
        interface.model = model
        data = interface.load_data(model)
        print(f"✅ Loaded data: {len(data)} rows, {len(data.columns)} columns")
        
        # Test metadata extraction
        dimensions = interface.get_dimensions()
        measures = interface.get_measures()
        print(f"✅ Found {len(dimensions)} dimensions, {len(measures)} measures")
        
        # Test query execution
        if dimensions and measures:
            dim_names = list(dimensions.keys())[:2]  # Take first 2 dimensions
            measure_names = list(measures.keys())[:2]  # Take first 2 measures
            
            print(f"🔄 Testing query with {dim_names} and {measure_names}")
            interface.data = data
            result = interface.execute_query(dim_names, measure_names)
            print(f"✅ Query executed: {len(result)} result rows")
            
            return True, result, dim_names, measure_names
        else:
            print("⚠️  No dimensions or measures found")
            return True, None, [], []
            
    except Exception as e:
        print(f"❌ Error testing interface: {e}")
        import traceback
        traceback.print_exc()
        return False, None, [], []


def test_charts(result_df, dimensions, measures):
    """Test chart creation functionality."""
    if result_df is None or result_df.empty:
        print("⚠️  Skipping chart tests - no data")
        return
    
    print("\n🧪 Testing ChartManager...")
    
    chart_manager = ChartManager()
    
    try:
        # Test chart suggestions
        suggestions = chart_manager._suggest_charts(result_df, dimensions, measures)
        print(f"✅ Generated {len(suggestions)} chart suggestions: {list(suggestions.keys())}")
        
        # Test chart creation
        for chart_type, config in suggestions.items():
            try:
                fig = chart_manager._create_chart(result_df, chart_type, config)
                if fig:
                    print(f"✅ Created {chart_type} chart successfully")
                else:
                    print(f"⚠️  Could not create {chart_type} chart")
            except Exception as e:
                print(f"❌ Error creating {chart_type} chart: {e}")
        
    except Exception as e:
        print(f"❌ Error testing charts: {e}")
        import traceback
        traceback.print_exc()


def main():
    """Run all UI tests."""
    print("🚀 Starting Copper UI Tests\n")
    
    # Test interface
    success, result_df, dimensions, measures = test_interface()
    
    if not success:
        print("\n❌ Interface tests failed")
        return
    
    # Test charts
    test_charts(result_df, dimensions, measures)
    
    print("\n🎉 UI tests completed!")
    
    if result_df is not None and not result_df.empty:
        print(f"\n📊 Sample Results:")
        print(result_df.head())


if __name__ == "__main__":
    main()