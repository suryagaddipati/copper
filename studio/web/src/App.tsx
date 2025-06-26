import { useState, useEffect } from 'react'
import { registerCopperLanguage } from './copper-language'
import { CopperEditor } from './components/CopperEditor'
import { ExamplesSidebar } from './components/ExamplesSidebar'
import { ValidationResults } from './components/ValidationResults'
import { DatabaseExplorer } from './components/database/DatabaseExplorer'
import { useParseCode } from './hooks/useParseCode'
import { useExamples } from './hooks/useExamples'
import './styles/database.css'

function App() {
  const [code, setCode] = useState('')
  const [isDarkTheme, setIsDarkTheme] = useState(false)
  const [activeTab, setActiveTab] = useState<'editor' | 'database'>('editor')
  const { parseResult, isLoading, parseCode } = useParseCode(code)
  const { examples, loadingExamples } = useExamples()

  // Register language early and update document theme
  useEffect(() => {
    registerCopperLanguage()
  }, [])

  useEffect(() => {
    document.documentElement.setAttribute('data-theme', isDarkTheme ? 'dark' : 'light')
  }, [isDarkTheme])

  const handleLoadExample = (example: { name: string; content: string; description: string }) => {
    setCode(example.content)
  }

  // Auto-load first example when examples are loaded
  useEffect(() => {
    if (examples.length > 0 && code === '') {
      setCode(examples[0].content)
    }
  }, [examples, code])

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
        {activeTab === 'editor' ? (
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
              <ExamplesSidebar
                examples={examples}
                loadingExamples={loadingExamples}
                onLoadExample={handleLoadExample}
              />
              <ValidationResults
                parseResult={parseResult}
                isLoading={isLoading}
              />
            </div>
          </>
        ) : (
          <DatabaseExplorer />
        )}
      </main>
    </div>
  )
}

export default App