"""
Main Copper Dashboard

Provides the core dashboard interface with model selection, query building,
and visualization controls.
"""

import streamlit as st
import pandas as pd
from typing import Dict, List, Optional, Any
from pathlib import Path

from copper_interface import CopperInterface
from charts import ChartManager
from components.filters import FilterManager


class CopperDashboard:
    """Main dashboard class for Copper data exploration."""
    
    def __init__(self):
        self.interface = CopperInterface()
        self.chart_manager = ChartManager()
        self.filter_manager = FilterManager()
        
        # Initialize session state
        if 'selected_model' not in st.session_state:
            st.session_state.selected_model = None
        if 'selected_dimensions' not in st.session_state:
            st.session_state.selected_dimensions = []
        if 'selected_measures' not in st.session_state:
            st.session_state.selected_measures = []
        if 'active_filters' not in st.session_state:
            st.session_state.active_filters = {}
        if 'model_data' not in st.session_state:
            st.session_state.model_data = None
        if 'loaded_model' not in st.session_state:
            st.session_state.loaded_model = None
    
    def render(self):
        """Render the complete dashboard."""
        # Sidebar for model selection and query building
        self._render_sidebar()
        
        # Main content area
        if st.session_state.selected_model:
            self._render_main_content()
        else:
            self._render_welcome()
    
    def _render_sidebar(self):
        """Render the sidebar with model selection and query controls."""
        with st.sidebar:
            st.header("🔧 Query Builder")
            
            # Model Selection
            self._render_model_selection()
            
            # If model is loaded, show query controls  
            if st.session_state.selected_model and st.session_state.loaded_model:
                # Ensure interface has the session state data
                if self.interface.model is None:
                    self.interface.model = st.session_state.loaded_model
                if self.interface.data is None and st.session_state.model_data is not None:
                    self.interface.data = st.session_state.model_data
                st.divider()
                self._render_dimension_selection()
                
                st.divider()
                self._render_measure_selection()
                
                st.divider()
                self._render_filter_controls()
                
                st.divider()
                self._render_query_actions()
    
    def _render_model_selection(self):
        """Render model selection dropdown."""
        st.subheader("📊 Data Model")
        
        # Get available models
        available_models = self.interface.get_available_models()
        
        if not available_models:
            st.warning("No semantic models found in examples/ufc/ directory")
            return
        
        # Debug info
        st.caption(f"Found {len(available_models)} models: {list(available_models.keys())}")
        
        # Model selection
        model_names = list(available_models.keys())
        current_index = 0
        
        if st.session_state.selected_model:
            current_model_name = None
            for name, path in available_models.items():
                if path == st.session_state.selected_model:
                    current_model_name = name
                    break
            if current_model_name and current_model_name in model_names:
                current_index = model_names.index(current_model_name)
        
        selected_model_name = st.selectbox(
            "Choose a semantic model:",
            options=model_names,
            index=current_index,
            help="Select a semantic model to explore. Each model provides different dimensions and measures for analysis.",
            key="model_selector"
        )
        
        selected_model_path = available_models[selected_model_name]
        
        # Load model only if changed
        if selected_model_path != st.session_state.selected_model:
            
            # Create a progress bar for better UX
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            try:
                # Step 1: Load model
                status_text.text("🔄 Loading semantic model...")
                progress_bar.progress(25)
                
                model = self.interface.load_semantic_model(selected_model_path)
                self.interface.model = model
                
                status_text.text(f"✅ Model loaded: {model.name}")
                progress_bar.progress(50)
                
                # Step 2: Load data
                status_text.text("🔄 Loading data...")
                progress_bar.progress(75)
                
                data = self.interface.load_data(model, selected_model_path)
                
                status_text.text(f"✅ Data loaded: {len(data):,} rows")
                progress_bar.progress(100)
                
                # Update session state
                st.session_state.selected_model = selected_model_path
                st.session_state.model_data = data
                st.session_state.loaded_model = model
                st.session_state.selected_dimensions = []
                st.session_state.selected_measures = []
                st.session_state.active_filters = {}
                
                # Update interface
                self.interface.model = model
                self.interface.data = data
                
                # Clear progress indicators
                progress_bar.empty()
                status_text.empty()
                
                st.success(f"🎉 Ready! Model: {model.name} ({len(data):,} rows)")
                
            except Exception as e:
                # Clear progress indicators
                progress_bar.empty()
                status_text.empty()
                
                st.error(f"❌ Failed to load model: {str(e)}")
                
                # Provide helpful error messages and solutions
                error_msg = str(e).lower()
                if "file not found" in error_msg or "no such file" in error_msg:
                    st.warning("📁 **File Not Found Error**")
                    st.info("🔧 **Troubleshooting Steps:**\n1. Check if the file path is correct\n2. Ensure the file exists in the examples/ufc directory\n3. Verify file permissions")
                elif "yaml" in error_msg or "parse" in error_msg:
                    st.warning("📝 **YAML Parsing Error**")
                    st.info("🔧 **Troubleshooting Steps:**\n1. Check YAML syntax\n2. Ensure proper indentation\n3. Verify all quotes are closed")
                elif "datasource" in error_msg:
                    st.warning("🗺️ **Data Source Error**")
                    st.info("🔧 **Troubleshooting Steps:**\n1. Check if CSV file exists\n2. Verify datasource configuration\n3. Ensure file path is relative to model file")
                else:
                    st.warning("⚠️ **General Loading Error**")
                    st.info("🔧 **Troubleshooting Steps:**\n1. Try refreshing the page\n2. Check file permissions\n3. Contact support if issue persists")
                
                # Expandable debug info
                with st.expander("🐛 Debug Information", expanded=False):
                    st.write("**Error Details:**")
                    st.code(str(e))
                    
                    st.write("**File Information:**")
                    st.write(f"- Model path: {selected_model_path}")
                    st.write(f"- Path exists: {Path(selected_model_path).exists()}")
                    
                    if Path(selected_model_path).exists():
                        st.write(f"- File size: {Path(selected_model_path).stat().st_size} bytes")
                        
                        # Show file content preview
                        try:
                            with open(selected_model_path, 'r') as f:
                                content = f.read()[:500]
                                st.write("**File Preview (first 500 chars):**")
                                st.code(content, language='yaml')
                        except Exception as file_err:
                            st.write(f"- Could not read file: {file_err}")
                    
                    st.write("**Full Traceback:**")
                    import traceback
                    st.code(traceback.format_exc())
        
        # Show model info
        if self.interface.model:
            with st.expander("ℹ️ Model Info", expanded=False):
                st.write(f"**Name:** {self.interface.model.name}")
                if hasattr(self.interface.model, 'description') and self.interface.model.description:
                    st.write(f"**Description:** {self.interface.model.description}")
                st.write(f"**Dimensions:** {len(self.interface.model.dimensions)}")
                st.write(f"**Measures:** {len(self.interface.model.measures)}")
                if self.interface.data is not None:
                    st.write(f"**Data Rows:** {len(self.interface.data):,}")
    
    def _render_dimension_selection(self):
        """Render dimension selection controls."""
        st.subheader("📏 Dimensions")
        
        dimensions = self.interface.get_dimensions()
        if not dimensions:
            st.info("No dimensions available")
            return
        
        # Dimension multiselect
        dimension_options = list(dimensions.keys())
        dimension_labels = []
        
        for dim_name in dimension_options:
            dim_info = self.interface.get_dimension_info(dim_name)
            label = dim_info.get('label', dim_name)
            dimension_labels.append(f"{label} ({dim_name})" if label != dim_name else dim_name)
        
        selected_indices = []
        for i, dim_name in enumerate(dimension_options):
            if dim_name in st.session_state.selected_dimensions:
                selected_indices.append(i)
        
        selected_dimension_indices = st.multiselect(
            "Select dimensions:",
            options=range(len(dimension_options)),
            default=selected_indices,
            format_func=lambda x: dimension_labels[x],
            help="Dimensions group your data into categories. Start with 1-2 dimensions for clearer results. Try 'Weight Class' or 'Finish Type' for interesting insights."
        )
        
        st.session_state.selected_dimensions = [dimension_options[i] for i in selected_dimension_indices]
        
        # Show dimension details
        if st.session_state.selected_dimensions:
            with st.expander("📋 Dimension Details", expanded=False):
                for dim_name in st.session_state.selected_dimensions:
                    dim_info = self.interface.get_dimension_info(dim_name)
                    st.write(f"**{dim_info.get('label', dim_name)}**")
                    if dim_info.get('description'):
                        st.caption(dim_info['description'])
                    st.code(dim_info.get('expression', ''), language='sql')
    
    def _render_measure_selection(self):
        """Render measure selection controls."""
        st.subheader("📊 Measures")
        
        measures = self.interface.get_measures()
        if not measures:
            st.info("No measures available")
            return
        
        # Measure multiselect
        measure_options = list(measures.keys())
        measure_labels = []
        
        for measure_name in measure_options:
            measure_info = self.interface.get_measure_info(measure_name)
            label = measure_info.get('label', measure_name)
            measure_labels.append(f"{label} ({measure_name})" if label != measure_name else measure_name)
        
        selected_indices = []
        for i, measure_name in enumerate(measure_options):
            if measure_name in st.session_state.selected_measures:
                selected_indices.append(i)
        
        selected_measure_indices = st.multiselect(
            "Select measures:",
            options=range(len(measure_options)),
            default=selected_indices,
            format_func=lambda x: measure_labels[x],
            help="Measures are calculated values like counts, averages, or sums. Try 'Total Fights' for fight counts or 'Average Fight Rounds' for duration analysis."
        )
        
        st.session_state.selected_measures = [measure_options[i] for i in selected_measure_indices]
        
        # Show measure details
        if st.session_state.selected_measures:
            with st.expander("🔢 Measure Details", expanded=False):
                for measure_name in st.session_state.selected_measures:
                    measure_info = self.interface.get_measure_info(measure_name)
                    st.write(f"**{measure_info.get('label', measure_name)}**")
                    if measure_info.get('description'):
                        st.caption(measure_info['description'])
                    st.code(measure_info.get('expression', ''), language='sql')
    
    def _render_filter_controls(self):
        """Render filter controls."""
        st.subheader("🔍 Filters")
        
        if self.interface.data is None:
            st.info("Load data to set filters")
            return
        
        # Get filterable columns (avoid duplicates)
        filterable_columns = []
        added_columns = set()
        
        # Add dimension columns first
        for dim_name in self.interface.get_dimensions().keys():
            dim_info = self.interface.get_dimension_info(dim_name)
            if 'unique_values' in dim_info:
                filterable_columns.append((dim_name, dim_info))
                added_columns.add(dim_name)
        
        # Add additional data columns only if not already added
        for col in ['weight_class', 'method', 'gender', 'title_fight']:
            if col not in added_columns and col in self.interface.data.columns:
                unique_vals = self.interface.data[col].unique()
                if len(unique_vals) < 50:  # Only show if reasonable number of options
                    filterable_columns.append((col, {
                        'name': col,
                        'label': col.replace('_', ' ').title(),
                        'unique_values': sorted([str(v) for v in unique_vals if pd.notna(v)])
                    }))
                    added_columns.add(col)
        
        if not filterable_columns:
            st.info("No filterable dimensions available")
            return
        
        # Render filter controls with stable keys
        for col_name, col_info in filterable_columns:
            unique_values = col_info.get('unique_values', [])
            if unique_values:
                label = col_info.get('label', col_name)
                
                current_filter = st.session_state.active_filters.get(col_name, [])
                selected_values = st.multiselect(
                    f"Filter by {label}:",
                    options=unique_values,
                    default=current_filter,
                    key=f"filter_{col_name}",
                    help=f"Filter data by {label}. Multiple selections allowed."
                )
                
                # Update session state based on widget value
                if selected_values:
                    st.session_state.active_filters[col_name] = selected_values
                elif col_name in st.session_state.active_filters:
                    del st.session_state.active_filters[col_name]
    
    def _render_query_actions(self):
        """Render query action buttons."""
        st.subheader("🚀 Actions")
        
        # Query button - enable if dimensions, measures, or filters are selected
        can_query = (st.session_state.selected_dimensions or 
                    st.session_state.selected_measures or
                    st.session_state.active_filters)
        
        if st.button("Execute Query", disabled=not can_query, type="primary", help="Run the query with selected dimensions and measures"):
            st.session_state.query_executed = True
            # Don't rerun here, let the main content handle it
        
        # Show query summary
        if st.session_state.selected_dimensions or st.session_state.selected_measures:
            with st.expander("📋 Current Query", expanded=False):
                if st.session_state.selected_dimensions:
                    st.write("**Dimensions:**", ", ".join(st.session_state.selected_dimensions))
                if st.session_state.selected_measures:
                    st.write("**Measures:**", ", ".join(st.session_state.selected_measures))
                if st.session_state.active_filters:
                    st.write("**Filters:**")
                    for filter_col, filter_vals in st.session_state.active_filters.items():
                        if isinstance(filter_vals, list) and filter_vals:
                            st.write(f"  • {filter_col}: {', '.join(map(str, filter_vals))}")
                        elif filter_vals:
                            st.write(f"  • {filter_col}: {filter_vals}")
        
        # Clear selections
        if st.button("Clear All", help="Clear all selections and filters"):
            st.session_state.selected_dimensions = []
            st.session_state.selected_measures = []
            st.session_state.active_filters = {}
            st.session_state.query_executed = False
            
            # Clear all filter widget states
            filter_keys = [key for key in st.session_state.keys() if key.startswith('filter_')]
            for key in filter_keys:
                del st.session_state[key]
            
            st.success("🧽 Cleared all selections!")
            st.rerun()
    
    def _render_main_content(self):
        """Render the main content area with charts and data."""
        # Check if query should be executed
        if (hasattr(st.session_state, 'query_executed') and 
            st.session_state.query_executed and 
            (st.session_state.selected_dimensions or st.session_state.selected_measures or st.session_state.active_filters)):
            
            # Execute query with progress indicator
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            try:
                status_text.text("🔄 Building query...")
                progress_bar.progress(25)
                
                status_text.text("🔄 Executing query...")
                progress_bar.progress(50)
                
                result_df = self.interface.execute_query(
                    dimensions=st.session_state.selected_dimensions,
                    measures=st.session_state.selected_measures,
                    filters=st.session_state.active_filters
                )
                
                status_text.text("🔄 Processing results...")
                progress_bar.progress(75)
                
                if not result_df.empty:
                    status_text.text("✅ Query completed successfully!")
                    progress_bar.progress(100)
                    
                    # Clear progress indicators
                    progress_bar.empty()
                    status_text.empty()
                    
                    self._render_results(result_df)
                    
                    # Reset query_executed to allow re-execution
                    st.session_state.query_executed = False
                else:
                    # Clear progress indicators
                    progress_bar.empty()
                    status_text.empty()
                    
                    st.warning("Query returned no results. Try adjusting your filters or selection.")
                    st.session_state.query_executed = False
                    
            except Exception as e:
                # Clear progress indicators
                progress_bar.empty()
                status_text.empty()
                
                st.error(f"❌ Query execution failed: {str(e)}")
                
                # Provide helpful error messages
                error_msg = str(e).lower()
                if "no data" in error_msg or "empty" in error_msg:
                    st.warning("📉 **No Data Available**")
                    st.info("🔧 **Suggestions:**\n1. Check if filters are too restrictive\n2. Try different dimension/measure combinations\n3. Verify data was loaded correctly")
                elif "column" in error_msg or "key" in error_msg:
                    st.warning("📊 **Column Reference Error**")
                    st.info("🔧 **Suggestions:**\n1. Check dimension/measure expressions\n2. Verify column names match data\n3. Try simpler queries first")
                elif "calculation" in error_msg or "aggregation" in error_msg:
                    st.warning("🧮 **Calculation Error**")
                    st.info("🔧 **Suggestions:**\n1. Check measure expressions\n2. Verify data types are compatible\n3. Try different aggregation functions")
                else:
                    st.warning("⚠️ **Query Execution Error**")
                    st.info("🔧 **Suggestions:**\n1. Try a simpler query\n2. Check your selections\n3. Clear filters and try again")
                
                with st.expander("🐛 Error Details", expanded=False):
                    import traceback
                    st.code(traceback.format_exc())
                
                st.session_state.query_executed = False
        else:
            self._render_query_prompt()
    
    def _render_results(self, result_df: pd.DataFrame):
        """Render query results with charts and data table."""
        st.header("📈 Results")
        
        # Results summary
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Rows", len(result_df))
        with col2:
            st.metric("Dimensions", len(st.session_state.selected_dimensions))
        with col3:
            st.metric("Measures", len(st.session_state.selected_measures))
        
        # Chart tabs
        chart_tabs = ["📊 Charts", "📋 Data Table"]
        tab1, tab2 = st.tabs(chart_tabs)
        
        with tab1:
            self.chart_manager.render_charts(
                result_df, 
                st.session_state.selected_dimensions,
                st.session_state.selected_measures
            )
        
        with tab2:
            st.subheader("📋 Data Table")
            st.dataframe(result_df, use_container_width=True)
            
            # Download button
            csv = result_df.to_csv(index=False)
            st.download_button(
                label="Download CSV",
                data=csv,
                file_name="copper_query_results.csv",
                mime="text/csv"
            )
    
    def _render_query_prompt(self):
        """Render prompt to build and execute a query."""
        st.header("🎯 Build Your Query")
        
        if not st.session_state.selected_dimensions and not st.session_state.selected_measures:
            st.info("""
            👈 **Get Started:**
            1. Select **dimensions** to group your data
            2. Select **measures** to calculate values
            3. Add **filters** to focus your analysis
            4. Click **Execute Query** to see results
            """)
        else:
            st.info("👈 Click **Execute Query** in the sidebar to see your results!")
        
        # Show current selections
        if st.session_state.selected_dimensions or st.session_state.selected_measures:
            st.subheader("📋 Current Selection")
            
            if st.session_state.selected_dimensions:
                st.write("**Dimensions:**", ", ".join(st.session_state.selected_dimensions))
            
            if st.session_state.selected_measures:
                st.write("**Measures:**", ", ".join(st.session_state.selected_measures))
            
            if st.session_state.active_filters:
                st.write("**Filters:**")
                for filter_col, filter_vals in st.session_state.active_filters.items():
                    st.write(f"  • {filter_col}: {', '.join(filter_vals)}")
    
    def _render_welcome(self):
        """Render welcome screen when no model is selected."""
        st.header("👋 Welcome to Copper Data Explorer")
        
        st.markdown("""
        **Copper** is a universal semantic layer that lets you define metrics once and run them anywhere.
        
        ### 🚀 Getting Started
        1. **Select a semantic model** from the sidebar
        2. **Choose dimensions and measures** to explore
        3. **Apply filters** to focus your analysis
        4. **Execute queries** and visualize results
        
        ### 📊 Available Models
        Explore UFC fight analysis with real MMA data including:
        - Fight outcomes and methods
        - Weight classes and fighter statistics
        - Event history and performance metrics
        """)
        
        # Show available models with more detail
        available_models = self.interface.get_available_models()
        if available_models:
            st.subheader("Available Models")
            
            for model_name, model_path in available_models.items():
                with st.container():
                    col1, col2 = st.columns([3, 1])
                    
                    with col1:
                        st.write(f"• **{model_name}**")
                        
                        # Add model descriptions
                        descriptions = {
                            "Fight Analysis": "Analyze fight outcomes, methods, and finish rates",
                            "Event Analytics": "Event-level metrics and attendance data",
                            "Fighter Performance": "Individual fighter statistics and career metrics", 
                            "Betting Analysis": "Betting odds and outcome predictions"
                        }
                        
                        if model_name in descriptions:
                            st.caption(descriptions[model_name])
                    
                    with col2:
                        # Quick load button
                        if st.button(f"Load {model_name}", key=f"quick_load_{model_name}", help=f"Quickly load the {model_name} model"):
                            st.session_state.selected_model = model_path
                            st.rerun()
        
        st.info("👈 Select a model from the sidebar or use the quick load buttons above to begin exploring!")
        
        # Tips and tricks
        with st.expander("💡 Tips & Tricks", expanded=False):
            st.markdown("""
            **Getting the Most Out of Copper:**
            
            📊 **Query Building:**
            - Start with 1-2 dimensions for clearer visualizations
            - Add measures that complement your dimensions
            - Use filters to focus on specific data subsets
            
            📈 **Visualization:**
            - Bar charts work great for categorical data
            - Line charts show trends over time
            - Pie charts are perfect for proportions
            
            🔍 **Analysis Tips:**
            - Combine related dimensions (e.g., weight class + gender)
            - Filter by title fights for championship analysis
            - Use finish method to analyze fighting styles
            
            ⚡ **Performance:**
            - Limit results for faster queries on large datasets
            - Use specific filters rather than broad selections
            - Start simple and add complexity gradually
            """)