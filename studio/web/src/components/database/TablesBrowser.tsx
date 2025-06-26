import { useState, useEffect } from 'react'
import { TableInfo, TableSchema, QueryResult, useConnections } from '../../hooks/useConnections'

interface TablesBrowserProps {
  connectionId: string
  connectionName: string
}

export const TablesBrowser = ({ connectionId, connectionName }: TablesBrowserProps) => {
  const [tables, setTables] = useState<TableInfo[]>([])
  const [selectedTable, setSelectedTable] = useState<string | null>(null)
  const [tableSchema, setTableSchema] = useState<TableSchema | null>(null)
  const [tableData, setTableData] = useState<QueryResult | null>(null)
  const [loading, setLoading] = useState(false)
  const [view, setView] = useState<'schema' | 'data'>('schema')

  const { getTables, getTableSchema, getTableData } = useConnections()

  useEffect(() => {
    loadTables()
  }, [connectionId])

  const loadTables = async () => {
    setLoading(true)
    try {
      const tablesData = await getTables(connectionId)
      setTables(tablesData)
    } catch (error) {
      console.error('Failed to load tables:', error)
    } finally {
      setLoading(false)
    }
  }

  const selectTable = async (tableName: string) => {
    setSelectedTable(tableName)
    setTableSchema(null)
    setTableData(null)
    setLoading(true)

    try {
      if (view === 'schema') {
        const schema = await getTableSchema(connectionId, tableName)
        setTableSchema(schema)
      } else {
        const data = await getTableData(connectionId, tableName, 100)
        setTableData(data)
      }
    } catch (error) {
      console.error(`Failed to load table ${view}:`, error)
    } finally {
      setLoading(false)
    }
  }

  const switchView = async (newView: 'schema' | 'data') => {
    if (!selectedTable) return
    
    setView(newView)
    setLoading(true)

    try {
      if (newView === 'schema' && !tableSchema) {
        const schema = await getTableSchema(connectionId, selectedTable)
        setTableSchema(schema)
      } else if (newView === 'data' && !tableData) {
        const data = await getTableData(connectionId, selectedTable, 100)
        setTableData(data)
      }
    } catch (error) {
      console.error(`Failed to load table ${newView}:`, error)
    } finally {
      setLoading(false)
    }
  }

  if (loading && tables.length === 0) {
    return <div className="loading">Loading tables...</div>
  }

  return (
    <div className="tables-browser">
      <div className="browser-header">
        <h3>Tables in {connectionName}</h3>
        <button onClick={loadTables} disabled={loading}>
          Refresh
        </button>
      </div>

      <div className="browser-content">
        <div className="tables-list">
          <h4>Tables ({tables.length})</h4>
          {tables.map((table) => (
            <div
              key={table.name}
              className={`table-item ${selectedTable === table.name ? 'selected' : ''}`}
              onClick={() => selectTable(table.name)}
            >
              <span className="table-name">{table.name}</span>
              {table.row_count !== null && (
                <span className="table-count">{table.row_count.toLocaleString()} rows</span>
              )}
            </div>
          ))}
        </div>

        {selectedTable && (
          <div className="table-details">
            <div className="table-details-header">
              <h4>{selectedTable}</h4>
              <div className="view-tabs">
                <button
                  className={view === 'schema' ? 'active' : ''}
                  onClick={() => switchView('schema')}
                >
                  Schema
                </button>
                <button
                  className={view === 'data' ? 'active' : ''}
                  onClick={() => switchView('data')}
                >
                  Data
                </button>
              </div>
            </div>

            <div className="table-details-content">
              {loading ? (
                <div className="loading">Loading...</div>
              ) : view === 'schema' && tableSchema ? (
                <div className="schema-view">
                  <div className="schema-info">
                    <span>Columns: {tableSchema.columns.length}</span>
                    {tableSchema.row_count !== null && (
                      <span>Rows: {tableSchema.row_count.toLocaleString()}</span>
                    )}
                  </div>
                  <table className="schema-table">
                    <thead>
                      <tr>
                        <th>Column</th>
                        <th>Type</th>
                        <th>Nullable</th>
                        <th>Key</th>
                      </tr>
                    </thead>
                    <tbody>
                      {tableSchema.columns.map((column) => (
                        <tr key={column.name}>
                          <td className="column-name">{column.name}</td>
                          <td className="column-type">{column.type}</td>
                          <td>{column.nullable ? 'Yes' : 'No'}</td>
                          <td>{column.primary_key ? 'PK' : ''}</td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              ) : view === 'data' && tableData ? (
                <div className="data-view">
                  <div className="data-info">
                    <span>Showing {tableData.data.length} of {tableData.row_count} rows</span>
                  </div>
                  <div className="data-table-container">
                    <table className="data-table">
                      <thead>
                        <tr>
                          {tableData.columns.map((column) => (
                            <th key={column}>{column}</th>
                          ))}
                        </tr>
                      </thead>
                      <tbody>
                        {tableData.data.map((row, index) => (
                          <tr key={index}>
                            {tableData.columns.map((column) => (
                              <td key={column}>
                                {row[column] !== null ? String(row[column]) : 'NULL'}
                              </td>
                            ))}
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                </div>
              ) : null}
            </div>
          </div>
        )}
      </div>
    </div>
  )
}