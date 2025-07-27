#!/usr/bin/env python3
"""
Test script to validate UI fixes
"""

import sys
from pathlib import Path

# Add UI and src to path
ui_path = Path(__file__).parent / "ui"
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(ui_path))
sys.path.insert(0, str(src_path))

def test_copper_interface():
    """Test the CopperInterface functionality."""
    print("🔧 Testing CopperInterface...")
    
    from copper_interface import CopperInterface
    
    # Create interface
    interface = CopperInterface()
    print("✅ Interface created")
    
    # Test model discovery
    models = interface.get_available_models()
    print(f"✅ Found {len(models)} models: {list(models.keys())}")
    
    # Test loading first model
    model_name, model_path = next(iter(models.items()))
    print(f"🔄 Loading model: {model_name}")
    
    try:
        # Load model
        model = interface.load_semantic_model(model_path)
        interface.model = model
        print(f"✅ Model loaded: {model.name}")
        
        # Load data
        data = interface.load_data(model, model_path)
        interface.data = data
        print(f"✅ Data loaded: {len(data)} rows")
        
        # Test getting dimensions and measures
        dimensions = interface.get_dimensions()
        measures = interface.get_measures()
        print(f"✅ Found {len(dimensions)} dimensions, {len(measures)} measures")
        
        # Test dimension info
        if dimensions:
            dim_name = next(iter(dimensions.keys()))
            dim_info = interface.get_dimension_info(dim_name)
            print(f"✅ Dimension info for '{dim_name}': {dim_info.get('label')}")
        
        # Test measure info
        if measures:
            measure_name = next(iter(measures.keys()))
            measure_info = interface.get_measure_info(measure_name)
            print(f"✅ Measure info for '{measure_name}': {measure_info.get('label')}")
        
        # Test simple query execution
        if dimensions and measures:
            dim_names = list(dimensions.keys())[:1]  # Take first dimension
            measure_names = list(measures.keys())[:1]  # Take first measure
            
            print(f"🔄 Testing query: dimensions={dim_names}, measures={measure_names}")
            result = interface.execute_query(dim_names, measure_names)
            print(f"✅ Query executed: {len(result)} result rows")
            
            if not result.empty:
                print(f"   Columns: {list(result.columns)}")
                print(f"   Sample: {result.head(3).to_dict('records')}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_dashboard_components():
    """Test dashboard components."""
    print("\n📊 Testing Dashboard Components...")
    
    try:
        from charts import ChartManager
        chart_manager = ChartManager()
        print("✅ ChartManager created")
        
        from components.filters import FilterManager
        filter_manager = FilterManager()
        print("✅ FilterManager created")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Run all tests."""
    print("🧪 Testing Copper UI Fixes\n")
    
    results = []
    
    # Test CopperInterface
    results.append(test_copper_interface())
    
    # Test Dashboard Components
    results.append(test_dashboard_components())
    
    # Summary
    print(f"\n📋 Test Summary:")
    print(f"✅ Passed: {sum(results)}")
    print(f"❌ Failed: {len(results) - sum(results)}")
    
    if all(results):
        print("\n🎉 All tests passed! UI should be working correctly.")
    else:
        print("\n⚠️  Some tests failed. Check the errors above.")
    
    return all(results)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)