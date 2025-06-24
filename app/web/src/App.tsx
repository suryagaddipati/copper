import { useState, useEffect } from 'react'
import { registerCopperLanguage } from './copper-language'
import { CopperEditor } from './components/CopperEditor'
import { ExamplesSidebar } from './components/ExamplesSidebar'
import { ValidationResults } from './components/ValidationResults'
import { useParseCode } from './hooks/useParseCode'
import { useExamples } from './hooks/useExamples'

function App() {
  const [code, setCode] = useState('')
  const [isDarkTheme, setIsDarkTheme] = useState(false)
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
          <h1>Copper Language Parser</h1>
          <p>Live parsing and validation for the Copper metadata language</p>
        </div>
      </header>

      <main className="main-content container">
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
      </main>
    </div>
  )
}

export default App