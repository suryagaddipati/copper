import { useState, useEffect } from 'react'
import axios from 'axios'

const API_BASE = 'http://localhost:8000'

export interface CopperFile {
  name: string
  path: string
  content: string
  relative_path: string
}

export interface Project {
  id: string
  name: string
  path: string
  file_count: number
  created_at: string
}

export const useProjects = () => {
  const [projects, setProjects] = useState<Project[]>([])
  const [loading, setLoading] = useState(false)

  const fetchProjects = async () => {
    setLoading(true)
    try {
      const response = await axios.get(`${API_BASE}/projects`)
      setProjects(response.data)
    } catch (error) {
      console.error('Failed to fetch projects:', error)
    } finally {
      setLoading(false)
    }
  }

  const loadProject = async (path: string, name?: string): Promise<Project> => {
    try {
      const response = await axios.post(`${API_BASE}/projects`, { path, name })
      await fetchProjects()
      return response.data
    } catch (error) {
      console.error('Failed to load project:', error)
      throw error
    }
  }

  const deleteProject = async (projectId: string) => {
    try {
      await axios.delete(`${API_BASE}/projects/${projectId}`)
      await fetchProjects()
    } catch (error) {
      console.error('Failed to delete project:', error)
      throw error
    }
  }

  const refreshProject = async (projectId: string): Promise<Project> => {
    try {
      const response = await axios.post(`${API_BASE}/projects/${projectId}/refresh`)
      await fetchProjects()
      return response.data
    } catch (error) {
      console.error('Failed to refresh project:', error)
      throw error
    }
  }

  const getProjectFiles = async (projectId: string): Promise<CopperFile[]> => {
    try {
      const response = await axios.get(`${API_BASE}/projects/${projectId}/files`)
      return response.data
    } catch (error) {
      console.error('Failed to get project files:', error)
      throw error
    }
  }

  useEffect(() => {
    fetchProjects()
  }, [])

  return {
    projects,
    loading,
    loadProject,
    deleteProject,
    refreshProject,
    getProjectFiles,
    refresh: fetchProjects
  }
}