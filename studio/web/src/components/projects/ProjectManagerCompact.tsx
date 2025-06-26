import { useState } from 'react'
import { useProjects, Project } from '../../hooks/useProjects'

interface ProjectManagerCompactProps {
  onProjectSelect?: (project: Project) => void
}

export const ProjectManagerCompact: React.FC<ProjectManagerCompactProps> = ({ onProjectSelect }) => {
  const { projects, loading, loadProject, deleteProject } = useProjects()
  const [loadingProject, setLoadingProject] = useState(false)
  const [projectPath, setProjectPath] = useState('')
  const [error, setError] = useState('')
  const [showForm, setShowForm] = useState(false)

  const handleLoadProject = async () => {
    if (!projectPath.trim()) {
      setError('Please enter a project path')
      return
    }

    setLoadingProject(true)
    setError('')

    try {
      const project = await loadProject(projectPath.trim())
      setProjectPath('')
      setShowForm(false)
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
    if (confirm(`Remove project "${projectName}" from workspace?`)) {
      try {
        await deleteProject(projectId)
      } catch (err) {
        console.error('Failed to delete project:', err)
      }
    }
  }

  return (
    <div className="project-manager-compact">
      <div className="project-actions">
        <button 
          onClick={() => setShowForm(!showForm)}
          className="btn primary"
          disabled={loadingProject}
        >
          {showForm ? 'Cancel' : 'Load Project'}
        </button>
      </div>

      {showForm && (
        <div className="project-form">
          <div className="form-group">
            <input
              type="text"
              value={projectPath}
              onChange={(e) => setProjectPath(e.target.value)}
              placeholder="/path/to/copper/files"
              disabled={loadingProject}
              onKeyPress={(e) => e.key === 'Enter' && handleLoadProject()}
            />
          </div>
          <button 
            onClick={handleLoadProject}
            disabled={loadingProject || !projectPath.trim()}
            className="btn primary small"
          >
            {loadingProject ? 'Loading...' : 'Load'}
          </button>
          {error && <div className="error-message small">{error}</div>}
        </div>
      )}

      <div className="projects-list-compact">
        {loading ? (
          <div className="loading small">Loading...</div>
        ) : projects.length === 0 ? (
          <div className="empty-state small">No projects loaded</div>
        ) : (
          <div className="project-items-compact">
            {projects.map(project => (
              <div key={project.id} className="project-item-compact">
                <div className="project-info-compact">
                  <div className="project-name">{project.name}</div>
                  <div className="project-meta-compact">
                    {project.file_count} files
                  </div>
                </div>
                <div className="project-actions-compact">
                  <button 
                    onClick={() => onProjectSelect?.(project)}
                    className="btn small"
                    title="Open project"
                  >
                    Open
                  </button>
                  <button 
                    onClick={() => handleDeleteProject(project.id, project.name)}
                    className="btn small delete"
                    title="Remove from workspace"
                  >
                    ×
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