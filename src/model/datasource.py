from typing import Optional
from pydantic import BaseModel
import pandas as pd
import os
from pathlib import Path


class DataSource(BaseModel):
    
    type: str = "file"
    file_path: Optional[str] = None
    format: Optional[str] = None
    table: Optional[str] = None
    description: Optional[str] = None
    
    def load(self, base_path: Optional[Path] = None) -> pd.DataFrame:
        if self.type != "file":
            raise ValueError(f"Unsupported datasource type: {self.type}")
        
        if not self.file_path:
            raise ValueError("file_path is required for file datasource")
        
        file_path = self.file_path
        if not os.path.isabs(file_path) and base_path:
            file_path = base_path / file_path
        
        if self.format == "csv" or file_path.suffix == '.csv':
            return pd.read_csv(file_path)
        elif self.format == "parquet" or file_path.suffix == '.parquet':
            return pd.read_parquet(file_path)
        elif self.format == "json" or file_path.suffix == '.json':
            return pd.read_json(file_path)
        else:
            return pd.read_csv(file_path)