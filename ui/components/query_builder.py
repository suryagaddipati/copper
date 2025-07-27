"""
Query Builder Component

Provides an advanced interface for building semantic queries with drag-and-drop
functionality and visual query construction.
"""

import streamlit as st
import pandas as pd
from typing import Dict, List, Optional, Any, Tuple


class QueryBuilder:
    """Advanced query builder with visual interface."""
    
    def __init__(self):
        self.query_state = {
            'dimensions': [],
            'measures': [],
            'filters': {},
            'sorts': [],
            'limit': None
        }
    
    def render_query_builder(self, dimensions: Dict[str, Any], measures: Dict[str, Any]) -> Dict[str, Any]:
        """Render the complete query builder interface."""
        st.subheader("🔧 Query Builder")
        
        # Query builder tabs
        tab1, tab2, tab3 = st.tabs(["📏 Dimensions & Measures", "🔍 Filters", "⚙️ Advanced"])
        
        with tab1:
            self._render_dimension_measure_builder(dimensions, measures)
        
        with tab2:
            self._render_filter_builder()
        
        with tab3:
            self._render_advanced_options()
        
        return self._get_query_state()
    
    def _render_dimension_measure_builder(self, dimensions: Dict[str, Any], measures: Dict[str, Any]):
        """Render the main dimension and measure selection interface."""
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📏 Dimensions")
            self._render_dimension_selector(dimensions)
        
        with col2:
            st.markdown("### 📊 Measures")
            self._render_measure_selector(measures)
        
        # Query preview
        if self.query_state['dimensions'] or self.query_state['measures']:
            with st.expander("🔍 Query Preview", expanded=False):
                self._render_query_preview()
    
    def _render_dimension_selector(self, dimensions: Dict[str, Any]):
        """Render dimension selection with metadata."""
        if not dimensions:
            st.info("No dimensions available")
            return
        
        # Available dimensions
        st.markdown("**Available Dimensions:**")
        
        for dim_name, dim_info in dimensions.items():
            label = dim_info.get('label', dim_name)
            description = dim_info.get('description', '')
            dim_type = dim_info.get('type', 'string')
            
            # Dimension card
            with st.container():
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    st.markdown(f"**{label}**")
                    if description:
                        st.caption(description)
                    st.code(f"Type: {dim_type}", language=None)
                
                with col2:
                    # Add/Remove button
                    if dim_name in self.query_state['dimensions']:
                        if st.button("➖", key=f"remove_dim_{dim_name}", help="Remove dimension"):
                            self.query_state['dimensions'].remove(dim_name)
                            st.rerun()
                    else:
                        if st.button("➕", key=f"add_dim_{dim_name}", help="Add dimension"):
                            self.query_state['dimensions'].append(dim_name)
                            st.rerun()
        
        # Selected dimensions
        if self.query_state['dimensions']:
            st.markdown("**Selected Dimensions:**")
            for i, dim_name in enumerate(self.query_state['dimensions']):
                col1, col2, col3 = st.columns([2, 1, 1])
                
                with col1:
                    dim_info = dimensions.get(dim_name, {})
                    label = dim_info.get('label', dim_name)
                    st.markdown(f"{i+1}. {label}")
                
                with col2:
                    # Move up/down
                    if i > 0 and st.button("⬆️", key=f"up_dim_{dim_name}", help="Move up"):
                        self.query_state['dimensions'][i], self.query_state['dimensions'][i-1] = \
                            self.query_state['dimensions'][i-1], self.query_state['dimensions'][i]
                        st.rerun()
                
                with col3:
                    if i < len(self.query_state['dimensions']) - 1 and st.button("⬇️", key=f"down_dim_{dim_name}", help="Move down"):
                        self.query_state['dimensions'][i], self.query_state['dimensions'][i+1] = \
                            self.query_state['dimensions'][i+1], self.query_state['dimensions'][i]
                        st.rerun()
    
    def _render_measure_selector(self, measures: Dict[str, Any]):
        """Render measure selection with metadata."""
        if not measures:
            st.info("No measures available")
            return
        
        # Available measures
        st.markdown("**Available Measures:**")
        
        for measure_name, measure_info in measures.items():
            label = measure_info.get('label', measure_name)
            description = measure_info.get('description', '')
            measure_type = measure_info.get('type', 'number')
            expression = measure_info.get('expression', '')
            
            # Measure card
            with st.container():
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    st.markdown(f"**{label}**")
                    if description:
                        st.caption(description)
                    st.code(f"Type: {measure_type}", language=None)
                    if expression:
                        with st.expander("📝 Expression", expanded=False):
                            st.code(expression, language='sql')
                
                with col2:
                    # Add/Remove button
                    if measure_name in self.query_state['measures']:
                        if st.button("➖", key=f"remove_measure_{measure_name}", help="Remove measure"):
                            self.query_state['measures'].remove(measure_name)
                            st.rerun()
                    else:
                        if st.button("➕", key=f"add_measure_{measure_name}", help="Add measure"):
                            self.query_state['measures'].append(measure_name)
                            st.rerun()
        
        # Selected measures
        if self.query_state['measures']:
            st.markdown("**Selected Measures:**")
            for i, measure_name in enumerate(self.query_state['measures']):
                col1, col2, col3 = st.columns([2, 1, 1])
                
                with col1:
                    measure_info = measures.get(measure_name, {})
                    label = measure_info.get('label', measure_name)
                    st.markdown(f"{i+1}. {label}")
                
                with col2:
                    # Move up/down
                    if i > 0 and st.button("⬆️", key=f"up_measure_{measure_name}", help="Move up"):
                        self.query_state['measures'][i], self.query_state['measures'][i-1] = \
                            self.query_state['measures'][i-1], self.query_state['measures'][i]
                        st.rerun()
                
                with col3:
                    if i < len(self.query_state['measures']) - 1 and st.button("⬇️", key=f"down_measure_{measure_name}", help="Move down"):
                        self.query_state['measures'][i], self.query_state['measures'][i+1] = \
                            self.query_state['measures'][i+1], self.query_state['measures'][i]
                        st.rerun()
    
    def _render_filter_builder(self):
        """Render advanced filter building interface."""
        st.markdown("### 🔍 Filter Builder")
        
        # Filter management will be handled by FilterManager
        st.info("Filters are managed in the main sidebar. Advanced filter expressions coming soon!")
        
        # Placeholder for future advanced filter builder
        with st.expander("🚧 Advanced Filters (Coming Soon)", expanded=False):
            st.markdown("""
            **Planned Features:**
            - Custom filter expressions
            - Date range filters
            - Numeric comparisons
            - Complex boolean logic
            - Filter templates
            """)
    
    def _render_advanced_options(self):
        """Render advanced query options."""
        st.markdown("### ⚙️ Advanced Options")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Sorting**")
            
            # Sort options
            available_fields = self.query_state['dimensions'] + self.query_state['measures']
            
            if available_fields:
                sort_field = st.selectbox(
                    "Sort by:",
                    options=[None] + available_fields,
                    format_func=lambda x: "No sorting" if x is None else x,
                    key="sort_field"
                )
                
                if sort_field:
                    sort_direction = st.radio(
                        "Direction:",
                        options=["ASC", "DESC"],
                        key="sort_direction"
                    )
                    
                    self.query_state['sorts'] = [(sort_field, sort_direction)]
                else:
                    self.query_state['sorts'] = []
            else:
                st.info("Add dimensions or measures to enable sorting")
        
        with col2:
            st.markdown("**Limits**")
            
            enable_limit = st.checkbox("Limit results", key="enable_limit")
            
            if enable_limit:
                limit_value = st.number_input(
                    "Maximum rows:",
                    min_value=1,
                    max_value=10000,
                    value=100,
                    key="limit_value"
                )
                self.query_state['limit'] = limit_value
            else:
                self.query_state['limit'] = None
    
    def _render_query_preview(self):
        """Render a preview of the current query."""
        st.markdown("**Query Summary:**")
        
        if self.query_state['dimensions']:
            st.markdown(f"📏 **Dimensions:** {', '.join(self.query_state['dimensions'])}")
        
        if self.query_state['measures']:
            st.markdown(f"📊 **Measures:** {', '.join(self.query_state['measures'])}")
        
        if self.query_state['filters']:
            st.markdown(f"🔍 **Filters:** {len(self.query_state['filters'])} applied")
        
        if self.query_state['sorts']:
            sort_desc = [f"{field} {direction}" for field, direction in self.query_state['sorts']]
            st.markdown(f"📈 **Sorting:** {', '.join(sort_desc)}")
        
        if self.query_state['limit']:
            st.markdown(f"🔢 **Limit:** {self.query_state['limit']} rows")
        
        # Pseudo-SQL preview
        with st.expander("📝 Pseudo-SQL Preview", expanded=False):
            sql_preview = self._generate_sql_preview()
            st.code(sql_preview, language='sql')
    
    def _generate_sql_preview(self) -> str:
        """Generate a pseudo-SQL preview of the query."""
        lines = []
        
        # SELECT clause
        select_items = []
        select_items.extend(self.query_state['dimensions'])
        select_items.extend(self.query_state['measures'])
        
        if select_items:
            lines.append(f"SELECT {', '.join(select_items)}")
        else:
            lines.append("SELECT *")
        
        # FROM clause
        lines.append("FROM semantic_model")
        
        # WHERE clause (filters)
        if self.query_state['filters']:
            filter_conditions = []
            for field, value in self.query_state['filters'].items():
                if isinstance(value, list):
                    filter_conditions.append(f"{field} IN ({', '.join(map(str, value))})")
                else:
                    filter_conditions.append(f"{field} = {value}")
            
            if filter_conditions:
                lines.append(f"WHERE {' AND '.join(filter_conditions)}")
        
        # GROUP BY clause
        if self.query_state['dimensions']:
            lines.append(f"GROUP BY {', '.join(self.query_state['dimensions'])}")
        
        # ORDER BY clause
        if self.query_state['sorts']:
            sort_items = [f"{field} {direction}" for field, direction in self.query_state['sorts']]
            lines.append(f"ORDER BY {', '.join(sort_items)}")
        
        # LIMIT clause
        if self.query_state['limit']:
            lines.append(f"LIMIT {self.query_state['limit']}")
        
        return '\n'.join(lines)
    
    def _get_query_state(self) -> Dict[str, Any]:
        """Get the current query state."""
        return self.query_state.copy()
    
    def clear_query(self):
        """Clear the current query."""
        self.query_state = {
            'dimensions': [],
            'measures': [],
            'filters': {},
            'sorts': [],
            'limit': None
        }