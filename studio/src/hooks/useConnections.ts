import { useState, useEffect } from 'react'
import axios from 'axios'

const API_BASE = '/api'

export interface Connection {
  id: string
  name: string
  type: string
  is_active: boolean
}

export interface TableInfo {
  name: string
  row_count: number | null
}

export interface ColumnInfo {
  name: string
  type: string
  nullable: boolean
  primary_key: boolean
}

export interface TableSchema {
  name: string
  columns: ColumnInfo[]
  row_count: number | null
}

export interface QueryResult {
  data: Record<string, any>[]
  columns: string[]
  row_count: number
}

export const useConnections = () => {
  const [connections, setConnections] = useState<Connection[]>([])
  const [loading, setLoading] = useState(false)

  const fetchConnections = async () => {
    setLoading(true)
    try {
      const response = await axios.get(`${API_BASE}/connections`)
      setConnections(response.data)
    } catch (error) {
      console.error('Failed to fetch connections:', error)
    } finally {
      setLoading(false)
    }
  }

  const createConnection = async (connectionData: {
    name: string
    type: string
    host?: string
    port?: number
    database?: string
    username?: string
    password?: string
    file_path?: string
  }) => {
    try {
      const response = await axios.post(`${API_BASE}/connections`, connectionData)
      await fetchConnections()
      return response.data
    } catch (error) {
      console.error('Failed to create connection:', error)
      throw error
    }
  }

  const connectToDatabase = async (connectionId: string) => {
    try {
      await axios.post(`${API_BASE}/connections/${connectionId}/connect`)
      await fetchConnections()
    } catch (error) {
      console.error('Failed to connect to database:', error)
      throw error
    }
  }

  const disconnectFromDatabase = async (connectionId: string) => {
    try {
      await axios.post(`${API_BASE}/connections/${connectionId}/disconnect`)
      await fetchConnections()
    } catch (error) {
      console.error('Failed to disconnect from database:', error)
      throw error
    }
  }

  const getTables = async (connectionId: string): Promise<TableInfo[]> => {
    try {
      const response = await axios.get(`${API_BASE}/connections/${connectionId}/tables`)
      return response.data
    } catch (error) {
      console.error('Failed to get tables:', error)
      throw error
    }
  }

  const getTableSchema = async (connectionId: string, tableName: string): Promise<TableSchema> => {
    try {
      const response = await axios.get(`${API_BASE}/connections/${connectionId}/tables/${tableName}/schema`)
      return response.data
    } catch (error) {
      console.error('Failed to get table schema:', error)
      throw error
    }
  }

  const getTableData = async (connectionId: string, tableName: string, limit = 100): Promise<QueryResult> => {
    try {
      const response = await axios.get(`${API_BASE}/connections/${connectionId}/tables/${tableName}/data?limit=${limit}`)
      return response.data
    } catch (error) {
      console.error('Failed to get table data:', error)
      throw error
    }
  }

  const executeQuery = async (connectionId: string, query: string, limit = 1000): Promise<QueryResult> => {
    try {
      const response = await axios.post(`${API_BASE}/connections/${connectionId}/query`, { query, limit })
      return response.data
    } catch (error) {
      console.error('Failed to execute query:', error)
      throw error
    }
  }

  useEffect(() => {
    fetchConnections()
  }, [])

  return {
    connections,
    loading,
    createConnection,
    connectToDatabase,
    disconnectFromDatabase,
    getTables,
    getTableSchema,
    getTableData,
    executeQuery,
    refresh: fetchConnections
  }
}