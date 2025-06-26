import json
import os
from typing import Dict
from datetime import datetime
from .project_manager import Project, CopperFile


class ProjectStorage:
    
    def __init__(self, storage_path: str = None):
        if storage_path is None:
            # Default to data directory relative to this file
            current_dir = os.path.dirname(os.path.abspath(__file__))
            data_dir = os.path.join(current_dir, '..', 'data')
            storage_path = os.path.join(data_dir, 'projects.json')
        
        self.storage_path = storage_path
        self._ensure_data_directory()
    
    def _ensure_data_directory(self):
        """Create data directory if it doesn't exist"""
        data_dir = os.path.dirname(self.storage_path)
        os.makedirs(data_dir, exist_ok=True)
    
    def save_projects(self, projects: Dict[str, Project]) -> bool:
        """Save projects to JSON file (without file contents)"""
        try:
            projects_data = {
                "projects": [
                    {
                        "id": project.id,
                        "name": project.name,
                        "path": project.path,
                        "created_at": project.created_at.isoformat(),
                        "file_count": len(project.files)
                    }
                    for project in projects.values()
                ]
            }
            
            with open(self.storage_path, 'w', encoding='utf-8') as f:
                json.dump(projects_data, f, indent=2)
            
            return True
            
        except Exception as e:
            print(f"Failed to save projects: {e}")
            return False
    
    def load_projects(self) -> Dict[str, Project]:
        """Load projects from JSON file and re-scan files from disk"""
        projects = {}
        
        try:
            if not os.path.exists(self.storage_path):
                return projects
            
            with open(self.storage_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            for project_data in data.get("projects", []):
                try:
                    project_path = project_data["path"]
                    
                    # Only load if directory still exists
                    if not os.path.exists(project_path):
                        print(f"Project path no longer exists: {project_path}")
                        continue
                    
                    # Re-scan files from disk
                    from .project_manager import ProjectManager
                    temp_manager = ProjectManager.__new__(ProjectManager)  # Create without __init__
                    copper_files = temp_manager._scan_copper_files(project_path)
                    
                    project = Project(
                        id=project_data["id"],
                        name=project_data["name"],
                        path=project_path,
                        files=copper_files,
                        created_at=datetime.fromisoformat(project_data["created_at"])
                    )
                    
                    projects[project.id] = project
                    
                except Exception as e:
                    print(f"Failed to load project {project_data.get('name', 'unknown')}: {e}")
                    continue
            
            return projects
            
        except Exception as e:
            print(f"Failed to load projects: {e}")
            return projects