import os
import uuid
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime


@dataclass
class CopperFile:
    name: str
    path: str
    content: str
    relative_path: str


@dataclass
class Project:
    id: str
    name: str
    path: str
    files: List[CopperFile]
    created_at: datetime


class ProjectManager:
    
    def __init__(self):
        self.projects: Dict[str, Project] = {}
        self._storage = None
        self._load_projects()
    
    def _load_projects(self):
        """Load saved projects from storage"""
        try:
            from .project_storage import ProjectStorage
            self._storage = ProjectStorage()
            self.projects = self._storage.load_projects()
        except Exception as e:
            print(f"Failed to load projects: {e}")
            self.projects = {}
    
    def _save_projects(self):
        """Save current projects to storage"""
        if self._storage:
            try:
                self._storage.save_projects(self.projects)
            except Exception as e:
                print(f"Failed to save projects: {e}")
    
    def load_project_from_path(self, project_path: str, project_name: str = None) -> Optional[Project]:
        """Load a project from a disk directory"""
        if not os.path.exists(project_path):
            raise ValueError(f"Path does not exist: {project_path}")
        
        if not os.path.isdir(project_path):
            raise ValueError(f"Path is not a directory: {project_path}")
        
        # Generate project name if not provided
        if not project_name:
            project_name = os.path.basename(project_path)
        
        # Scan for .copper files
        copper_files = self._scan_copper_files(project_path)
        
        if not copper_files:
            raise ValueError(f"No .copper files found in directory: {project_path}")
        
        # Create project
        project_id = str(uuid.uuid4())
        project = Project(
            id=project_id,
            name=project_name,
            path=os.path.abspath(project_path),
            files=copper_files,
            created_at=datetime.now()
        )
        
        self.projects[project_id] = project
        self._save_projects()
        return project
    
    def _scan_copper_files(self, directory_path: str) -> List[CopperFile]:
        """Recursively scan directory for .copper files"""
        copper_files = []
        
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith('.copper'):
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, directory_path)
                    
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        copper_file = CopperFile(
                            name=file,
                            path=file_path,
                            content=content,
                            relative_path=relative_path
                        )
                        copper_files.append(copper_file)
                        
                    except Exception as e:
                        print(f"Failed to read file {file_path}: {e}")
                        continue
        
        return copper_files
    
    def get_project(self, project_id: str) -> Optional[Project]:
        """Get a project by ID"""
        return self.projects.get(project_id)
    
    def list_projects(self) -> List[Project]:
        """List all loaded projects"""
        return list(self.projects.values())
    
    def delete_project(self, project_id: str) -> bool:
        """Remove a project from the workspace"""
        if project_id in self.projects:
            del self.projects[project_id]
            self._save_projects()
            return True
        return False
    
    def refresh_project(self, project_id: str) -> Optional[Project]:
        """Refresh project files from disk"""
        project = self.get_project(project_id)
        if not project:
            return None
        
        try:
            # Re-scan the directory
            copper_files = self._scan_copper_files(project.path)
            project.files = copper_files
            self._save_projects()
            return project
        except Exception as e:
            print(f"Failed to refresh project {project_id}: {e}")
            return None
    
    def get_project_files(self, project_id: str) -> List[CopperFile]:
        """Get all files in a project"""
        project = self.get_project(project_id)
        return project.files if project else []