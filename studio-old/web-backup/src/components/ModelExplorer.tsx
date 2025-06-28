import { useState, useEffect } from 'react'
import { useParseCode } from '../hooks/useParseCode'
import axios from 'axios'

interface ModelField {
  name: string
  type: string
  label?: string
}

interface ParsedModel {
  name: string
  dimensions: ModelField[]
  measures: ModelField[]
}

interface ModelExplorerProps {
  onQueryRequest: (query: QueryRequest) => void
  disabled?: boolean
  loading?: boolean
  modelName?: string
  modelFile?: string
}

interface QueryRequest {
  modelName: string
  selectedDimensions: string[]
  selectedMeasures: string[]
  filters: Record<string, string>
}

export function ModelExplorer({ onQueryRequest, disabled = false, loading = false, modelName, modelFile }: ModelExplorerProps) {
  const [selectedDimensions, setSelectedDimensions] = useState<string[]>([])
  const [selectedMeasures, setSelectedMeasures] = useState<string[]>([])
  const [filters, setFilters] = useState<Record<string, string>>({})
  const [parsedModel, setParsedModel] = useState<ParsedModel | null>(null)

  const [modelContent, setModelContent] = useState<string>('')
  const { parseResult } = useParseCode(modelContent)

  // Load model content when modelFile changes
  useEffect(() => {
    if (modelFile) {
      const loadModelContent = async () => {
        try {
          const response = await axios.get(`http://localhost:8000/model-content/${modelFile}`)
          setModelContent(response.data.content)
        } catch (err) {
          console.error('Failed to load model content:', err)
          setModelContent('')
        }
      }
      loadModelContent()
    } else {
      setModelContent('')
    }
  }, [modelFile])

  // Update parsed model when parse result changes
  useEffect(() => {
    if (parseResult?.valid && parseResult.models?.length > 0) {
      const model = parseResult.models[0] // Take first model
      
      // Extract dimensions from model children
      const dimensions = model.children?.filter((child: any) => child.type === 'dimension').map((dim: any) => ({
        name: dim.name,
        type: dim.properties?.type || 'string',
        label: dim.properties?.label || dim.name
      })) || []
      
      // Extract measures from model children  
      const measures = model.children?.filter((child: any) => child.type === 'measure').map((measure: any) => ({
        name: measure.name,
        type: measure.properties?.type || 'count',
        label: measure.properties?.label || measure.name
      })) || []
      
      setParsedModel({
        name: model.name, // Use actual model name from file
        dimensions,
        measures
      })
    } else {
      setParsedModel(null)
    }
  }, [parseResult])

  // Reset selections when model changes
  useEffect(() => {
    setSelectedDimensions([])
    setSelectedMeasures([])
    setFilters({})
  }, [modelName])

  const handleDimensionToggle = (dimensionName: string) => {
    setSelectedDimensions(prev => 
      prev.includes(dimensionName) 
        ? prev.filter(d => d !== dimensionName)
        : [...prev, dimensionName]
    )
  }

  const handleMeasureToggle = (measureName: string) => {
    setSelectedMeasures(prev => 
      prev.includes(measureName) 
        ? prev.filter(m => m !== measureName)
        : [...prev, measureName]
    )
  }

  const handleFilterChange = (fieldName: string, value: string) => {
    setFilters(prev => ({
      ...prev,
      [fieldName]: value
    }))
  }

  const handleRunQuery = () => {
    const actualModelName = parsedModel?.name || modelName
    if (actualModelName && (selectedDimensions.length > 0 || selectedMeasures.length > 0)) {
      onQueryRequest({
        modelName: actualModelName,
        selectedDimensions,
        selectedMeasures,
        filters
      })
    }
  }

  const canRunQuery = parsedModel && (selectedDimensions.length > 0 || selectedMeasures.length > 0)

  if (!parsedModel) {
    return (
      <div className="model-explorer bg-white border border-gray-200 rounded-lg p-4 space-y-4">
        <div className="text-center text-gray-500">
          {modelContent ? 'Parsing model...' : 'Select a table to explore'}
        </div>
      </div>
    )
  }

  return (
    <div className="model-explorer bg-white border border-gray-200 rounded-lg p-4 space-y-4">
      <div className="header">
        <h3 className="text-lg font-semibold text-gray-900">Explore {parsedModel.name}</h3>
        <p className="text-sm text-gray-600">Choose dimensions and measures to analyze your data</p>
      </div>

      {/* Dimensions */}
      {parsedModel.dimensions.length > 0 && (
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            Dimensions
          </label>
          <div className="space-y-2 max-h-32 overflow-y-auto">
            {parsedModel.dimensions.map((dimension) => (
              <label key={dimension.name} className="flex items-center">
                <input
                  type="checkbox"
                  checked={selectedDimensions.includes(dimension.name)}
                  onChange={() => handleDimensionToggle(dimension.name)}
                  className="mr-2 h-4 w-4 text-blue-600 rounded border-gray-300"
                  disabled={disabled}
                />
                <span className="text-sm text-gray-700">
                  {dimension.label} <span className="text-gray-400">({dimension.type})</span>
                </span>
              </label>
            ))}
          </div>
        </div>
      )}

      {/* Measures */}
      {parsedModel.measures.length > 0 && (
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            Measures
          </label>
          <div className="space-y-2 max-h-32 overflow-y-auto">
            {parsedModel.measures.map((measure) => (
              <label key={measure.name} className="flex items-center">
                <input
                  type="checkbox"
                  checked={selectedMeasures.includes(measure.name)}
                  onChange={() => handleMeasureToggle(measure.name)}
                  className="mr-2 h-4 w-4 text-blue-600 rounded border-gray-300"
                  disabled={disabled}
                />
                <span className="text-sm text-gray-700">
                  {measure.label} <span className="text-gray-400">({measure.type})</span>
                </span>
              </label>
            ))}
          </div>
        </div>
      )}

      {/* Basic Filters */}
      {selectedDimensions.length > 0 && (
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            Filters
          </label>
          <div className="space-y-2">
            {selectedDimensions.slice(0, 3).map((dimensionName) => {
              const dimension = parsedModel.dimensions.find(d => d.name === dimensionName)
              return (
                <div key={dimensionName} className="flex items-center space-x-2">
                  <span className="text-xs text-gray-600 w-20 truncate">{dimension?.label}:</span>
                  <input
                    type="text"
                    placeholder={`Filter ${dimension?.label || dimensionName}...`}
                    value={filters[dimensionName] || ''}
                    onChange={(e) => handleFilterChange(dimensionName, e.target.value)}
                    className="flex-1 px-2 py-1 text-sm border border-gray-300 rounded focus:outline-none focus:ring-1 focus:ring-blue-500"
                    disabled={disabled}
                  />
                </div>
              )
            })}
          </div>
        </div>
      )}

      {/* Run Query Button */}
      <div className="pt-2">
        <button
          onClick={handleRunQuery}
          disabled={!canRunQuery || disabled || loading}
          className="w-full px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {loading ? 'Running Query...' : 'Run Query'}
        </button>
      </div>

      {/* Selected Summary */}
      {(selectedDimensions.length > 0 || selectedMeasures.length > 0) && (
        <div className="text-xs text-gray-500 bg-gray-50 p-2 rounded">
          Selected: {[...selectedDimensions, ...selectedMeasures].join(', ')}
          {Object.keys(filters).some(k => filters[k]) && (
            <span> | Filters: {Object.entries(filters).filter(([_, v]) => v).map(([k, v]) => `${k}="${v}"`).join(', ')}</span>
          )}
        </div>
      )}
    </div>
  )
}