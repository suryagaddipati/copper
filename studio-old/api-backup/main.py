"""
FastAPI backend for Copper Studio
"""
import os
import glob
from typing import Dict, List, Any, Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from src.parser.antlr_parser import validate_copper_syntax
from database import ConnectionManager, QueryExecutor, SchemaInspector
from database.connection_manager import DatabaseType
from projects import ProjectManager

app = FastAPI(
    title="Copper Studio API",
    description="API for Copper Studio - semantic layer development environment",
    version="1.0.0"
)

connection_manager = ConnectionManager()
query_executor = QueryExecutor(connection_manager)
schema_inspector = SchemaInspector(connection_manager)
project_manager = ProjectManager()

# Enable CORS for web frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual frontend domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ParseRequest(BaseModel):
    content: str


class ParseResponse(BaseModel):
    valid: bool
    errors: List[str]
    warnings: List[str]
    statistics: Dict[str, Any]
    models: List[Dict[str, Any]]
    views: List[Dict[str, Any]]


class ExampleFile(BaseModel):
    name: str
    content: str
    description: str


class ConnectionRequest(BaseModel):
    name: str
    type: str
    host: Optional[str] = None
    port: Optional[int] = None
    database: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    file_path: Optional[str] = None


class ConnectionResponse(BaseModel):
    id: str
    name: str
    type: str
    is_active: bool


class QueryRequest(BaseModel):
    query: str
    limit: Optional[int] = 1000


class QueryResponse(BaseModel):
    data: List[Dict[str, Any]]
    columns: List[str]
    row_count: int


class TableInfo(BaseModel):
    name: str
    row_count: Optional[int] = None


class ColumnInfo(BaseModel):
    name: str
    type: str
    nullable: bool
    primary_key: bool = False


class TableSchema(BaseModel):
    name: str
    columns: List[ColumnInfo]
    row_count: Optional[int] = None


class ProjectRequest(BaseModel):
    path: str
    name: Optional[str] = None


class CopperFileResponse(BaseModel):
    name: str
    path: str
    content: str
    relative_path: str


class ProjectResponse(BaseModel):
    id: str
    name: str
    path: str
    file_count: int
    created_at: str


@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Copper Parser API",
        "version": "1.0.0",
        "endpoints": {
            "/parse": "Parse Copper content",
            "/examples": "Get example Copper files",
            "/health": "Health check"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "copper-parser-api"}


@app.post("/parse", response_model=ParseResponse)
async def parse_copper(request: ParseRequest):
    """Parse Copper content and return validation results"""
    try:
        result = validate_copper_syntax(request.content)
        
        # Convert parsed nodes to serializable format
        models = []
        for model in result["models"]:
            models.append({
                "name": model.name,
                "type": model.type.value,
                "line_number": model.line_number,
                "properties": model.properties,
                "children": [
                    {
                        "name": child.name,
                        "type": child.type.value,
                        "line_number": child.line_number,
                        "properties": child.properties
                    }
                    for child in model.children
                ]
            })
        
        views = []
        for view in result["views"]:
            views.append({
                "name": view.name,
                "type": view.type.value,
                "line_number": view.line_number,
                "properties": view.properties,
                "children": [
                    {
                        "name": child.name,
                        "type": child.type.value,
                        "line_number": child.line_number,
                        "properties": child.properties
                    }
                    for child in view.children
                ]
            })
        
        return ParseResponse(
            valid=result["valid"],
            errors=result["errors"],
            warnings=result["warnings"],
            statistics=result["statistics"],
            models=models,
            views=views
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Parse error: {str(e)}")


@app.get("/examples", response_model=List[ExampleFile])
async def get_examples():
    """Get all example Copper files"""
    examples = []
    examples_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "examples")
    
    if not os.path.exists(examples_dir):
        return examples
    
    # Get all .copper files
    copper_files = glob.glob(os.path.join(examples_dir, "*.copper"))
    
    for file_path in copper_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            filename = os.path.basename(file_path)
            name = filename.replace('.copper', '').replace('_', ' ').title()
            
            # Extract description from first comment if available
            description = f"Example Copper file: {name}"
            lines = content.split('\n')
            for line in lines[:5]:  # Check first 5 lines for description
                if line.strip().startswith('#') and len(line.strip()) > 2:
                    description = line.strip()[1:].strip()
                    break
            
            examples.append(ExampleFile(
                name=name,
                content=content,
                description=description
            ))
        
        except Exception as e:
            # Skip files that can't be read
            continue
    
    return examples


@app.get("/examples/{example_name}")
async def get_example(example_name: str):
    """Get a specific example file by name"""
    examples_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "examples")
    
    # Convert display name back to filename
    filename = example_name.lower().replace(' ', '_') + '.copper'
    file_path = os.path.join(examples_dir, filename)
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail=f"Example '{example_name}' not found")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract description
        description = f"Example Copper file: {example_name}"
        lines = content.split('\n')
        for line in lines[:5]:
            if line.strip().startswith('#') and len(line.strip()) > 2:
                description = line.strip()[1:].strip()
                break
        
        return ExampleFile(
            name=example_name,
            content=content,
            description=description
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading example: {str(e)}")


@app.post("/connections", response_model=ConnectionResponse)
async def create_connection(request: ConnectionRequest):
    try:
        db_type = DatabaseType(request.type.lower())
        connection = connection_manager.create_connection(
            name=request.name,
            db_type=db_type,
            host=request.host,
            port=request.port,
            database=request.database,
            username=request.username,
            password=request.password,
            file_path=request.file_path
        )
        
        return ConnectionResponse(
            id=connection.id,
            name=connection.name,
            type=connection.type.value,
            is_active=connection.is_active
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to create connection: {str(e)}")


@app.get("/connections", response_model=List[ConnectionResponse])
async def list_connections():
    connections = connection_manager.list_connections()
    return [
        ConnectionResponse(
            id=conn.id,
            name=conn.name,
            type=conn.type.value,
            is_active=conn.is_active
        )
        for conn in connections
    ]


@app.post("/connections/{connection_id}/connect")
async def connect_to_database(connection_id: str):
    if not connection_manager.get_connection(connection_id):
        raise HTTPException(status_code=404, detail="Connection not found")
    
    if connection_manager.connect(connection_id):
        return {"status": "connected"}
    else:
        raise HTTPException(status_code=400, detail="Failed to connect to database")


@app.post("/connections/{connection_id}/disconnect")
async def disconnect_from_database(connection_id: str):
    if not connection_manager.get_connection(connection_id):
        raise HTTPException(status_code=404, detail="Connection not found")
    
    if connection_manager.disconnect(connection_id):
        return {"status": "disconnected"}
    else:
        raise HTTPException(status_code=400, detail="Failed to disconnect from database")


@app.get("/connections/{connection_id}/tables", response_model=List[TableInfo])
async def get_tables(connection_id: str):
    try:
        tables = schema_inspector.get_tables(connection_id)
        table_infos = []
        
        for table in tables:
            try:
                info = schema_inspector.get_table_info(connection_id, table)
                table_infos.append(TableInfo(name=info.name, row_count=info.row_count))
            except Exception:
                table_infos.append(TableInfo(name=table, row_count=None))
        
        return table_infos
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to get tables: {str(e)}")


@app.get("/connections/{connection_id}/tables/{table_name}/schema", response_model=TableSchema)
async def get_table_schema(connection_id: str, table_name: str):
    try:
        table_info = schema_inspector.get_table_info(connection_id, table_name)
        
        columns = [
            ColumnInfo(
                name=col.name,
                type=col.type,
                nullable=col.nullable,
                primary_key=col.primary_key
            )
            for col in table_info.columns
        ]
        
        return TableSchema(
            name=table_info.name,
            columns=columns,
            row_count=table_info.row_count
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to get table schema: {str(e)}")


@app.post("/connections/{connection_id}/query", response_model=QueryResponse)
async def execute_query(connection_id: str, request: QueryRequest):
    try:
        result = query_executor.execute_query(connection_id, request.query, request.limit)
        
        return QueryResponse(
            data=result.data,
            columns=result.columns,
            row_count=result.row_count
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Query execution failed: {str(e)}")


@app.get("/connections/{connection_id}/tables/{table_name}/data", response_model=QueryResponse)
async def get_table_data(connection_id: str, table_name: str, limit: int = 100):
    try:
        result = query_executor.get_table_data(connection_id, table_name, limit)
        
        return QueryResponse(
            data=result.data,
            columns=result.columns,
            row_count=result.row_count
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to get table data: {str(e)}")


@app.post("/projects", response_model=ProjectResponse)
async def load_project(request: ProjectRequest):
    """Load a project from a disk directory"""
    try:
        project = project_manager.load_project_from_path(request.path, request.name)
        return ProjectResponse(
            id=project.id,
            name=project.name,
            path=project.path,
            file_count=len(project.files),
            created_at=project.created_at.isoformat()
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to load project: {str(e)}")


@app.get("/projects", response_model=List[ProjectResponse])
async def list_projects():
    """List all loaded projects"""
    projects = project_manager.list_projects()
    return [
        ProjectResponse(
            id=project.id,
            name=project.name,
            path=project.path,
            file_count=len(project.files),
            created_at=project.created_at.isoformat()
        )
        for project in projects
    ]


@app.get("/projects/{project_id}/files", response_model=List[CopperFileResponse])
async def get_project_files(project_id: str):
    """Get all Copper files in a project"""
    project = project_manager.get_project(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    return [
        CopperFileResponse(
            name=file.name,
            path=file.path,
            content=file.content,
            relative_path=file.relative_path
        )
        for file in project.files
    ]


@app.delete("/projects/{project_id}")
async def delete_project(project_id: str):
    """Remove a project from the workspace"""
    if project_manager.delete_project(project_id):
        return {"status": "deleted"}
    else:
        raise HTTPException(status_code=404, detail="Project not found")


@app.post("/projects/{project_id}/refresh")
async def refresh_project(project_id: str):
    """Refresh project files from disk"""
    project = project_manager.refresh_project(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    return ProjectResponse(
        id=project.id,
        name=project.name,
        path=project.path,
        file_count=len(project.files),
        created_at=project.created_at.isoformat()
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)