"""
FastAPI backend for Copper language live parsing
"""
import os
import glob
from typing import Dict, List, Any
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from antlr_parser import validate_copper_syntax

app = FastAPI(
    title="Copper Parser API",
    description="Live parsing API for the Copper metadata language",
    version="1.0.0"
)

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
    examples_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "examples")
    
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
    examples_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "examples")
    
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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)