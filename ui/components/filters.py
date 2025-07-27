"""
Filter Management Components

Provides interactive filtering widgets and filter state management.
"""

import streamlit as st
import pandas as pd
from typing import Dict, List, Any, Optional


class FilterManager:
    """Manages interactive filters for data exploration."""
    
    def __init__(self):
        self.active_filters = {}
    
    def render_filter_panel(self, df: pd.DataFrame, dimensions: Dict[str, Any]) -> Dict[str, Any]:
        """Render a complete filter panel with available dimensions."""
        filters = {}
        
        st.subheader("🔍 Data Filters")
        
        if df.empty:
            st.info("No data available for filtering")
            return filters
        
        # Create filter controls for each dimension
        for dim_name, dim_info in dimensions.items():
            filter_values = self._render_dimension_filter(df, dim_name, dim_info)
            if filter_values:
                filters[dim_name] = filter_values
        
        # Additional column-based filters
        additional_filters = self._render_column_filters(df)
        filters.update(additional_filters)
        
        return filters
    
    def _render_dimension_filter(self, df: pd.DataFrame, dim_name: str, 
                                dim_info: Dict[str, Any]) -> Optional[List[Any]]:
        """Render a filter control for a specific dimension."""
        # Extract column name from dimension expression
        expression = dim_info.get('expression', '')
        
        # Simple case: table.column format
        if '.' in expression:
            _, column = expression.split('.', 1)
        else:
            column = expression
        
        # Check if column exists in dataframe
        if column not in df.columns:
            return None
        
        # Get unique values
        unique_values = df[column].dropna().unique()
        
        # Only show filter if reasonable number of options
        if len(unique_values) > 50:
            return None
        
        # Sort values
        try:
            unique_values = sorted(unique_values)
        except TypeError:
            unique_values = sorted([str(v) for v in unique_values])
        
        # Create filter widget
        label = dim_info.get('label', dim_name)
        description = dim_info.get('description', '')
        
        selected_values = st.multiselect(
            f"Filter by {label}:",
            options=unique_values,
            help=description if description else f"Filter data by {label}",
            key=f"filter_dim_{dim_name}"
        )
        
        return selected_values if selected_values else None
    
    def _render_column_filters(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Render filters for common data columns."""
        filters = {}
        
        # Common filterable columns in UFC data
        common_filters = {
            'weight_class': 'Weight Class',
            'method': 'Finish Method',
            'gender': 'Gender',
            'title_fight': 'Title Fight'
        }
        
        for column, label in common_filters.items():
            if column in df.columns:
                filter_values = self._render_column_filter(df, column, label)
                if filter_values is not None:
                    filters[column] = filter_values
        
        return filters
    
    def _render_column_filter(self, df: pd.DataFrame, column: str, 
                             label: str) -> Optional[Any]:
        """Render a filter control for a specific column."""
        unique_values = df[column].dropna().unique()
        
        # Handle boolean columns
        if df[column].dtype == bool or set(unique_values).issubset({True, False, 0, 1}):
            return self._render_boolean_filter(column, label)
        
        # Handle categorical columns
        if len(unique_values) <= 50:
            return self._render_categorical_filter(df, column, label, unique_values)
        
        # Handle numeric columns
        if pd.api.types.is_numeric_dtype(df[column]):
            return self._render_numeric_filter(df, column, label)
        
        return None
    
    def _render_boolean_filter(self, column: str, label: str) -> Optional[bool]:
        """Render a boolean filter control."""
        options = ["All", "True", "False"]
        
        selected = st.selectbox(
            f"{label}:",
            options=options,
            key=f"filter_bool_{column}"
        )
        
        if selected == "True":
            return True
        elif selected == "False":
            return False
        else:
            return None
    
    def _render_categorical_filter(self, df: pd.DataFrame, column: str, 
                                  label: str, unique_values: List[Any]) -> Optional[List[Any]]:
        """Render a categorical filter control."""
        # Sort values
        try:
            sorted_values = sorted(unique_values)
        except TypeError:
            sorted_values = sorted([str(v) for v in unique_values])
        
        selected_values = st.multiselect(
            f"Filter by {label}:",
            options=sorted_values,
            key=f"filter_cat_{column}"
        )
        
        return selected_values if selected_values else None
    
    def _render_numeric_filter(self, df: pd.DataFrame, column: str, 
                              label: str) -> Optional[tuple]:
        """Render a numeric range filter control."""
        min_val = float(df[column].min())
        max_val = float(df[column].max())
        
        if min_val == max_val:
            return None
        
        selected_range = st.slider(
            f"{label} Range:",
            min_value=min_val,
            max_value=max_val,
            value=(min_val, max_val),
            key=f"filter_num_{column}"
        )
        
        # Return None if full range is selected
        if selected_range == (min_val, max_val):
            return None
        
        return selected_range
    
    def apply_filters(self, df: pd.DataFrame, filters: Dict[str, Any]) -> pd.DataFrame:
        """Apply filters to a dataframe."""
        filtered_df = df.copy()
        
        for column, filter_value in filters.items():
            if filter_value is None:
                continue
            
            try:
                if isinstance(filter_value, list):
                    # Categorical filter
                    if filter_value:  # Only apply if list is not empty
                        filtered_df = filtered_df[filtered_df[column].isin(filter_value)]
                        
                elif isinstance(filter_value, tuple) and len(filter_value) == 2:
                    # Numeric range filter
                    min_val, max_val = filter_value
                    filtered_df = filtered_df[
                        (filtered_df[column] >= min_val) & 
                        (filtered_df[column] <= max_val)
                    ]
                    
                elif isinstance(filter_value, bool):
                    # Boolean filter
                    filtered_df = filtered_df[filtered_df[column] == filter_value]
                    
                else:
                    # Single value filter
                    filtered_df = filtered_df[filtered_df[column] == filter_value]
                    
            except Exception as e:
                st.warning(f"Could not apply filter for {column}: {e}")
                continue
        
        return filtered_df
    
    def render_filter_summary(self, filters: Dict[str, Any]) -> None:
        """Render a summary of active filters."""
        if not filters:
            return
        
        st.subheader("Active Filters")
        
        for column, filter_value in filters.items():
            if filter_value is None:
                continue
            
            if isinstance(filter_value, list):
                if filter_value:
                    st.write(f"**{column}:** {', '.join(map(str, filter_value))}")
            elif isinstance(filter_value, tuple):
                st.write(f"**{column}:** {filter_value[0]} - {filter_value[1]}")
            else:
                st.write(f"**{column}:** {filter_value}")
    
    def clear_filters(self) -> None:
        """Clear all active filters from session state."""
        # Find all filter keys in session state and remove them
        filter_keys = [key for key in st.session_state.keys() if key.startswith('filter_')]
        
        for key in filter_keys:
            del st.session_state[key]
        
        # Also clear the active_filters dict if it exists
        if 'active_filters' in st.session_state:
            st.session_state.active_filters = {}