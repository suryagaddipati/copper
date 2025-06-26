import { useState } from 'react'
import { Connection, useConnections } from '../../hooks/useConnections'
import { ConnectionForm, ConnectionFormData } from './ConnectionForm'
import { ConnectionsList } from './ConnectionsList'
import { TablesBrowser } from './TablesBrowser'

export const DatabaseExplorer = () => {
  const [showForm, setShowForm] = useState(false)
  const [selectedConnection, setSelectedConnection] = useState<Connection | null>(null)
  const [formLoading, setFormLoading] = useState(false)

  const {
    connections,
    loading,
    createConnection,
    connectToDatabase,
    disconnectFromDatabase
  } = useConnections()

  const handleCreateConnection = async (data: ConnectionFormData) => {
    setFormLoading(true)
    try {
      await createConnection(data)
      setShowForm(false)
    } catch (error) {
      console.error('Failed to create connection:', error)
    } finally {
      setFormLoading(false)
    }
  }

  const handleConnect = async (connectionId: string) => {
    try {
      await connectToDatabase(connectionId)
    } catch (error) {
      console.error('Failed to connect:', error)
    }
  }

  const handleDisconnect = async (connectionId: string) => {
    try {
      await disconnectFromDatabase(connectionId)
      if (selectedConnection?.id === connectionId) {
        setSelectedConnection(null)
      }
    } catch (error) {
      console.error('Failed to disconnect:', error)
    }
  }

  const handleSelectConnection = (connection: Connection) => {
    if (connection.is_active) {
      setSelectedConnection(connection)
    }
  }

  return (
    <div className="database-explorer">
      <div className="explorer-header">
        <h2>Database Explorer</h2>
        <button 
          onClick={() => setShowForm(true)}
          disabled={showForm}
          className="create-connection-btn"
        >
          + New Connection
        </button>
      </div>

      {showForm && (
        <div className="modal-overlay">
          <div className="modal-content">
            <ConnectionForm
              onSubmit={handleCreateConnection}
              onCancel={() => setShowForm(false)}
              loading={formLoading}
            />
          </div>
        </div>
      )}

      <div className="explorer-content">
        <div className="connections-panel">
          <ConnectionsList
            connections={connections}
            onConnect={handleConnect}
            onDisconnect={handleDisconnect}
            onSelectConnection={handleSelectConnection}
            selectedConnectionId={selectedConnection?.id}
            loading={loading}
          />
        </div>

        <div className="tables-panel">
          {selectedConnection ? (
            <TablesBrowser
              connectionId={selectedConnection.id}
              connectionName={selectedConnection.name}
            />
          ) : (
            <div className="no-connection">
              <p>Select a connected database to explore tables</p>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}