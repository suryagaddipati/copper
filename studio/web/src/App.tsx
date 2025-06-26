import { useState, useEffect } from 'react'
import { registerCopperLanguage } from './copper-language'
import { CopperEditor } from './components/CopperEditor'
import { ValidationResults } from './components/ValidationResults'
import { ProjectManagerCompact } from './components/projects/ProjectManagerCompact'
import { ProjectFileTree } from './components/projects/ProjectFileTree'
import { useParseCode } from './hooks/useParseCode'
import { Project, CopperFile } from './hooks/useProjects'

function App() {
  const [code, setCode] = useState('')
  const [isDarkTheme, setIsDarkTheme] = useState(false)
  const [selectedProject, setSelectedProject] = useState<Project | null>(null)
  const [selectedFile, setSelectedFile] = useState<CopperFile | null>(null)
  const { parseResult, isLoading, parseCode } = useParseCode(code)

  // Register language early and update document theme
  useEffect(() => {
    registerCopperLanguage()
  }, [])

  useEffect(() => {
    document.documentElement.setAttribute('data-theme', isDarkTheme ? 'dark' : 'light')
  }, [isDarkTheme])

  const handleProjectSelect = (project: Project) => {
    setSelectedProject(project)
    setSelectedFile(null)
  }

  const handleFileSelect = (file: CopperFile) => {
    setSelectedFile(file)
    setCode(file.content)
  }

  const handleClearCode = () => {
    setCode('')
  }

  const handleToggleTheme = () => {
    setIsDarkTheme(!isDarkTheme)
  }

  const handleCodeChange = (value: string) => {
    setCode(value)
  }

  return (
    <div className="app-container">
      <header className="app-header">
        <div className="app-header-content">
          <h1 className="app-title">Copper Studio</h1>
          <p className="app-subtitle">Semantic layer development environment</p>
          
        </div>
      </header>

      <main className="main-content">
        <div className="studio-layout">
          <div className="studio-sidebar">
            <div className="panel">
              <div className="panel-header">
                Projects
              </div>
              <div className="panel-content">
                <ProjectManagerCompact onProjectSelect={handleProjectSelect} />
              </div>
            </div>
            <div className="panel panel-flex">
              <div className="panel-header">
                Project Files
              </div>
              <div className="panel-content-no-padding">
                <ProjectFileTree
                  project={selectedProject}
                  onFileSelect={handleFileSelect}
                  selectedFile={selectedFile}
                />
              </div>
            </div>
          </div>

          <div className="studio-editor">
            <CopperEditor
              code={code}
              onChange={handleCodeChange}
              onParse={parseCode}
              onClear={handleClearCode}
              isLoading={isLoading}
              isDarkTheme={isDarkTheme}
              onToggleTheme={handleToggleTheme}
              parseResult={parseResult}
            />
          </div>
        </div>
      </main>
    </div>
  )
}

export default App