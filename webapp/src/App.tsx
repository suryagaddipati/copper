import React, { useState, useEffect, useCallback, useRef } from 'react'
import Editor from '@monaco-editor/react'
import { Check, X, FileText, BarChart3, Loader2 } from 'lucide-react'
import axios from 'axios'
import { registerCopperLanguage } from './copper-language'
import * as monaco from 'monaco-editor'

const API_BASE_URL = 'http://localhost:8000'

interface ExampleFile {
  name: string
  content: string
  description: string
}

interface ParseResult {
  valid: boolean
  errors: string[]
  warnings: string[]
  statistics: {
    total_models: number
    total_views: number
    total_dimensions: number
    total_measures: number
    total_joins: number
  }
  models: any[]
  views: any[]
}

const defaultCode = `# Welcome to the Copper Language Live Parser
# Select an example from the sidebar or start typing your own Copper code
# This demonstrates enhanced syntax highlighting

model: sample_orders {
  # Primary key dimension
  dimension: order_id {
    type: string
    expression: Orders[OrderID] ;;
    primary_key: yes
    label: "Order ID"
    description: "Unique identifier for each order"
  }
  
  # Date dimension with DAX function
  dimension: order_date {
    type: date
    expression: DATE(YEAR(Orders[OrderDate]), MONTH(Orders[OrderDate]), DAY(Orders[OrderDate])) ;;
    label: "Order Date"
  }
  
  # Complex measure with multi-line DAX
  measure: total_revenue {
    type: sum
    expression: 
      VAR CurrentRevenue = SUM(Orders[Amount])
      VAR FilteredRevenue = CALCULATE(
        CurrentRevenue,
        FILTER(Orders, Orders[Status] = "Completed")
      )
      RETURN FilteredRevenue ;;
    value_format: usd
    label: "Total Revenue"
  }
  
  # Boolean dimension
  dimension: is_weekend {
    type: yesno
    expression: WEEKDAY(Orders[OrderDate]) IN {1, 7} ;;
    label: "Weekend Order"
  }
}`

function App() {
  const [code, setCode] = useState(defaultCode)
  const [examples, setExamples] = useState<ExampleFile[]>([])
  const [parseResult, setParseResult] = useState<ParseResult | null>(null)
  const [isLoading, setIsLoading] = useState(false)
  const [loadingExamples, setLoadingExamples] = useState(true)
  const editorRef = useRef<monaco.editor.IStandaloneCodeEditor | null>(null)
  const monacoRef = useRef<typeof monaco | null>(null)

  // Fetch examples on component mount and register language
  useEffect(() => {
    fetchExamples()
    registerCopperLanguage()
  }, [])

  // Parse code whenever it changes and update editor markers
  useEffect(() => {
    const timeoutId = setTimeout(() => {
      parseCode(code)
    }, 500) // Debounce parsing

    return () => clearTimeout(timeoutId)
  }, [code])

  // Update editor markers when parse results change
  useEffect(() => {
    if (editorRef.current && monacoRef.current && parseResult) {
      updateEditorMarkers()
    }
  }, [parseResult])

  const fetchExamples = async () => {
    try {
      setLoadingExamples(true)
      const response = await axios.get(`${API_BASE_URL}/examples`)
      setExamples(response.data)
    } catch (error) {
      console.error('Failed to fetch examples:', error)
    } finally {
      setLoadingExamples(false)
    }
  }

  const parseCode = async (content: string) => {
    if (!content.trim()) {
      setParseResult(null)
      return
    }

    try {
      setIsLoading(true)
      const response = await axios.post(`${API_BASE_URL}/parse`, {
        content: content
      })
      setParseResult(response.data)
    } catch (error) {
      console.error('Parse error:', error)
      setParseResult({
        valid: false,
        errors: ['Failed to connect to parser API'],
        warnings: [],
        statistics: {
          total_models: 0,
          total_views: 0,
          total_dimensions: 0,
          total_measures: 0,
          total_joins: 0
        },
        models: [],
        views: []
      })
    } finally {
      setIsLoading(false)
    }
  }

  const loadExample = (example: ExampleFile) => {
    setCode(example.content)
  }

  const updateEditorMarkers = () => {
    if (!editorRef.current || !monacoRef.current || !parseResult) return

    const model = editorRef.current.getModel()
    if (!model) return

    const markers: monaco.editor.IMarkerData[] = []

    // Add error markers
    parseResult.errors.forEach((error, index) => {
      // Try to extract line number from error message
      const lineMatch = error.match(/Line (\d+):/)
      const lineNumber = lineMatch ? parseInt(lineMatch[1]) : 1

      markers.push({
        severity: monacoRef.current!.MarkerSeverity.Error,
        startLineNumber: lineNumber,
        startColumn: 1,
        endLineNumber: lineNumber,
        endColumn: model.getLineContent(lineNumber).length + 1,
        message: error,
        source: 'copper-parser'
      })
    })

    // Add warning markers
    parseResult.warnings.forEach((warning, index) => {
      const lineMatch = warning.match(/Line (\d+):/)
      const lineNumber = lineMatch ? parseInt(lineMatch[1]) : 1

      markers.push({
        severity: monacoRef.current!.MarkerSeverity.Warning,
        startLineNumber: lineNumber,
        startColumn: 1,
        endLineNumber: lineNumber,
        endColumn: model.getLineContent(lineNumber).length + 1,
        message: warning,
        source: 'copper-parser'
      })
    })

    // Set markers on the model
    monacoRef.current.editor.setModelMarkers(model, 'copper-parser', markers)
  }

  const handleEditorDidMount = (editor: monaco.editor.IStandaloneCodeEditor, monacoInstance: typeof monaco) => {
    editorRef.current = editor
    monacoRef.current = monacoInstance
    
    // Update markers if we already have parse results
    if (parseResult) {
      updateEditorMarkers()
    }
  }

  const handleEditorChange = useCallback((value: string | undefined) => {
    setCode(value || '')
  }, [])

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
          <div className="panel">
            <div className="panel-header">
              <FileText size={16} style={{ display: 'inline', marginRight: '0.5rem' }} />
              Code Editor
            </div>
            <div className="toolbar">
              <button 
                className="btn primary" 
                onClick={() => parseCode(code)}
                disabled={isLoading}
              >
                {isLoading ? <Loader2 size={14} className="animate-spin" /> : 'Parse'}
              </button>
              <button 
                className="btn" 
                onClick={() => setCode('')}
              >
                Clear
              </button>
            </div>
            <div className="editor-container">
              <Editor
                height="500px"
                defaultLanguage="copper"
                theme="copper-dark"
                value={code}
                onChange={handleEditorChange}
                onMount={handleEditorDidMount}
                options={{
                  minimap: { enabled: false },
                  scrollBeyondLastLine: false,
                  fontSize: 14,
                  wordWrap: 'on',
                  automaticLayout: true,
                  suggestOnTriggerCharacters: true,
                  quickSuggestions: true,
                  folding: true,
                  foldingStrategy: 'indentation',
                  showFoldingControls: 'always',
                  bracketPairColorization: { enabled: true },
                  guides: {
                    bracketPairs: true,
                    indentation: true
                  }
                }}
              />
            </div>
          </div>
        </div>

        <div className="sidebar">
          <div className="panel">
            <div className="panel-header">
              <FileText size={16} style={{ display: 'inline', marginRight: '0.5rem' }} />
              Examples
            </div>
            <div className="panel-content">
              {loadingExamples ? (
                <div className="loading">
                  <Loader2 size={16} className="animate-spin" />
                  Loading examples...
                </div>
              ) : (
                <div className="examples-list">
                  {examples.map((example) => (
                    <div
                      key={example.name}
                      className="example-item"
                      onClick={() => loadExample(example)}
                    >
                      <h4>{example.name}</h4>
                      <p>{example.description}</p>
                    </div>
                  ))}
                </div>
              )}
            </div>
          </div>

          <div className="panel">
            <div className="panel-header">
              <BarChart3 size={16} style={{ display: 'inline', marginRight: '0.5rem' }} />
              Validation Results
            </div>
            <div className="panel-content">
              <div className="validation-results">
                {isLoading ? (
                  <div className="loading">
                    <Loader2 size={16} className="animate-spin" />
                    Parsing...
                  </div>
                ) : parseResult ? (
                  <>
                    <div className={`validation-status ${parseResult.valid ? 'valid' : 'invalid'}`}>
                      {parseResult.valid ? (
                        <>
                          <Check size={16} />
                          Valid Copper syntax
                        </>
                      ) : (
                        <>
                          <X size={16} />
                          Syntax errors found
                        </>
                      )}
                    </div>

                    <div className="statistics">
                      <div className="stat-item">
                        <div className="stat-value">{parseResult.statistics.total_models}</div>
                        <div className="stat-label">Models</div>
                      </div>
                      <div className="stat-item">
                        <div className="stat-value">{parseResult.statistics.total_views}</div>
                        <div className="stat-label">Views</div>
                      </div>
                      <div className="stat-item">
                        <div className="stat-value">{parseResult.statistics.total_dimensions}</div>
                        <div className="stat-label">Dimensions</div>
                      </div>
                      <div className="stat-item">
                        <div className="stat-value">{parseResult.statistics.total_measures}</div>
                        <div className="stat-label">Measures</div>
                      </div>
                    </div>

                    {parseResult.errors.length > 0 && (
                      <div className="errors-list">
                        <h4 style={{ color: '#ef4444', margin: '0 0 0.5rem 0' }}>Errors:</h4>
                        {parseResult.errors.map((error, index) => (
                          <div key={index} className="error-item">
                            {error}
                          </div>
                        ))}
                      </div>
                    )}

                    {parseResult.warnings.length > 0 && (
                      <div className="errors-list">
                        <h4 style={{ color: '#f59e0b', margin: '1rem 0 0.5rem 0' }}>Warnings:</h4>
                        {parseResult.warnings.map((warning, index) => (
                          <div key={index} className="error-item" style={{ 
                            background: 'rgba(245, 158, 11, 0.1)', 
                            borderColor: 'rgba(245, 158, 11, 0.3)',
                            color: '#f59e0b'
                          }}>
                            {warning}
                          </div>
                        ))}
                      </div>
                    )}
                  </>
                ) : (
                  <div style={{ color: '#aaaaaa', textAlign: 'center', padding: '2rem' }}>
                    Enter Copper code to see validation results
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  )
}

export default App