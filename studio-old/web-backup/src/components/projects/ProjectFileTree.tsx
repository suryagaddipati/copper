import { useState, useEffect } from 'react'
import { useProjects, CopperFile, Project } from '../../hooks/useProjects'

interface ProjectFileTreeProps {
  project: Project | null
  onFileSelect?: (file: CopperFile) => void
  selectedFile?: CopperFile | null
}

export const ProjectFileTree: React.FC<ProjectFileTreeProps> = ({ 
  project, 
  onFileSelect, 
  selectedFile 
}) => {
  const { getProjectFiles } = useProjects()
  const [files, setFiles] = useState<CopperFile[]>([])
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    if (project) {
      loadProjectFiles()
    } else {
      setFiles([])
    }
  }, [project])

  const loadProjectFiles = async () => {
    if (!project) return

    setLoading(true)
    try {
      const projectFiles = await getProjectFiles(project.id)
      setFiles(projectFiles)
    } catch (error) {
      console.error('Failed to load project files:', error)
    } finally {
      setLoading(false)
    }
  }

  const organizeFilesByFolder = (files: CopperFile[]) => {
    const organized: { [folder: string]: CopperFile[] } = {}
    
    files.forEach(file => {
      const parts = file.relative_path.split('/')
      if (parts.length === 1) {
        // Root level file
        if (!organized['']) organized[''] = []
        organized[''].push(file)
      } else {
        // File in subfolder
        const folder = parts.slice(0, -1).join('/')
        if (!organized[folder]) organized[folder] = []
        organized[folder].push(file)
      }
    })

    return organized
  }

  if (!project) {
    return (
      <div className="project-file-tree">
        <div className="empty-state">No project selected</div>
      </div>
    )
  }

  if (loading) {
    return (
      <div className="project-file-tree">
        <div className="loading">Loading files...</div>
      </div>
    )
  }

  const organizedFiles = organizeFilesByFolder(files)
  const folders = Object.keys(organizedFiles).sort()

  return (
    <div className="project-file-tree">
      <div className="project-header">
        <h4>{project.name}</h4>
        <p className="file-count">{files.length} files</p>
      </div>

      <div className="file-tree">
        {folders.map(folder => (
          <div key={folder} className="folder-section">
            {folder && (
              <div className="folder-name">
                📁 {folder}
              </div>
            )}
            <div className="files-list">
              {organizedFiles[folder].map(file => (
                <div 
                  key={file.path}
                  className={`file-item ${selectedFile?.path === file.path ? 'selected' : ''}`}
                  onClick={() => onFileSelect?.(file)}
                >
                  <span className="file-icon">📄</span>
                  <span className="file-name">{file.name}</span>
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}