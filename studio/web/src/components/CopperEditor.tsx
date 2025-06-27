import React, { useCallback, useRef, useEffect } from 'react'
import Editor from '@monaco-editor/react'
import { FileText, Loader2, Sun, Moon, Check, X } from 'lucide-react'
import { registerCopperLanguage, copperLanguageDefinition } from '../copper-language'
import * as monaco from 'monaco-editor'

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

interface CopperEditorProps {
  code: string
  onChange: (value: string) => void
  onParse: () => void
  onClear: () => void
  isLoading: boolean
  isDarkTheme: boolean
  onToggleTheme: () => void
  parseResult: ParseResult | null
}

export const CopperEditor: React.FC<CopperEditorProps> = ({
  code,
  onChange,
  onParse,
  onClear,
  isLoading,
  isDarkTheme,
  onToggleTheme,
  parseResult
}) => {
  const editorRef = useRef<monaco.editor.IStandaloneCodeEditor | null>(null)
  const monacoRef = useRef<typeof monaco | null>(null)

  // Update editor markers when parse results change
  useEffect(() => {
    if (editorRef.current && monacoRef.current && parseResult) {
      updateEditorMarkers()
    }
  }, [parseResult])

  const updateEditorMarkers = () => {
    if (!editorRef.current || !monacoRef.current || !parseResult) return

    const model = editorRef.current.getModel()
    if (!model) return

    const markers: monaco.editor.IMarkerData[] = []

    // Helper function to parse error line and column
    const parseErrorLocation = (errorMsg: string) => {
      // Try to match "Line X:Y" pattern first (with column)
      let match = errorMsg.match(/Line (\d+):(\d+)/)
      if (match) {
        return { line: parseInt(match[1]), column: parseInt(match[2]) }
      }
      
      // Fall back to "Line X:" pattern (no column)
      match = errorMsg.match(/Line (\d+):/)
      if (match) {
        return { line: parseInt(match[1]), column: 1 }
      }
      
      return { line: 1, column: 1 }
    }

    // Add error markers
    parseResult.errors.forEach((error) => {
      const { line: lineNumber, column: columnNumber } = parseErrorLocation(error)
      
      // Ensure line number is valid
      if (lineNumber <= 0 || lineNumber > model.getLineCount()) return
      
      const lineContent = model.getLineContent(lineNumber)
      const startColumn = Math.max(1, columnNumber)
      const endColumn = Math.min(lineContent.length + 1, startColumn + 10) // Underline ~10 chars or to end of line
      
      markers.push({
        severity: monacoRef.current!.MarkerSeverity.Error,
        startLineNumber: lineNumber,
        startColumn: startColumn,
        endLineNumber: lineNumber,
        endColumn: endColumn,
        message: error.replace(/^Line \d+:\d*\s*-?\s*/, ''), // Clean up message
        source: 'copper-parser'
      })
    })

    // Add warning markers (typically DAX token recognition warnings)
    parseResult.warnings.forEach((warning) => {
      const { line: lineNumber, column: columnNumber } = parseErrorLocation(warning)
      
      // Ensure line number is valid
      if (lineNumber <= 0 || lineNumber > model.getLineCount()) return
      
      const lineContent = model.getLineContent(lineNumber)
      const startColumn = Math.max(1, columnNumber)
      const endColumn = Math.min(lineContent.length + 1, startColumn + 5) // Shorter underline for warnings
      
      // Filter out token recognition errors to reduce noise
      if (warning.includes('token recognition error')) return
      
      markers.push({
        severity: monacoRef.current!.MarkerSeverity.Warning,
        startLineNumber: lineNumber,
        startColumn: startColumn,
        endLineNumber: lineNumber,
        endColumn: endColumn,
        message: warning.replace(/^Line \d+:\d*\s*-?\s*/, ''), // Clean up message
        source: 'copper-parser'
      })
    })

    monacoRef.current.editor.setModelMarkers(model, 'copper-parser', markers)
  }

  const handleEditorDidMount = (editor: monaco.editor.IStandaloneCodeEditor, monacoInstance: typeof monaco) => {
    console.log('Editor mounted')
    editorRef.current = editor
    monacoRef.current = monacoInstance
    
    const currentModel = editor.getModel()
    console.log('Current model language:', currentModel?.getLanguageId())
    
    monacoInstance.languages.setMonarchTokensProvider('plaintext', copperLanguageDefinition)
    console.log('Applied Copper tokenizer to plaintext')
    
    const currentTheme = isDarkTheme ? "copper-dark" : "copper-light"
    monacoInstance.editor.setTheme(currentTheme)
    console.log('Applied theme:', currentTheme)
    
    if (currentModel) {
      setTimeout(() => {
        const currentContent = currentModel.getValue()
        currentModel.setValue('')
        currentModel.setValue(currentContent)
        console.log('Forced re-tokenization for proper syntax highlighting')
      }, 100)
    }
    
    if (parseResult) {
      setTimeout(() => updateEditorMarkers(), 300)
    }
  }

  const handleEditorChange = useCallback((value: string | undefined) => {
    onChange(value || '')
  }, [onChange])

  return (
    <div className="editor-panel">
      <div className="panel-header panel-header-with-icon">
        <FileText size={16} className="icon-spacing" />
        Code Editor
      </div>
      <div className="editor-toolbar">
        <div className="editor-toolbar-left">
          <button 
            className="btn btn-primary btn-with-icon" 
            onClick={onParse}
            disabled={isLoading}
          >
            {isLoading ? <Loader2 size={14} className="animate-spin" /> : 'Parse'}
          </button>
          <button 
            className="btn btn-secondary" 
            onClick={onClear}
          >
            Clear
          </button>
          <button 
            className="btn btn-secondary btn-with-icon" 
            onClick={onToggleTheme}
            title={isDarkTheme ? 'Switch to Light Theme' : 'Switch to Dark Theme'}
          >
            {isDarkTheme ? <Sun size={14} /> : <Moon size={14} />}
            {isDarkTheme ? 'Light' : 'Dark'}
          </button>
        </div>

        <div className="editor-toolbar-right">
          {isLoading ? (
            <div className="validation-status validation-status-parsing">
              <Loader2 size={14} className="animate-spin" />
              <span>Parsing...</span>
            </div>
          ) : parseResult ? (
            <div className={`validation-status ${
              parseResult.valid ? 'validation-status-valid' : 'validation-status-invalid'
            }`}>
              {parseResult.valid ? (
                <>
                  <Check size={14} />
                  <span>Valid</span>
                </>
              ) : (
                <>
                  <X size={14} />
                  <span>{parseResult.errors.length} Error{parseResult.errors.length !== 1 ? 's' : ''}</span>
                </>
              )}
            </div>
          ) : null}
        </div>
      </div>
      <div className="editor-container">
        <Editor
          height="100%"
          defaultLanguage="plaintext"
          theme={isDarkTheme ? "copper-dark" : "copper-light"}
          value={code}
          onChange={handleEditorChange}
          onMount={handleEditorDidMount}
          beforeMount={(monacoInstance) => {
            console.log('Before mount - ensuring language is registered')
            registerCopperLanguage()
            
            setTimeout(() => {
              const currentTheme = isDarkTheme ? "copper-dark" : "copper-light"
              monacoInstance.editor.setTheme(currentTheme)
              console.log('Force applied theme:', currentTheme)
            }, 50)
          }}
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
  )
}