import { useState } from 'react'
import { useProjects, Project } from '../../hooks/useProjects'

interface ProjectManagerProps {
  onProjectSelect?: (project: Project) => void
}

export const ProjectManager: React.FC<ProjectManagerProps> = ({ onProjectSelect }) => {
  const { projects, loading, loadProject, deleteProject } = useProjects()
  const [loadingProject, setLoadingProject] = useState(false)
  const [projectPath, setProjectPath] = useState('')
  const [projectName, setProjectName] = useState('')
  const [error, setError] = useState('')

  const handleLoadProject = async () => {
    if (!projectPath.trim()) {
      setError('Please enter a project path')
      return
    }

    setLoadingProject(true)
    setError('')

    try {
      const project = await loadProject(projectPath.trim(), projectName.trim() || undefined)
      setProjectPath('')
      setProjectName('')
      if (onProjectSelect) {
        onProjectSelect(project)
      }
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Failed to load project')
    } finally {
      setLoadingProject(false)
    }
  }

  const handleDeleteProject = async (projectId: string, projectName: string) => {
    if (confirm(`Delete project "${projectName}"? This will only remove it from the workspace, not delete files.`)) {
      try {
        await deleteProject(projectId)
      } catch (err) {
        console.error('Failed to delete project:', err)
      }
    }
  }

  return (
    <div className="project-manager">
      <div className="project-loader">
        <h3>Load Project</h3>
        <div className="form-group">
          <label htmlFor="project-path">Project Path:</label>
          <input
            id="project-path"
            type="text"
            value={projectPath}
            onChange={(e) => setProjectPath(e.target.value)}
            placeholder="/path/to/copper/files"
            disabled={loadingProject}
          />
        </div>
        <div className="form-group">
          <label htmlFor="project-name">Project Name (optional):</label>
          <input
            id="project-name"
            type="text"
            value={projectName}
            onChange={(e) => setProjectName(e.target.value)}
            placeholder="My Project"
            disabled={loadingProject}
          />
        </div>
        <button 
          onClick={handleLoadProject}
          disabled={loadingProject || !projectPath.trim()}
          className="btn primary"
        >
          {loadingProject ? 'Loading...' : 'Load Project'}
        </button>
        {error && <div className="error-message">{error}</div>}
      </div>

      <div className="projects-list">
        <h3>Loaded Projects ({projects.length})</h3>
        {loading ? (
          <div className="loading">Loading projects...</div>
        ) : projects.length === 0 ? (
          <div className="empty-state">No projects loaded</div>
        ) : (
          <div className="project-items">
            {projects.map(project => (
              <div key={project.id} className="project-item">
                <div className="project-info">
                  <h4>{project.name}</h4>
                  <p className="project-path">{project.path}</p>
                  <p className="project-meta">
                    {project.file_count} files • {new Date(project.created_at).toLocaleDateString()}
                  </p>
                </div>
                <div className="project-actions">
                  <button 
                    onClick={() => onProjectSelect?.(project)}
                    className="btn"
                  >
                    Open
                  </button>
                  <button 
                    onClick={() => handleDeleteProject(project.id, project.name)}
                    className="btn delete"
                  >
                    Remove
                  </button>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  )
}