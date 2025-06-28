import { useState } from 'react'
import { useConnections } from '../hooks/useConnections'

interface SQLViewerProps {
  copperCode: string
}

export const SQLViewer: React.FC<SQLViewerProps> = ({ copperCode }) => {
  const { generateSQL } = useConnections()
  const [selectedView, setSelectedView] = useState('')
  const [generatedSQL, setGeneratedSQL] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  // Extract view names from Copper code
  const extractViewNames = (code: string): string[] => {
    const viewMatches = code.match(/view:\s*(\w+)/g)
    if (!viewMatches) return []
    return viewMatches.map(match => match.replace('view:', '').trim())
  }

  const handleGenerateSQL = async () => {
    if (!selectedView) {
      setError('Please select a view')
      return
    }

    setLoading(true)
    setError('')
    
    try {
      const sql = await generateSQL(copperCode, selectedView)
      setGeneratedSQL(sql)
    } catch (err) {
      setError('Failed to generate SQL')
      console.error(err)
    } finally {
      setLoading(false)
    }
  }

  const viewNames = extractViewNames(copperCode)

  return (
    <div className="sql-viewer">
      <div className="sql-controls">
        <div className="view-selector">
          <label htmlFor="view-select">Select View:</label>
          <select 
            id="view-select"
            value={selectedView} 
            onChange={(e) => setSelectedView(e.target.value)}
            disabled={viewNames.length === 0}
          >
            <option value="">Choose a view...</option>
            {viewNames.map(name => (
              <option key={name} value={name}>{name}</option>
            ))}
          </select>
        </div>
        
        <button 
          onClick={handleGenerateSQL}
          disabled={!selectedView || loading}
          className="generate-btn"
        >
          {loading ? 'Generating...' : 'Generate SQL'}
        </button>
      </div>

      {error && (
        <div className="error-message">
          {error}
        </div>
      )}

      {generatedSQL && (
        <div className="sql-output">
          <h3>Generated SQL</h3>
          <pre className="sql-code">
            <code>{generatedSQL}</code>
          </pre>
        </div>
      )}
    </div>
  )
}