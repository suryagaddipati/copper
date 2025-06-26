import { useState } from 'react'

interface ConnectionFormProps {
  onSubmit: (data: ConnectionFormData) => void
  onCancel: () => void
  loading?: boolean
}

export interface ConnectionFormData {
  name: string
  type: string
  host?: string
  port?: number
  database?: string
  username?: string
  password?: string
  file_path?: string
}

export const ConnectionForm = ({ onSubmit, onCancel, loading }: ConnectionFormProps) => {
  const [formData, setFormData] = useState<ConnectionFormData>({
    name: '',
    type: 'duckdb'
  })

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    onSubmit(formData)
  }

  const handleChange = (field: keyof ConnectionFormData, value: string | number) => {
    setFormData(prev => ({
      ...prev,
      [field]: value
    }))
  }

  const isFileBasedDb = formData.type === 'duckdb' || formData.type === 'sqlite'

  return (
    <div className="connection-form">
      <h3>Create Database Connection</h3>
      
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="name">Connection Name</label>
          <input
            id="name"
            type="text"
            value={formData.name}
            onChange={(e) => handleChange('name', e.target.value)}
            placeholder="My Database"
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="type">Database Type</label>
          <select
            id="type"
            value={formData.type}
            onChange={(e) => handleChange('type', e.target.value)}
          >
            <option value="duckdb">DuckDB</option>
            <option value="sqlite">SQLite</option>
            <option value="postgres">PostgreSQL</option>
            <option value="mysql">MySQL</option>
          </select>
        </div>

        {isFileBasedDb ? (
          <div className="form-group">
            <label htmlFor="file_path">Database File Path</label>
            <input
              id="file_path"
              type="text"
              value={formData.file_path || ''}
              onChange={(e) => handleChange('file_path', e.target.value)}
              placeholder="/path/to/database.db"
            />
            <small>Leave empty for in-memory database</small>
          </div>
        ) : (
          <>
            <div className="form-group">
              <label htmlFor="host">Host</label>
              <input
                id="host"
                type="text"
                value={formData.host || ''}
                onChange={(e) => handleChange('host', e.target.value)}
                placeholder="localhost"
                required
              />
            </div>

            <div className="form-group">
              <label htmlFor="port">Port</label>
              <input
                id="port"
                type="number"
                value={formData.port || ''}
                onChange={(e) => handleChange('port', parseInt(e.target.value))}
                placeholder={formData.type === 'postgres' ? '5432' : '3306'}
              />
            </div>

            <div className="form-group">
              <label htmlFor="database">Database Name</label>
              <input
                id="database"
                type="text"
                value={formData.database || ''}
                onChange={(e) => handleChange('database', e.target.value)}
                placeholder="my_database"
                required
              />
            </div>

            <div className="form-group">
              <label htmlFor="username">Username</label>
              <input
                id="username"
                type="text"
                value={formData.username || ''}
                onChange={(e) => handleChange('username', e.target.value)}
                placeholder="username"
              />
            </div>

            <div className="form-group">
              <label htmlFor="password">Password</label>
              <input
                id="password"
                type="password"
                value={formData.password || ''}
                onChange={(e) => handleChange('password', e.target.value)}
                placeholder="password"
              />
            </div>
          </>
        )}

        <div className="form-actions">
          <button type="button" onClick={onCancel} disabled={loading}>
            Cancel
          </button>
          <button type="submit" disabled={loading || !formData.name}>
            {loading ? 'Creating...' : 'Create Connection'}
          </button>
        </div>
      </form>
    </div>
  )
}