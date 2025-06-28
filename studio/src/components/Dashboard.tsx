import { useState, useEffect } from 'react'
import { SimpleChart } from './SimpleChart'
import { ModelExplorer } from './ModelExplorer'
import { useConnections, Connection } from '../hooks/useConnections'
import { Database, Plus, Power, PowerOff } from 'lucide-react'
import axios from 'axios'

interface QueryRequest {
  modelName: string
  selectedDimensions: string[]
  selectedMeasures: string[]
  filters: Record<string, string>
}

interface QueryData {
  data: Array<Record<string, any>>
  columns: string[]
  row_count: number
  sql: string
}

export function Dashboard() {
  const [chartData, setChartData] = useState<QueryData | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string>('')
  const [showConnectionForm, setShowConnectionForm] = useState(false)
  const [selectedModelFile, setSelectedModelFile] = useState<string>('')
  const [connectionFormData, setConnectionFormData] = useState({
    name: '',
    type: 'sqlite',
    host: '',
    port: 5432,
    database: '',
    username: '',
    password: '',
    file_path: ''
  })
  
  const { 
    connections, 
    loading: connectionsLoading, 
    createConnection, 
    connectToDatabase, 
    disconnectFromDatabase
  } = useConnections()
  
  const activeConnection = connections.find(conn => conn.is_active)

  const [availableModels, setAvailableModels] = useState<string[]>([])

  // Load available models from filesystem
  useEffect(() => {
    const loadModels = async () => {
      try {
        const response = await axios.get('http://localhost:8000/models')
        setAvailableModels(response.data.models)
        setSelectedModelFile(response.data.models[0] || '')
      } catch (err) {
        console.error('Failed to load models:', err)
      }
    }
    loadModels()
  }, [])

  const handleQueryRequest = async (queryRequest: QueryRequest) => {
    if (!activeConnection) {
      setError('No active connection. Please connect to a database first.')
      return
    }

    if (!selectedModelFile) {
      setError('Please select a model file first')
      return
    }

    setLoading(true)
    setError('')

    try {
      const response = await axios.post<QueryData>('http://localhost:8000/explore', {
        connection_id: activeConnection.id,
        model_file: selectedModelFile,
        model_name: queryRequest.modelName,
        selected_dimensions: queryRequest.selectedDimensions,
        selected_measures: queryRequest.selectedMeasures,
        filters: queryRequest.filters,
        limit: 100
      })
      
      setChartData(response.data)
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Failed to query data')
    } finally {
      setLoading(false)
    }
  }

  const handleCreateConnection = async () => {
    try {
      await createConnection(connectionFormData)
      setShowConnectionForm(false)
      setConnectionFormData({
        name: '',
        type: 'sqlite',
        host: '',
        port: 5432,
        database: '',
        username: '',
        password: '',
        file_path: ''
      })
    } catch (err: any) {
      setError(`Failed to create connection: ${err.response?.data?.detail || err.message}`)
    }
  }

  const handleConnect = async (connectionId: string) => {
    try {
      await connectToDatabase(connectionId)
    } catch (err: any) {
      setError(`Failed to connect: ${err.response?.data?.detail || err.message}`)
    }
  }

  const handleDisconnect = async (connectionId: string) => {
    try {
      await disconnectFromDatabase(connectionId)
    } catch (err: any) {
      setError(`Failed to disconnect: ${err.response?.data?.detail || err.message}`)
    }
  }

  const renderConnectionManager = () => {
    return (
      <div className="bg-white border border-gray-200 rounded-lg p-4 mb-4">
        <div className="flex items-center justify-between mb-3">
          <h4 className="text-sm font-medium text-gray-900 flex items-center">
            <Database className="w-4 h-4 mr-2" />
            Database Connections
          </h4>
          <button
            onClick={() => setShowConnectionForm(!showConnectionForm)}
            className="p-1 text-gray-500 hover:text-gray-700 rounded"
          >
            <Plus className="w-4 h-4" />
          </button>
        </div>

        {/* Connection Form */}
        {showConnectionForm && (
          <div className="mb-4 p-3 bg-gray-50 border border-gray-200 rounded">
            <div className="grid grid-cols-2 gap-2 mb-2">
              <input
                type="text"
                placeholder="Connection name"
                value={connectionFormData.name}
                onChange={(e) => setConnectionFormData({...connectionFormData, name: e.target.value})}
                className="px-2 py-1 text-xs border border-gray-300 rounded"
              />
              <select
                value={connectionFormData.type}
                onChange={(e) => setConnectionFormData({...connectionFormData, type: e.target.value})}
                className="px-2 py-1 text-xs border border-gray-300 rounded"
              >
                <option value="sqlite">SQLite</option>
                <option value="postgresql">PostgreSQL</option>
                <option value="mysql">MySQL</option>
                <option value="duckdb">DuckDB</option>
              </select>
            </div>

            {connectionFormData.type === 'sqlite' ? (
              <input
                type="text"
                placeholder="Database file path"
                value={connectionFormData.file_path}
                onChange={(e) => setConnectionFormData({...connectionFormData, file_path: e.target.value})}
                className="w-full px-2 py-1 text-xs border border-gray-300 rounded mb-2"
              />
            ) : (
              <div className="grid grid-cols-2 gap-2 mb-2">
                <input
                  type="text"
                  placeholder="Host"
                  value={connectionFormData.host}
                  onChange={(e) => setConnectionFormData({...connectionFormData, host: e.target.value})}
                  className="px-2 py-1 text-xs border border-gray-300 rounded"
                />
                <input
                  type="number"
                  placeholder="Port"
                  value={connectionFormData.port}
                  onChange={(e) => setConnectionFormData({...connectionFormData, port: parseInt(e.target.value)})}
                  className="px-2 py-1 text-xs border border-gray-300 rounded"
                />
                <input
                  type="text"
                  placeholder="Database"
                  value={connectionFormData.database}
                  onChange={(e) => setConnectionFormData({...connectionFormData, database: e.target.value})}
                  className="px-2 py-1 text-xs border border-gray-300 rounded"
                />
                <input
                  type="text"
                  placeholder="Username"
                  value={connectionFormData.username}
                  onChange={(e) => setConnectionFormData({...connectionFormData, username: e.target.value})}
                  className="px-2 py-1 text-xs border border-gray-300 rounded"
                />
                <input
                  type="password"
                  placeholder="Password"
                  value={connectionFormData.password}
                  onChange={(e) => setConnectionFormData({...connectionFormData, password: e.target.value})}
                  className="px-2 py-1 text-xs border border-gray-300 rounded col-span-2"
                />
              </div>
            )}

            <div className="flex gap-2">
              <button
                onClick={handleCreateConnection}
                disabled={!connectionFormData.name || connectionsLoading}
                className="px-3 py-1 bg-blue-600 text-white text-xs rounded hover:bg-blue-700 disabled:opacity-50"
              >
                Create
              </button>
              <button
                onClick={() => setShowConnectionForm(false)}
                className="px-3 py-1 bg-gray-300 text-gray-700 text-xs rounded hover:bg-gray-400"
              >
                Cancel
              </button>
            </div>
          </div>
        )}

        {/* Connection List */}
        <div className="space-y-2 max-h-32 overflow-y-auto">
          {connections.length === 0 ? (
            <p className="text-xs text-gray-500 italic">No connections yet. Click + to add one.</p>
          ) : (
            connections.map((connection) => (
              <div key={connection.id} className="flex items-center justify-between p-2 bg-gray-50 rounded border">
                <div className="flex items-center flex-1 min-w-0">
                  <Database className="w-3 h-3 mr-2 text-gray-400" />
                  <div className="flex-1 min-w-0">
                    <div className="text-xs font-medium text-gray-900 truncate">{connection.name}</div>
                    <div className="text-xs text-gray-500 capitalize">{connection.type}</div>
                  </div>
                  <span className={`text-xs px-1 py-0.5 rounded ${connection.is_active ? 'bg-green-100 text-green-700' : 'bg-gray-100 text-gray-600'}`}>
                    {connection.is_active ? 'Active' : 'Inactive'}
                  </span>
                </div>
                <button
                  onClick={() => connection.is_active ? handleDisconnect(connection.id) : handleConnect(connection.id)}
                  className="ml-2 p-1 text-gray-500 hover:text-gray-700"
                >
                  {connection.is_active ? <PowerOff className="w-3 h-3" /> : <Power className="w-3 h-3" />}
                </button>
              </div>
            ))
          )}
        </div>
      </div>
    )
  }

  return (
    <div className="dashboard-container p-6">
      <div className="dashboard-header mb-6">
        <h2 className="text-2xl font-bold text-gray-900">BI Dashboard</h2>
        <p className="text-gray-600">Explore your Copper models with interactive data visualization</p>
      </div>

      <div className="dashboard-layout grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Left Panel - Connections & Model Explorer */}
        <div className="lg:col-span-1 space-y-4">
          {/* Database Connections */}
          {renderConnectionManager()}
          
          {/* Model File Selector */}
          <div className="bg-white border border-gray-200 rounded-lg p-4 mb-4">
            <h4 className="text-sm font-medium text-gray-900 mb-3">Select Model</h4>
            {selectedModelFile && selectedModelFile.includes('ufc-analytics') && (
              <div className="mb-3 p-2 bg-blue-50 border border-blue-200 rounded text-xs text-blue-800">
                💡 UFC models require SQLite connection to: <code>/home/surya/code/copper/example-projects/ufc-analytics/ufc_sample.db</code>
              </div>
            )}
            <select
              value={selectedModelFile}
              onChange={(e) => setSelectedModelFile(e.target.value)}
              className="w-full px-3 py-2 text-sm border border-gray-300 rounded focus:outline-none focus:ring-1 focus:ring-blue-500"
              disabled={!activeConnection}
            >
              <option value="">Choose a model file...</option>
              {availableModels.map((model) => {
                const fileName = model.split('/').pop()?.replace('.copper', '') || model
                const isUFC = model.includes('ufc-analytics')
                const isEcommerce = model.includes('ecommerce-demo')
                let dbHint = ''
                if (isUFC) dbHint = ' (UFC DB)'
                if (isEcommerce) dbHint = ' (Ecommerce DB)'
                return (
                  <option key={model} value={model}>
                    {fileName}{dbHint}
                  </option>
                )
              })}
            </select>
          </div>

          {/* Model Explorer - Show when model is selected */}
          {selectedModelFile && (
            <ModelExplorer 
              onQueryRequest={handleQueryRequest}
              disabled={!activeConnection}
              loading={loading}
              modelName="auto"
              modelFile={selectedModelFile}
            />
          )}
        </div>

        {/* Right Panel - Results */}
        <div className="lg:col-span-2">
          {error && (
            <div className="error-message mb-4 p-3 bg-red-50 border border-red-200 rounded-md text-red-700">
              {error}
            </div>
          )}

          {chartData ? (
            <div className="space-y-4">
              {/* SQL Display */}
              <div className="bg-gray-50 p-3 rounded-lg">
                <h4 className="text-sm font-medium text-gray-700 mb-2">Generated SQL</h4>
                <pre className="text-xs text-gray-600 overflow-x-auto bg-white p-2 rounded border">
                  {chartData.sql}
                </pre>
              </div>

              {/* Chart */}
              <div className="bg-white border border-gray-200 rounded-lg p-4">
                <SimpleChart data={chartData} />
              </div>
            </div>
          ) : !activeConnection ? (
            <div className="bg-blue-50 border-2 border-dashed border-blue-300 rounded-lg p-8 text-center">
              <Database className="w-12 h-12 text-blue-400 mx-auto mb-4" />
              <h3 className="text-lg font-medium text-gray-900 mb-2">Connect to Database</h3>
              <p className="text-gray-600 mb-4">Create a database connection to start exploring your data with Copper models.</p>
              <div className="text-sm text-gray-500">
                <p>💡 Try the UFC sample database:</p>
                <code className="bg-gray-100 px-2 py-1 rounded text-xs">
                  /home/surya/code/copper/example-projects/ufc-analytics/ufc_sample.db
                </code>
              </div>
            </div>
          ) : (
            <div className="bg-gray-50 border-2 border-dashed border-gray-300 rounded-lg p-8 text-center">
              <h3 className="text-lg font-medium text-gray-900 mb-2">Ready to Explore</h3>
              <p className="text-gray-600">Select a model and choose dimensions or measures to start exploring your data.</p>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}