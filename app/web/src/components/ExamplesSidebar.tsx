import React from 'react'
import { FileText, Loader2 } from 'lucide-react'

interface ExampleFile {
  name: string
  content: string
  description: string
}

interface ExamplesSidebarProps {
  examples: ExampleFile[]
  loadingExamples: boolean
  onLoadExample: (example: ExampleFile) => void
}

export const ExamplesSidebar: React.FC<ExamplesSidebarProps> = ({
  examples,
  loadingExamples,
  onLoadExample
}) => {
  return (
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
                onClick={() => onLoadExample(example)}
              >
                <h4>{example.name}</h4>
                <p>{example.description}</p>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  )
}