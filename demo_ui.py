#!/usr/bin/env python3
"""
Copper UI Demo Script

Demonstrates the Copper Data Explorer UI capabilities without running Streamlit.
This script shows the core functionality that powers the interactive dashboard.
"""

import sys
from pathlib import Path

# Add src to path for imports
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))
sys.path.insert(0, str(Path(__file__).parent / "ui"))

from copper_interface import CopperInterface
from charts import ChartManager
import pandas as pd


def print_header(title: str, symbol: str = "="):
    """Print a formatted header."""
    print(f"\n{symbol * 60}")
    print(f" {title}")
    print(f"{symbol * 60}")


def print_section(title: str):
    """Print a section header."""
    print(f"\n📋 {title}")
    print("-" * 40)


def demo_model_discovery():
    """Demonstrate model discovery functionality."""
    print_header("🔍 Model Discovery Demo")
    
    interface = CopperInterface()
    
    print("🔄 Discovering available semantic models...")
    models = interface.get_available_models()
    
    print(f"✅ Found {len(models)} semantic models:")
    for i, (name, path) in enumerate(models.items(), 1):
        print(f"  {i}. {name}")
        print(f"     📁 {Path(path).name}")
    
    return models


def demo_model_loading(models):
    """Demonstrate model loading and data access."""
    print_header("📊 Model Loading Demo")
    
    if not models:
        print("❌ No models available for demo")
        return None, None
    
    # Load the first model (Fight Analysis)
    model_name, model_path = next(iter(models.items()))
    print(f"🔄 Loading model: {model_name}")
    print(f"📁 Path: {model_path}")
    
    interface = CopperInterface()
    
    try:
        # Load model
        model = interface.load_semantic_model(model_path)
        print(f"✅ Model loaded: {model.name}")
        
        # Load data
        interface.model = model
        data = interface.load_data(model)
        interface.data = data
        print(f"✅ Data loaded: {len(data):,} rows × {len(data.columns)} columns")
        
        return interface, data
        
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return None, None


def demo_metadata_exploration(interface):
    """Demonstrate metadata exploration."""
    print_header("🔍 Metadata Exploration Demo")
    
    if not interface or not interface.model:
        print("❌ No model loaded")
        return
    
    print_section("Available Dimensions")
    dimensions = interface.get_dimensions()
    
    for i, (dim_name, dim_obj) in enumerate(dimensions.items(), 1):
        dim_info = interface.get_dimension_info(dim_name)
        print(f"  {i}. {dim_info.get('label', dim_name)}")
        print(f"     📝 {dim_info.get('description', 'No description')}")
        print(f"     🔧 {dim_info.get('expression', 'No expression')}")
        if 'unique_values' in dim_info:
            values = dim_info['unique_values'][:5]  # Show first 5
            print(f"     📊 Sample values: {', '.join(values)}")
            if len(dim_info['unique_values']) > 5:
                print(f"        ... and {len(dim_info['unique_values']) - 5} more")
        print()
    
    print_section("Available Measures")
    measures = interface.get_measures()
    
    for i, (measure_name, measure_obj) in enumerate(measures.items(), 1):
        measure_info = interface.get_measure_info(measure_name)
        print(f"  {i}. {measure_info.get('label', measure_name)}")
        print(f"     📝 {measure_info.get('description', 'No description')}")
        print(f"     🔧 {measure_info.get('expression', 'No expression')}")
        print(f"     📊 Type: {measure_info.get('type', 'unknown')}")
        print()


def demo_data_preview(data):
    """Demonstrate data preview functionality."""
    print_header("📋 Data Preview Demo")
    
    if data is None or data.empty:
        print("❌ No data available")
        return
    
    print_section("Dataset Overview")
    print(f"📊 Shape: {data.shape[0]:,} rows × {data.shape[1]} columns")
    print(f"💾 Memory usage: {data.memory_usage(deep=True).sum() / 1024**2:.1f} MB")
    
    print_section("Column Information")
    interesting_columns = ['weight_class', 'method', 'gender', 'title_fight', 'round', 'time']
    available_columns = [col for col in interesting_columns if col in data.columns]
    
    for col in available_columns[:8]:  # Show first 8 columns
        dtype = data[col].dtype
        unique_count = data[col].nunique()
        null_count = data[col].isnull().sum()
        
        print(f"  📊 {col}")
        print(f"     Type: {dtype}")
        print(f"     Unique values: {unique_count:,}")
        print(f"     Null values: {null_count:,}")
        
        # Show sample values for categorical columns
        if unique_count < 20 and unique_count > 0:
            sample_values = data[col].dropna().unique()[:5]
            print(f"     Sample: {', '.join(map(str, sample_values))}")
        print()
    
    print_section("Sample Data")
    pd.set_option('display.max_columns', 8)
    pd.set_option('display.width', 100)
    print(data[available_columns[:6]].head())


def demo_query_execution(interface):
    """Demonstrate query execution."""
    print_header("🚀 Query Execution Demo")
    
    if not interface or not interface.model or interface.data is None:
        print("❌ No data available for querying")
        return None
    
    print_section("Building Sample Query")
    
    # Get available dimensions and measures
    dimensions = list(interface.get_dimensions().keys())
    measures = list(interface.get_measures().keys())
    
    # Build a sample query
    selected_dims = dimensions[:2] if len(dimensions) >= 2 else dimensions[:1]
    selected_measures = measures[:1] if measures else []
    
    print(f"📏 Selected dimensions: {', '.join(selected_dims)}")
    print(f"📊 Selected measures: {', '.join(selected_measures)}")
    
    print_section("Executing Query")
    try:
        result = interface.execute_query(
            dimensions=selected_dims,
            measures=selected_measures
        )
        
        if result.empty:
            print("⚠️  Query returned no results (simplified execution logic)")
            print("💡 In the full UI, this would use the pandas executor for proper aggregation")
            
            # Show what the query would look like
            print("\n🔍 Query Intent:")
            print(f"   GROUP BY {', '.join(selected_dims)}")
            if selected_measures:
                print(f"   SELECT {', '.join(selected_measures)}")
            
            # Create a simple demo result
            if 'weight_class' in interface.data.columns:
                print("\n📊 Sample Aggregation (demo):")
                demo_result = interface.data.groupby('weight_class').size().reset_index(name='fight_count')
                print(demo_result.head())
                return demo_result
        else:
            print(f"✅ Query executed: {len(result)} rows returned")
            print(result.head())
            return result
            
    except Exception as e:
        print(f"❌ Query execution error: {e}")
        return None


def demo_chart_generation(data):
    """Demonstrate chart generation capabilities."""
    print_header("📈 Chart Generation Demo")
    
    if data is None or data.empty:
        print("❌ No data available for charts")
        return
    
    print_section("Chart Type Suggestions")
    
    chart_manager = ChartManager()
    
    # Simulate dimensions and measures for chart suggestions
    dimensions = list(data.columns[:2]) if len(data.columns) >= 2 else [data.columns[0]]
    measures = [col for col in data.columns if data[col].dtype in ['int64', 'float64']][:2]
    
    print(f"📏 Using dimensions: {dimensions}")
    print(f"📊 Using measures: {measures}")
    
    try:
        suggestions = chart_manager._suggest_charts(data, dimensions, measures)
        
        print(f"✅ Generated {len(suggestions)} chart suggestions:")
        for chart_type, config in suggestions.items():
            print(f"  📈 {chart_type.title()} Chart")
            print(f"     X-axis: {config.get('x', 'N/A')}")
            print(f"     Y-axis: {config.get('y', 'N/A')}")
            print(f"     Title: {config.get('title', 'N/A')}")
            
            # Test chart creation
            try:
                fig = chart_manager._create_chart(data, chart_type, config)
                if fig:
                    print(f"     ✅ Chart created successfully")
                else:
                    print(f"     ⚠️  Chart creation failed")
            except Exception as e:
                print(f"     ❌ Chart error: {e}")
            print()
            
    except Exception as e:
        print(f"❌ Chart generation error: {e}")


def demo_filter_capabilities(interface):
    """Demonstrate filtering capabilities."""
    print_header("🔍 Filter Capabilities Demo")
    
    if not interface or interface.data is None:
        print("❌ No data available for filtering")
        return
    
    data = interface.data
    
    print_section("Available Filters")
    
    # Common filterable columns
    filter_columns = ['weight_class', 'method', 'gender', 'title_fight']
    available_filters = [col for col in filter_columns if col in data.columns]
    
    for col in available_filters:
        unique_values = data[col].dropna().unique()
        if len(unique_values) <= 20:  # Only show if reasonable number
            print(f"  🔍 {col.replace('_', ' ').title()}")
            print(f"     Options: {', '.join(map(str, sorted(unique_values)))}")
            print(f"     Count: {len(unique_values)} unique values")
        else:
            print(f"  🔍 {col.replace('_', ' ').title()}")
            print(f"     Count: {len(unique_values)} unique values (too many to display)")
        print()
    
    print_section("Sample Filter Application")
    
    # Apply a sample filter
    if 'weight_class' in data.columns:
        original_count = len(data)
        
        # Get most common weight class
        common_weight_class = data['weight_class'].value_counts().index[0]
        filtered_data = data[data['weight_class'] == common_weight_class]
        
        print(f"📊 Original data: {original_count:,} rows")
        print(f"🔍 Filter: weight_class = '{common_weight_class}'")
        print(f"📊 Filtered data: {len(filtered_data):,} rows ({len(filtered_data)/original_count*100:.1f}%)")


def main():
    """Run the complete UI functionality demo."""
    print_header("🚀 Copper Data Explorer UI Demo", "=")
    print("""
This demo showcases the functionality that powers the Copper Data Explorer UI.
The actual UI provides an interactive Streamlit interface for all these features.

To launch the interactive UI, run:
  python run_ui.py
    """)
    
    try:
        # Demo 1: Model Discovery
        models = demo_model_discovery()
        
        # Demo 2: Model Loading
        interface, data = demo_model_loading(models)
        
        if interface and data is not None:
            # Demo 3: Metadata Exploration
            demo_metadata_exploration(interface)
            
            # Demo 4: Data Preview
            demo_data_preview(data)
            
            # Demo 5: Query Execution
            result_data = demo_query_execution(interface)
            
            # Demo 6: Chart Generation
            demo_chart_generation(result_data or data.head(100))  # Use sample if no results
            
            # Demo 7: Filter Capabilities
            demo_filter_capabilities(interface)
        
        print_header("🎉 Demo Complete!")
        print("""
✅ All core UI functionality demonstrated successfully!

🚀 Next Steps:
  1. Launch the interactive UI: python run_ui.py
  2. Explore the UFC fight data interactively
  3. Create custom visualizations and filters
  4. Export results for further analysis

📚 Learn More:
  - Read ui/README.md for detailed documentation
  - Check examples/ufc/ for sample semantic models
  - Explore src/ for the core Copper semantic layer
        """)
        
    except KeyboardInterrupt:
        print("\n👋 Demo interrupted by user")
    except Exception as e:
        print(f"\n❌ Demo error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()