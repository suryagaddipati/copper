import React from 'react'
import { BarChart3, Check, X, Loader2 } from 'lucide-react'

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

interface ValidationResultsProps {
  parseResult: ParseResult | null
  isLoading: boolean
}

export const ValidationResults: React.FC<ValidationResultsProps> = ({
  parseResult,
  isLoading
}) => {
  return (
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
  )
}