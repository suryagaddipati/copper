"""
Copper Semantic Layer Interface for UI

This module provides a bridge between the Copper semantic layer and the Streamlit UI,
handling model loading, data querying, and result formatting.
"""

import pandas as pd
import streamlit as st
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
import sys

# Add src to path for imports
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from model.loader import load_model
from model.semantic import Model
from model.datasource import DataSource
from model.dimension import Dimension
from model.measure import Measure


class CopperInterface:
    """Interface to Copper semantic layer for UI operations."""
    
    def __init__(self):
        self.model: Optional[Model] = None
        self.data: Optional[pd.DataFrame] = None
        self.model_path = None
        
    def load_semantic_model(self, model_path: str) -> Model:
        """Load a semantic model from YAML file."""
        try:
            model = load_model(model_path)
            self.model_path = model_path
            return model
        except Exception as e:
            st.error(f"Error loading model: {e}")
            raise e
    
    def load_data(self, model: Model, model_path: str) -> pd.DataFrame:
        """Load data from model datasources."""
        try:
            # For now, assume single datasource (UFC example)
            if not model.datasources:
                raise ValueError("No datasources found in model")
                
            # Get first datasource
            datasource_name, datasource = next(iter(model.datasources.items()))
            
            # Load data relative to model path
            model_dir = Path(model_path).parent
            data = datasource.load(base_path=model_dir)
            
            return data
        except Exception as e:
            st.error(f"Error loading data: {e}")
            raise e
    
    def get_available_models(self) -> Dict[str, str]:
        """Get available semantic models from examples directory."""
        examples_dir = Path(__file__).parent.parent / "examples" / "ufc"
        models = {}
        
        for yaml_file in examples_dir.glob("*.yaml"):
            if yaml_file.name != "datasources.yaml":  # Skip datasource files
                model_name = yaml_file.stem.replace("_", " ").title()
                models[model_name] = str(yaml_file)
                
        return models
    
    def get_dimensions(self) -> Dict[str, Dimension]:
        """Get available dimensions from loaded model."""
        if not self.model:
            return {}
        return self.model.dimensions
    
    def get_measures(self) -> Dict[str, Measure]:
        """Get available measures from loaded model."""
        if not self.model:
            return {}
        return self.model.measures
    
    def get_dimension_info(self, dim_name: str) -> Dict[str, Any]:
        """Get detailed information about a dimension."""
        if not self.model or dim_name not in self.model.dimensions:
            return {}
            
        dim = self.model.dimensions[dim_name]
        info = {
            "name": dim_name,
            "label": getattr(dim, 'label', dim_name),
            "description": getattr(dim, 'description', ''),
            "type": dim.type.value if dim.type else 'string',
            "expression": dim.expression
        }
        
        # Get unique values if data is loaded
        if self.data is not None:
            try:
                # Simple case: direct column reference
                if '.' in dim.expression:
                    table, column = dim.expression.split('.', 1)
                    if column in self.data.columns:
                        unique_vals = self.data[column].unique()
                        info["unique_values"] = sorted([str(v) for v in unique_vals if pd.notna(v)])[:20]  # Limit to 20
            except Exception:
                pass  # Skip if expression is complex
                
        return info
    
    def get_measure_info(self, measure_name: str) -> Dict[str, Any]:
        """Get detailed information about a measure."""
        if not self.model or measure_name not in self.model.measures:
            return {}
            
        measure = self.model.measures[measure_name]
        return {
            "name": measure_name,
            "label": getattr(measure, 'label', measure_name),
            "description": getattr(measure, 'description', ''),
            "type": measure.type.value if measure.type else 'number',
            "expression": measure.expression,
            "format": getattr(measure, 'format', None)
        }
    
    def execute_query(self, dimensions: List[str], measures: List[str], 
                     filters: Optional[Dict[str, Any]] = None) -> pd.DataFrame:
        """Execute a query with selected dimensions and measures."""
        if self.data is None or self.data.empty or not self.model:
            raise ValueError("No data or model loaded")
        
        try:
            # Start with base data
            df = self.data.copy()
            
            # Apply filters if provided
            if filters:
                for column, filter_values in filters.items():
                    if filter_values and column in df.columns:
                        if isinstance(filter_values, list):
                            df = df[df[column].isin(filter_values)]
                        else:
                            df = df[df[column] == filter_values]
            
            # Prepare dimension columns
            dim_columns = {}
            for dim_name in dimensions:
                if dim_name in self.model.dimensions:
                    dim = self.model.dimensions[dim_name]
                    column_data = self._extract_dimension_data(df, dim)
                    if column_data is not None:
                        dim_columns[dim_name] = column_data
            
            # If we have dimensions, group by them
            if dim_columns:
                # Create a combined dataframe with dimension columns
                result_df = pd.DataFrame(dim_columns)
                
                # Group by all dimensions
                group_cols = list(dim_columns.keys())
                result_df = result_df.groupby(group_cols).size().reset_index(name='row_count')
                
                # Calculate measures for each group
                for measure_name in measures:
                    if measure_name in self.model.measures:
                        measure = self.model.measures[measure_name]
                        result_df[measure_name] = self._calculate_grouped_measure(df, measure, dim_columns, result_df)
                
                # Remove row_count if we have actual measures
                if measures and 'row_count' in result_df.columns:
                    result_df = result_df.drop('row_count', axis=1)
                
                return result_df
            else:
                # No dimensions, just calculate scalar measures
                result_data = {}
                for measure_name in measures:
                    if measure_name in self.model.measures:
                        measure = self.model.measures[measure_name]
                        result_data[measure_name] = [self._calculate_scalar_measure(df, measure)]
                        
                return pd.DataFrame(result_data)
                
        except Exception as e:
            st.error(f"Error executing query: {e}")
            import traceback
            st.error(traceback.format_exc())
            raise e
    
    def _extract_dimension_data(self, df: pd.DataFrame, dimension: Dimension) -> Optional[pd.Series]:
        """Extract dimension data from dataframe."""
        expr = dimension.expression
        
        # Handle simple table.column references
        if '.' in expr:
            _, column = expr.split('.', 1)
            if column in df.columns:
                return df[column]
        
        # Handle CASE statements and complex expressions (simplified)
        if expr.strip().upper().startswith('CASE'):
            # For now, just return the first column that might be referenced
            # This is a simplified implementation
            if 'method' in expr and 'method' in df.columns:
                # Handle finish_type dimension
                return df['method'].map({
                    'KO/TKO': 'Knockout',
                    'SUB': 'Submission', 
                    'Decision': 'Decision'
                }).fillna('Other')
            elif 'round' in expr and 'round' in df.columns:
                # Handle fight_duration_category
                def categorize_round(r):
                    if pd.isna(r):
                        return 'Unknown'
                    r = int(r)
                    if r == 1:
                        return 'Round 1'
                    elif r == 2:
                        return 'Round 2'
                    elif r == 3:
                        return 'Round 3'
                    elif r >= 4:
                        return 'Championship Rounds'
                    else:
                        return 'Unknown'
                return df['round'].apply(categorize_round)
        
        # Fallback: try to find column name in expression
        for col in df.columns:
            if col in expr:
                return df[col]
        
        return None
    
    def _calculate_scalar_measure(self, df: pd.DataFrame, measure: Measure) -> Any:
        """Calculate a scalar measure value."""
        expr = measure.expression.upper()
        
        if expr.startswith('COUNT('):
            # Handle COUNT with WHERE clauses
            if 'WHERE' in expr:
                # Simple parsing for COUNT(table.column WHERE condition)
                # This is a simplified implementation
                return len(df)
            else:
                return len(df)
        elif expr.startswith('AVG('):
            # Extract column name from AVG(table.column)
            col_ref = expr[4:-1].strip()
            if '.' in col_ref:
                _, column = col_ref.split('.', 1)
                if column in df.columns:
                    return df[column].mean()
        elif expr.startswith('SUM('):
            col_ref = expr[4:-1].strip()
            if '.' in col_ref:
                _, column = col_ref.split('.', 1)
                if column in df.columns:
                    return df[column].sum()
        
        return 0
    
    def _calculate_grouped_measure(self, df: pd.DataFrame, measure: Measure, 
                                  dim_columns: Dict[str, pd.Series], result_df: pd.DataFrame) -> List[Any]:
        """Calculate measure values for grouped data."""
        expr = measure.expression.upper()
        results = []
        
        for idx, row in result_df.iterrows():
            # Filter data for this group
            group_filter = pd.Series([True] * len(df), index=df.index)
            for dim_name, dim_values in dim_columns.items():
                # Ensure both series have the same index
                aligned_dim_values = dim_values.reindex(df.index)
                group_filter &= (aligned_dim_values == row[dim_name])
            
            group_df = df[group_filter]
            
            # Calculate measure for this group
            if expr.startswith('COUNT('):
                # Handle COUNT with WHERE clauses
                if 'WHERE' in expr:
                    # Simple parsing for COUNT(table.column WHERE condition)
                    # This is a simplified implementation
                    results.append(len(group_df))
                else:
                    results.append(len(group_df))
            elif expr.startswith('AVG('):
                col_ref = expr[4:-1].strip()
                if '.' in col_ref:
                    _, column = col_ref.split('.', 1)
                    if column in group_df.columns:
                        val = group_df[column].mean()
                        results.append(val if pd.notna(val) else 0)
                    else:
                        results.append(0)
                else:
                    results.append(0)
            elif expr.startswith('SUM('):
                col_ref = expr[4:-1].strip()
                if '.' in col_ref:
                    _, column = col_ref.split('.', 1)
                    if column in group_df.columns:
                        val = group_df[column].sum()
                        results.append(val if pd.notna(val) else 0)
                    else:
                        results.append(0)
                else:
                    results.append(0)
            else:
                results.append(0)
        
        return results