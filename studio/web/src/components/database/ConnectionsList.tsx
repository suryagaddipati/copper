import { Connection } from '../../hooks/useConnections'

interface ConnectionsListProps {
  connections: Connection[]
  onConnect: (connectionId: string) => void
  onDisconnect: (connectionId: string) => void
  onSelectConnection: (connection: Connection) => void
  selectedConnectionId?: string
  loading?: boolean
}

export const ConnectionsList = ({ 
  connections, 
  onConnect, 
  onDisconnect, 
  onSelectConnection,
  selectedConnectionId,
  loading 
}: ConnectionsListProps) => {
  
  const getStatusColor = (isActive: boolean) => {
    return isActive ? '#22c55e' : '#ef4444'
  }

  const getStatusText = (isActive: boolean) => {
    return isActive ? 'Connected' : 'Disconnected'
  }

  if (connections.length === 0) {
    return (
      <div className="connections-empty">
        <p>No database connections yet.</p>
        <p>Create your first connection to get started.</p>
      </div>
    )
  }

  return (
    <div className="connections-list">
      <h3>Database Connections</h3>
      
      {connections.map((connection) => (
        <div 
          key={connection.id} 
          className={`connection-item ${selectedConnectionId === connection.id ? 'selected' : ''}`}
          onClick={() => onSelectConnection(connection)}
        >
          <div className="connection-header">
            <div className="connection-info">
              <h4>{connection.name}</h4>
              <span className="connection-type">{connection.type.toUpperCase()}</span>
            </div>
            
            <div className="connection-status">
              <span 
                className="status-indicator"
                style={{ backgroundColor: getStatusColor(connection.is_active) }}
              />
              <span className="status-text">
                {getStatusText(connection.is_active)}
              </span>
            </div>
          </div>

          <div className="connection-actions">
            {connection.is_active ? (
              <button
                onClick={(e) => {
                  e.stopPropagation()
                  onDisconnect(connection.id)
                }}
                disabled={loading}
                className="disconnect-btn"
              >
                Disconnect
              </button>
            ) : (
              <button
                onClick={(e) => {
                  e.stopPropagation()
                  onConnect(connection.id)
                }}
                disabled={loading}
                className="connect-btn"
              >
                Connect
              </button>
            )}
          </div>
        </div>
      ))}
    </div>
  )
}