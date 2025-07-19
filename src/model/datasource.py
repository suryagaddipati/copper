from typing import Optional
from pydantic import BaseModel
import pandas as pd
import os
from pathlib import Path


class DataSource(BaseModel):
    """Data source with connection metadata."""
    
    type: str = "file"
    file_path: Optional[str] = None
    format: Optional[str] = None
    table: Optional[str] = None
    description: Optional[str] = None
    
    def load(self, base_path: Optional[Path] = None) -> pd.DataFrame:
        """Load data from this datasource and return as DataFrame."""
        if self.type != "file":
            raise ValueError(f"Unsupported datasource type: {self.type}")
        
        if not self.file_path:
            raise ValueError("file_path is required for file datasource")
        
        # Resolve file path
        file_path = self.file_path
        if not os.path.isabs(file_path) and base_path:
            file_path = base_path / file_path
        
        # Load based on format
        if self.format == "csv" or file_path.endswith('.csv'):
            return pd.read_csv(file_path)
        elif self.format == "parquet" or file_path.endswith('.parquet'):
            return pd.read_parquet(file_path)
        elif self.format == "json" or file_path.endswith('.json'):
            return pd.read_json(file_path)
        else:
            # Default to CSV
            return pd.read_csv(file_path)