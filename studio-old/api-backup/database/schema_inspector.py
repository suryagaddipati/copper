from typing import List, Dict, Any, Optional
from dataclasses import dataclass


@dataclass
class ColumnInfo:
    name: str
    type: str
    nullable: bool
    primary_key: bool = False


@dataclass  
class TableInfo:
    name: str
    columns: List[ColumnInfo]
    row_count: Optional[int] = None


class SchemaInspector:
    
    def __init__(self, connection_manager):
        self.connection_manager = connection_manager
    
    def get_tables(self, connection_id: str) -> List[str]:
        conn = self.connection_manager.get_active_connection(connection_id)
        if not conn:
            raise ValueError(f"No active connection found for {connection_id}")
        
        try:
            result = conn.execute("SHOW TABLES").fetchall()
            return [row[0] for row in result]
        except Exception as e:
            raise Exception(f"Failed to get tables: {str(e)}")
    
    def get_table_info(self, connection_id: str, table_name: str) -> TableInfo:
        conn = self.connection_manager.get_active_connection(connection_id)
        if not conn:
            raise ValueError(f"No active connection found for {connection_id}")
        
        try:
            desc_result = conn.execute(f"DESCRIBE {table_name}").fetchall()
            
            columns = []
            for row in desc_result:
                column_name = row[0]
                column_type = row[1]
                nullable = row[2] == 'YES' if len(row) > 2 else True
                
                columns.append(ColumnInfo(
                    name=column_name,
                    type=column_type,
                    nullable=nullable
                ))
            
            try:
                count_result = conn.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()
                row_count = count_result[0] if count_result else None
            except Exception:
                row_count = None
            
            return TableInfo(
                name=table_name,
                columns=columns,
                row_count=row_count
            )
            
        except Exception as e:
            raise Exception(f"Failed to get table info for {table_name}: {str(e)}")
    
    def get_database_schema(self, connection_id: str) -> List[TableInfo]:
        tables = self.get_tables(connection_id)
        schema = []
        
        for table in tables:
            try:
                table_info = self.get_table_info(connection_id, table)
                schema.append(table_info)
            except Exception:
                continue
        
        return schema