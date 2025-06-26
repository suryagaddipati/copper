import json
import os
from typing import List, Dict, Any
from .connection_manager import DatabaseConnection, DatabaseType


class ConnectionStorage:
    
    def __init__(self, storage_path: str = None):
        if storage_path is None:
            # Default to data directory relative to this file
            current_dir = os.path.dirname(os.path.abspath(__file__))
            data_dir = os.path.join(current_dir, '..', 'data')
            storage_path = os.path.join(data_dir, 'connections.json')
        
        self.storage_path = storage_path
        self._ensure_data_directory()
    
    def _ensure_data_directory(self):
        """Create data directory if it doesn't exist"""
        data_dir = os.path.dirname(self.storage_path)
        os.makedirs(data_dir, exist_ok=True)
    
    def save_connections(self, connections: Dict[str, DatabaseConnection]) -> bool:
        """Save connections to JSON file"""
        try:
            # Convert connections to JSON-serializable format
            connections_data = {
                "connections": [
                    {
                        "id": conn.id,
                        "name": conn.name,
                        "type": conn.type.value,
                        "host": conn.host,
                        "port": conn.port,
                        "database": conn.database,
                        "username": conn.username,
                        "password": conn.password,
                        "file_path": conn.file_path
                    }
                    for conn in connections.values()
                ]
            }
            
            with open(self.storage_path, 'w', encoding='utf-8') as f:
                json.dump(connections_data, f, indent=2)
            
            return True
            
        except Exception as e:
            print(f"Failed to save connections: {e}")
            return False
    
    def load_connections(self) -> Dict[str, DatabaseConnection]:
        """Load connections from JSON file"""
        connections = {}
        
        try:
            if not os.path.exists(self.storage_path):
                return connections
            
            with open(self.storage_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Convert JSON data back to DatabaseConnection objects
            for conn_data in data.get("connections", []):
                try:
                    connection = DatabaseConnection(
                        id=conn_data["id"],
                        name=conn_data["name"],
                        type=DatabaseType(conn_data["type"]),
                        host=conn_data.get("host"),
                        port=conn_data.get("port"),
                        database=conn_data.get("database"),
                        username=conn_data.get("username"),
                        password=conn_data.get("password"),
                        file_path=conn_data.get("file_path"),
                        is_active=False  # Always start as inactive
                    )
                    connections[connection.id] = connection
                    
                except Exception as e:
                    print(f"Failed to load connection {conn_data.get('name', 'unknown')}: {e}")
                    continue
            
            return connections
            
        except Exception as e:
            print(f"Failed to load connections: {e}")
            return connections