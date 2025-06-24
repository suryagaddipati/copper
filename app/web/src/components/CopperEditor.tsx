import React, { useCallback, useRef, useEffect } from 'react'
import Editor from '@monaco-editor/react'
import { FileText, Loader2, Sun, Moon } from 'lucide-react'
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

    // Add error markers
    parseResult.errors.forEach((error) => {
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
    parseResult.warnings.forEach((warning) => {
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
    <div className="panel">
      <div className="panel-header">
        <FileText size={16} style={{ display: 'inline', marginRight: '0.5rem' }} />
        Code Editor
      </div>
      <div className="toolbar">
        <button 
          className="btn primary" 
          onClick={onParse}
          disabled={isLoading}
        >
          {isLoading ? <Loader2 size={14} className="animate-spin" /> : 'Parse'}
        </button>
        <button 
          className="btn" 
          onClick={onClear}
        >
          Clear
        </button>
        <button 
          className="btn" 
          onClick={onToggleTheme}
          title={isDarkTheme ? 'Switch to Light Theme' : 'Switch to Dark Theme'}
        >
          {isDarkTheme ? <Sun size={14} /> : <Moon size={14} />}
          {isDarkTheme ? ' Light' : ' Dark'}
        </button>
      </div>
      <div className="editor-container">
        <Editor
          height="500px"
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