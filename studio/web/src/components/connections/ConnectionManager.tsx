import { useState } from 'react'
import { useConnections, Connection } from '../../hooks/useConnections'
import { Database, Plus, Trash2, Power, PowerOff } from 'lucide-react'

export const ConnectionManager: React.FC = () => {
  const { connections, loading, createConnection, connectToDatabase, disconnectFromDatabase } = useConnections()
  const [showForm, setShowForm] = useState(false)
  const [formData, setFormData] = useState({
    name: '',
    type: 'postgresql',
    host: '',
    port: 5432,
    database: '',
    username: '',
    password: ''
  })
  const [error, setError] = useState('')
  const [submitting, setSubmitting] = useState(false)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!formData.name || !formData.host || !formData.database) {
      setError('Name, host, and database are required')
      return
    }

    setSubmitting(true)
    setError('')

    try {
      await createConnection(formData)
      setFormData({
        name: '',
        type: 'postgresql',
        host: '',
        port: 5432,
        database: '',
        username: '',
        password: ''
      })
      setShowForm(false)
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Failed to create connection')
    } finally {
      setSubmitting(false)
    }
  }

  const handleConnect = async (connectionId: string) => {
    try {
      await connectToDatabase(connectionId)
    } catch (err) {
      console.error('Failed to connect:', err)
    }
  }

  const handleDisconnect = async (connectionId: string) => {
    try {
      await disconnectFromDatabase(connectionId)
    } catch (err) {
      console.error('Failed to disconnect:', err)
    }
  }

  return (
    <div className="connection-manager">
      <div className="connection-actions">
        <button 
          onClick={() => setShowForm(!showForm)}
          className="btn btn-primary btn-small btn-with-icon"
          disabled={submitting}
        >
          <Plus size={12} />
          {showForm ? 'Cancel' : 'Add Connection'}
        </button>
      </div>

      {showForm && (
        <form onSubmit={handleSubmit} className="connection-form">
          <div className="form-group">
            <input
              type="text"
              placeholder="Connection name"
              value={formData.name}
              onChange={(e) => setFormData({ ...formData, name: e.target.value })}
              disabled={submitting}
            />
          </div>
          
          <div className="form-group">
            <select
              value={formData.type}
              onChange={(e) => setFormData({ ...formData, type: e.target.value })}
              disabled={submitting}
            >
              <option value="postgresql">PostgreSQL</option>
              <option value="mysql">MySQL</option>
              <option value="sqlite">SQLite</option>
              <option value="duckdb">DuckDB</option>
            </select>
          </div>

          <div className="form-group">
            <input
              type="text"
              placeholder="Host"
              value={formData.host}
              onChange={(e) => setFormData({ ...formData, host: e.target.value })}
              disabled={submitting}
            />
          </div>

          <div className="form-group">
            <input
              type="number"
              placeholder="Port"
              value={formData.port}
              onChange={(e) => setFormData({ ...formData, port: parseInt(e.target.value) || 5432 })}
              disabled={submitting}
            />
          </div>

          <div className="form-group">
            <input
              type="text"
              placeholder="Database"
              value={formData.database}
              onChange={(e) => setFormData({ ...formData, database: e.target.value })}
              disabled={submitting}
            />
          </div>

          <div className="form-group">
            <input
              type="text"
              placeholder="Username"
              value={formData.username}
              onChange={(e) => setFormData({ ...formData, username: e.target.value })}
              disabled={submitting}
            />
          </div>

          <div className="form-group">
            <input
              type="password"
              placeholder="Password"
              value={formData.password}
              onChange={(e) => setFormData({ ...formData, password: e.target.value })}
              disabled={submitting}
            />
          </div>

          <button 
            type="submit"
            disabled={submitting || !formData.name || !formData.host || !formData.database}
            className="btn btn-primary btn-small"
          >
            {submitting ? 'Creating...' : 'Create Connection'}
          </button>
          
          {error && <div className="error-message">{error}</div>}
        </form>
      )}

      <div className="connections-list">
        {loading ? (
          <div className="loading">Loading connections...</div>
        ) : connections.length === 0 ? (
          <div className="empty-state">No connections configured</div>
        ) : (
          <div className="connection-items">
            {connections.map(connection => (
              <ConnectionItem 
                key={connection.id}
                connection={connection}
                onConnect={handleConnect}
                onDisconnect={handleDisconnect}
              />
            ))}
          </div>
        )}
      </div>
    </div>
  )
}

interface ConnectionItemProps {
  connection: Connection
  onConnect: (id: string) => void
  onDisconnect: (id: string) => void
}

const ConnectionItem: React.FC<ConnectionItemProps> = ({ connection, onConnect, onDisconnect }) => {
  return (
    <div className="connection-item">
      <div className="connection-info">
        <div className="connection-header">
          <Database size={12} className="connection-icon" />
          <span className="connection-name">{connection.name}</span>
          <span className={`connection-status ${connection.is_active ? 'active' : 'inactive'}`}>
            {connection.is_active ? 'Connected' : 'Disconnected'}
          </span>
        </div>
        <div className="connection-meta">
          {connection.type}
        </div>
      </div>
      
      <div className="connection-actions-item">
        {connection.is_active ? (
          <button 
            onClick={() => onDisconnect(connection.id)}
            className="btn btn-small btn-secondary btn-with-icon"
            title="Disconnect"
          >
            <PowerOff size={10} />
          </button>
        ) : (
          <button 
            onClick={() => onConnect(connection.id)}
            className="btn btn-small btn-secondary btn-with-icon"
            title="Connect"
          >
            <Power size={10} />
          </button>
        )}
      </div>
    </div>
  )
}