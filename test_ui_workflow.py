#!/usr/bin/env python3
"""
Copper UI Workflow Test

This script tests the complete UI workflow without running Streamlit.
"""

import sys
from pathlib import Path

# Add ui to path
ui_path = Path(__file__).parent / "ui"
sys.path.insert(0, str(ui_path))

def test_workflow():
    """Test the complete workflow."""
    print("🧪 Testing Copper UI Workflow")
    print("=" * 50)
    
    try:
        # Test 1: Import copper interface
        print("1️⃣ Testing imports...")
        from ui.copper_interface import CopperInterface
        from ui.charts import ChartManager
        from ui.components.filters import FilterManager
        print("   ✅ All imports successful")
        
        # Test 2: Create interface and load models
        print("\n2️⃣ Testing model discovery...")
        interface = CopperInterface()
        models = interface.get_available_models()
        print(f"   ✅ Found {len(models)} models: {list(models.keys())}")
        
        if not models:
            print("   ❌ No models found!")
            return False
        
        # Test 3: Load first model
        print("\n3️⃣ Testing model loading...")
        first_model_path = list(models.values())[0]
        model = interface.load_semantic_model(first_model_path)
        print(f"   ✅ Model loaded: {model.name}")
        print(f"   📏 Dimensions: {len(model.dimensions)}")
        print(f"   📊 Measures: {len(model.measures)}")
        
        # Test 4: Load data
        print("\n4️⃣ Testing data loading...")
        data = interface.load_data(model, first_model_path)
        print(f"   ✅ Data loaded: {data.shape[0]:,} rows, {data.shape[1]} columns")
        
        # Test 5: Set up interface for querying
        print("\n5️⃣ Testing interface setup...")
        interface.model = model
        interface.data = data
        print("   ✅ Interface configured")
        
        # Test 6: Test dimension and measure info
        print("\n6️⃣ Testing metadata access...")
        dimensions = interface.get_dimensions()
        measures = interface.get_measures()
        print(f"   📏 Available dimensions: {list(dimensions.keys())}")
        print(f"   📊 Available measures: {list(measures.keys())}")
        
        # Test dimension info
        if dimensions:
            first_dim = list(dimensions.keys())[0]
            dim_info = interface.get_dimension_info(first_dim)
            print(f"   ℹ️ Dimension '{first_dim}' info: {dim_info.get('type', 'unknown')} type")
        
        # Test measure info
        if measures:
            first_measure = list(measures.keys())[0]
            measure_info = interface.get_measure_info(first_measure)
            print(f"   ℹ️ Measure '{first_measure}' info: {measure_info.get('type', 'unknown')} type")
        
        # Test 7: Execute queries
        print("\n7️⃣ Testing query execution...")
        
        # Simple dimension query
        if dimensions:
            dim_name = list(dimensions.keys())[0]
            result = interface.execute_query([dim_name], [])
            print(f"   ✅ Dimension query: {result.shape[0]} groups")
        
        # Measure-only query
        if measures:
            measure_name = list(measures.keys())[0]
            result = interface.execute_query([], [measure_name])
            print(f"   ✅ Measure query: {result.shape}")
        
        # Combined query
        if dimensions and measures:
            dim_name = list(dimensions.keys())[0]
            measure_name = list(measures.keys())[0]
            result = interface.execute_query([dim_name], [measure_name])
            print(f"   ✅ Combined query: {result.shape}")
            print(f"   📋 Result columns: {list(result.columns)}")
            
            if not result.empty:
                print("   📊 Sample results:")
                print(result.head(3).to_string(index=False))
        
        # Test 8: Chart manager
        print("\n8️⃣ Testing chart manager...")
        chart_manager = ChartManager()
        print("   ✅ Chart manager created")
        
        # Test 9: Filter manager
        print("\n9️⃣ Testing filter manager...")
        filter_manager = FilterManager()
        print("   ✅ Filter manager created")
        
        print("\n🎉 All tests passed! The UI workflow is working correctly.")
        print("\n🚀 You can now start the UI with:")
        print("   python start_ui.py")
        print("   or")
        print("   uv run streamlit run ui/app.py")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        print("\n🐛 Full traceback:")
        print(traceback.format_exc())
        return False

if __name__ == "__main__":
    success = test_workflow()
    sys.exit(0 if success else 1)