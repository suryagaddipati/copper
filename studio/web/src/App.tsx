import { useState, useEffect } from 'react'
import { registerCopperLanguage } from './copper-language'
import { CopperEditor } from './components/CopperEditor'
import { ValidationResults } from './components/ValidationResults'
import { DatabaseExplorer } from './components/database/DatabaseExplorer'
import { ProjectManager } from './components/projects/ProjectManager'
import { ProjectFileTree } from './components/projects/ProjectFileTree'
import { useParseCode } from './hooks/useParseCode'
import { Project, CopperFile } from './hooks/useProjects'
import './styles/database.css'

function App() {
  const [code, setCode] = useState('')
  const [isDarkTheme, setIsDarkTheme] = useState(false)
  const [activeTab, setActiveTab] = useState<'projects' | 'editor' | 'database'>('projects')
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
    setActiveTab('editor')
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
    <div className="app">
      <header className="header">
        <div className="container">
          <h1>Copper Studio</h1>
          <p>Semantic layer development environment</p>
          
          <nav className="main-nav">
            <button 
              className={`nav-tab ${activeTab === 'projects' ? 'active' : ''}`}
              onClick={() => setActiveTab('projects')}
            >
              Projects
            </button>
            <button 
              className={`nav-tab ${activeTab === 'editor' ? 'active' : ''}`}
              onClick={() => setActiveTab('editor')}
            >
              Copper Editor
            </button>
            <button 
              className={`nav-tab ${activeTab === 'database' ? 'active' : ''}`}
              onClick={() => setActiveTab('database')}
            >
              Database Explorer
            </button>
          </nav>
        </div>
      </header>

      <main className="main-content container">
        {activeTab === 'projects' && (
          <ProjectManager onProjectSelect={handleProjectSelect} />
        )}
        
        {activeTab === 'editor' && (
          <>
            <div className="editor-panel">
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

            <div className="sidebar">
              <div className="panel">
                <div className="panel-header">Project Files</div>
                <div className="panel-content" style={{ padding: 0 }}>
                  <ProjectFileTree
                    project={selectedProject}
                    onFileSelect={handleFileSelect}
                    selectedFile={selectedFile}
                  />
                </div>
              </div>
              <ValidationResults
                parseResult={parseResult}
                isLoading={isLoading}
              />
            </div>
          </>
        )}

        {activeTab === 'database' && (
          <DatabaseExplorer />
        )}
      </main>
    </div>
  )
}

export default App