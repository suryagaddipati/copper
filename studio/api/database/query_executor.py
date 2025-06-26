from typing import List, Dict, Any, Optional
import pandas as pd


class QueryResult:
    
    def __init__(self, data: List[Dict[str, Any]], columns: List[str], row_count: int):
        self.data = data
        self.columns = columns
        self.row_count = row_count


class QueryExecutor:
    
    def __init__(self, connection_manager):
        self.connection_manager = connection_manager
    
    def execute_query(self, connection_id: str, query: str, limit: Optional[int] = 1000) -> QueryResult:
        conn = self.connection_manager.get_active_connection(connection_id)
        if not conn:
            raise ValueError(f"No active connection found for {connection_id}")
        
        try:
            if limit:
                query = f"SELECT * FROM ({query}) LIMIT {limit}"
            
            result = conn.execute(query).fetchdf()
            
            data = result.to_dict('records')
            columns = result.columns.tolist()
            row_count = len(data)
            
            return QueryResult(data=data, columns=columns, row_count=row_count)
            
        except Exception as e:
            raise Exception(f"Query execution failed: {str(e)}")
    
    def get_table_data(self, connection_id: str, table_name: str, limit: int = 100) -> QueryResult:
        query = f"SELECT * FROM {table_name}"
        return self.execute_query(connection_id, query, limit)
    
    def get_table_count(self, connection_id: str, table_name: str) -> int:
        conn = self.connection_manager.get_active_connection(connection_id)
        if not conn:
            raise ValueError(f"No active connection found for {connection_id}")
        
        try:
            result = conn.execute(f"SELECT COUNT(*) as count FROM {table_name}").fetchone()
            return result[0] if result else 0
        except Exception as e:
            raise Exception(f"Count query failed: {str(e)}")
    
    def validate_query(self, connection_id: str, query: str) -> bool:
        try:
            conn = self.connection_manager.get_active_connection(connection_id)
            if not conn:
                return False
            
            conn.execute(f"EXPLAIN {query}")
            return True
        except Exception:
            return False