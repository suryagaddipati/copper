"""
Chart Manager for Copper Dashboard

Handles the creation and rendering of interactive Plotly charts based on query results.
"""

import streamlit as st
import pandas as pd
from typing import List, Dict, Optional, Any

try:
    import plotly.express as px
    import plotly.graph_objects as go
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False
    st.error("Plotly is not installed. Install with: uv add plotly")


class ChartManager:
    """Manages chart creation and rendering for the dashboard."""
    
    def __init__(self):
        self.chart_types = {
            "bar": "📊 Bar Chart",
            "line": "📈 Line Chart", 
            "scatter": "🔵 Scatter Plot",
            "pie": "🥧 Pie Chart",
            "histogram": "📊 Histogram",
            "box": "📦 Box Plot"
        }
    
    def render_charts(self, df: pd.DataFrame, dimensions: List[str], measures: List[str]):
        """Render charts based on query results."""
        if not PLOTLY_AVAILABLE:
            st.error("Plotly charts are not available. Showing data table instead.")
            st.dataframe(df, use_container_width=True)
            return
            
        if df.empty:
            st.warning("No data to display")
            return
        
        # Auto-suggest chart types
        suggested_charts = self._suggest_charts(df, dimensions, measures)
        
        # Handle case with no chart suggestions (e.g., no dimensions)
        if not suggested_charts:
            st.info("📊 **Summary Results**")
            # Display scalar measures as metrics
            if measures:
                cols = st.columns(len(measures))
                for i, measure in enumerate(measures):
                    if measure in df.columns:
                        value = df[measure].iloc[0] if not df.empty else 0
                        with cols[i]:
                            st.metric(label=measure.replace("_", " ").title(), value=f"{value:,}")
            else:
                st.write("No visualization available for current selection.")
            return
        
        # Chart type selection
        if len(suggested_charts) > 1:
            chart_cols = st.columns(len(suggested_charts))
            
            for i, (chart_type, chart_data) in enumerate(suggested_charts.items()):
                with chart_cols[i]:
                    self._render_single_chart(df, chart_type, chart_data, dimensions, measures)
        else:
            # Single chart
            chart_type, chart_data = next(iter(suggested_charts.items()))
            self._render_single_chart(df, chart_type, chart_data, dimensions, measures)
    
    def _suggest_charts(self, df: pd.DataFrame, dimensions: List[str], measures: List[str]) -> Dict[str, Dict]:
        """Suggest appropriate chart types based on data characteristics."""
        suggestions = {}
        
        # Get data characteristics
        num_dims = len(dimensions)
        num_measures = len(measures)
        row_count = len(df)
        
        # Determine primary dimension and measure
        primary_dim = dimensions[0] if dimensions else None
        primary_measure = measures[0] if measures else None
        
        # Bar chart - good for categorical data
        if primary_dim and primary_measure and num_dims <= 2:
            suggestions["bar"] = {
                "x": primary_dim,
                "y": primary_measure,
                "color": dimensions[1] if num_dims > 1 else None,
                "title": f"{primary_measure} by {primary_dim}"
            }
        
        # Pie chart - good for single dimension with counts
        if primary_dim and num_dims == 1 and row_count <= 10:
            suggestions["pie"] = {
                "values": primary_measure if primary_measure else None,
                "names": primary_dim,
                "title": f"Distribution of {primary_measure or 'Count'} by {primary_dim}"
            }
        
        # Line chart - good for time series or ordered data
        if primary_dim and primary_measure and num_dims <= 2:
            suggestions["line"] = {
                "x": primary_dim,
                "y": primary_measure,
                "color": dimensions[1] if num_dims > 1 else None,
                "title": f"{primary_measure} trend by {primary_dim}"
            }
        
        # Scatter plot - good for two measures
        if num_measures >= 2:
            suggestions["scatter"] = {
                "x": measures[0],
                "y": measures[1],
                "color": primary_dim,
                "title": f"{measures[1]} vs {measures[0]}"
            }
        
        # Default to bar if no suggestions
        if not suggestions and primary_dim and primary_measure:
            suggestions["bar"] = {
                "x": primary_dim,
                "y": primary_measure,
                "title": f"{primary_measure} by {primary_dim}"
            }
        
        return suggestions
    
    def _render_single_chart(self, df: pd.DataFrame, chart_type: str, chart_config: Dict,
                           dimensions: List[str], measures: List[str]):
        """Render a single chart of the specified type."""
        try:
            # Chart type selector
            available_types = list(self.chart_types.keys())
            current_index = available_types.index(chart_type) if chart_type in available_types else 0
            
            selected_type = st.selectbox(
                "Chart Type:",
                options=available_types,
                index=current_index,
                format_func=lambda x: self.chart_types[x],
                key=f"chart_type_{chart_type}"
            )
            
            # Update chart config if type changed
            if selected_type != chart_type:
                chart_config = self._get_chart_config(df, selected_type, dimensions, measures)
            
            # Render the selected chart type
            fig = self._create_chart(df, selected_type, chart_config)
            
            if fig:
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.error(f"Could not create {selected_type} chart")
                
        except Exception as e:
            st.error(f"Error creating chart: {e}")
    
    def _get_chart_config(self, df: pd.DataFrame, chart_type: str, 
                         dimensions: List[str], measures: List[str]) -> Dict:
        """Get configuration for a specific chart type."""
        primary_dim = dimensions[0] if dimensions else None
        primary_measure = measures[0] if measures else None
        
        configs = {
            "bar": {
                "x": primary_dim,
                "y": primary_measure,
                "color": dimensions[1] if len(dimensions) > 1 else None,
                "title": f"{primary_measure} by {primary_dim}" if primary_dim and primary_measure else "Bar Chart"
            },
            "line": {
                "x": primary_dim,
                "y": primary_measure,
                "color": dimensions[1] if len(dimensions) > 1 else None,
                "title": f"{primary_measure} trend by {primary_dim}" if primary_dim and primary_measure else "Line Chart"
            },
            "scatter": {
                "x": measures[0] if len(measures) > 0 else primary_dim,
                "y": measures[1] if len(measures) > 1 else primary_measure,
                "color": primary_dim,
                "title": f"Scatter Plot"
            },
            "pie": {
                "values": primary_measure,
                "names": primary_dim,
                "title": f"Distribution by {primary_dim}" if primary_dim else "Pie Chart"
            },
            "histogram": {
                "x": primary_measure or primary_dim,
                "title": f"Distribution of {primary_measure or primary_dim}"
            },
            "box": {
                "x": primary_dim,
                "y": primary_measure,
                "title": f"{primary_measure} distribution by {primary_dim}" if primary_dim and primary_measure else "Box Plot"
            }
        }
        
        return configs.get(chart_type, {})
    
    def _create_chart(self, df: pd.DataFrame, chart_type: str, config: Dict) -> Optional[go.Figure]:
        """Create a Plotly chart of the specified type."""
        try:
            # Common chart settings
            common_settings = {
                "template": "plotly_white",
                "height": 500
            }
            
            if chart_type == "bar":
                fig = px.bar(
                    df,
                    x=config.get("x"),
                    y=config.get("y"),
                    color=config.get("color"),
                    title=config.get("title", "Bar Chart"),
                    **common_settings
                )
                
            elif chart_type == "line":
                fig = px.line(
                    df,
                    x=config.get("x"),
                    y=config.get("y"),
                    color=config.get("color"),
                    title=config.get("title", "Line Chart"),
                    **common_settings
                )
                
            elif chart_type == "scatter":
                fig = px.scatter(
                    df,
                    x=config.get("x"),
                    y=config.get("y"),
                    color=config.get("color"),
                    title=config.get("title", "Scatter Plot"),
                    **common_settings
                )
                
            elif chart_type == "pie":
                fig = px.pie(
                    df,
                    values=config.get("values"),
                    names=config.get("names"),
                    title=config.get("title", "Pie Chart"),
                    **common_settings
                )
                
            elif chart_type == "histogram":
                fig = px.histogram(
                    df,
                    x=config.get("x"),
                    title=config.get("title", "Histogram"),
                    **common_settings
                )
                
            elif chart_type == "box":
                fig = px.box(
                    df,
                    x=config.get("x"),
                    y=config.get("y"),
                    title=config.get("title", "Box Plot"),
                    **common_settings
                )
                
            else:
                return None
            
            # Update layout for better appearance
            fig.update_layout(
                showlegend=True,
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1
                ),
                margin=dict(t=60, b=60, l=60, r=60)
            )
            
            return fig
            
        except Exception as e:
            st.error(f"Error creating {chart_type} chart: {e}")
            return None
    
    def render_custom_chart(self, df: pd.DataFrame, chart_config: Dict):
        """Render a custom chart with user-specified configuration."""
        chart_type = chart_config.get("type", "bar")
        
        # Allow user to customize chart parameters
        with st.expander("🎨 Customize Chart", expanded=False):
            col1, col2 = st.columns(2)
            
            with col1:
                x_col = st.selectbox("X-axis:", options=df.columns, 
                                   index=list(df.columns).index(chart_config.get("x", df.columns[0])))
                color_col = st.selectbox("Color by:", options=[None] + list(df.columns),
                                       index=0)
            
            with col2:
                if chart_type not in ["pie", "histogram"]:
                    y_col = st.selectbox("Y-axis:", options=df.columns,
                                       index=list(df.columns).index(chart_config.get("y", df.columns[-1])))
                else:
                    y_col = chart_config.get("y")
                
                title = st.text_input("Chart Title:", value=chart_config.get("title", ""))
        
        # Update config with user selections
        updated_config = {
            "x": x_col,
            "y": y_col,
            "color": color_col,
            "title": title
        }
        
        # Create and display chart
        fig = self._create_chart(df, chart_type, updated_config)
        if fig:
            st.plotly_chart(fig, use_container_width=True)