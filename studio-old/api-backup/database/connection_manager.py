from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from enum import Enum
import uuid


class DatabaseType(Enum):
    DUCKDB = "duckdb"
    POSTGRES = "postgres"
    MYSQL = "mysql"
    SQLITE = "sqlite"


@dataclass
class DatabaseConnection:
    id: str
    name: str
    type: DatabaseType
    host: Optional[str] = None
    port: Optional[int] = None
    database: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    file_path: Optional[str] = None
    is_active: bool = False


class ConnectionManager:
    
    def __init__(self):
        self.connections: Dict[str, DatabaseConnection] = {}
        self._active_connections: Dict[str, Any] = {}
        self._storage = None
        self._load_connections()
    
    def _load_connections(self):
        """Load saved connections from storage"""
        try:
            from .connection_storage import ConnectionStorage
            self._storage = ConnectionStorage()
            self.connections = self._storage.load_connections()
        except Exception as e:
            print(f"Failed to load connections: {e}")
            self.connections = {}
    
    def _save_connections(self):
        """Save current connections to storage"""
        if self._storage:
            try:
                self._storage.save_connections(self.connections)
            except Exception as e:
                print(f"Failed to save connections: {e}")
    
    def create_connection(
        self,
        name: str,
        db_type: DatabaseType,
        host: Optional[str] = None,
        port: Optional[int] = None,
        database: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        file_path: Optional[str] = None
    ) -> DatabaseConnection:
        
        connection_id = str(uuid.uuid4())
        connection = DatabaseConnection(
            id=connection_id,
            name=name,
            type=db_type,
            host=host,
            port=port,
            database=database,
            username=username,
            password=password,
            file_path=file_path
        )
        
        self.connections[connection_id] = connection
        self._save_connections()
        return connection
    
    def get_connection(self, connection_id: str) -> Optional[DatabaseConnection]:
        return self.connections.get(connection_id)
    
    def list_connections(self) -> List[DatabaseConnection]:
        return list(self.connections.values())
    
    def delete_connection(self, connection_id: str) -> bool:
        if connection_id in self.connections:
            if connection_id in self._active_connections:
                self.disconnect(connection_id)
            del self.connections[connection_id]
            self._save_connections()
            return True
        return False
    
    def connect(self, connection_id: str) -> bool:
        connection = self.get_connection(connection_id)
        if not connection:
            return False
        
        try:
            if connection.type == DatabaseType.DUCKDB:
                import duckdb
                if connection.file_path:
                    conn = duckdb.connect(connection.file_path)
                else:
                    conn = duckdb.connect()
                self._active_connections[connection_id] = conn
                connection.is_active = True
                return True
                
        except Exception as e:
            print(f"Connection failed: {e}")
            return False
        
        return False
    
    def disconnect(self, connection_id: str) -> bool:
        if connection_id in self._active_connections:
            try:
                conn = self._active_connections[connection_id]
                if hasattr(conn, 'close'):
                    conn.close()
                del self._active_connections[connection_id]
                
                connection = self.get_connection(connection_id)
                if connection:
                    connection.is_active = False
                return True
            except Exception:
                return False
        return False
    
    def get_active_connection(self, connection_id: str):
        return self._active_connections.get(connection_id)
    
    def test_connection(self, connection_id: str) -> bool:
        if self.connect(connection_id):
            conn = self.get_active_connection(connection_id)
            if conn:
                try:
                    conn.execute("SELECT 1").fetchone()
                    return True
                except Exception:
                    return False
        return False