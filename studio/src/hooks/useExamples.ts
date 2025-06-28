import { useState, useEffect } from 'react'
import axios from 'axios'

const API_BASE_URL = '/api'

interface ExampleFile {
  name: string
  content: string
  description: string
}

export const useExamples = () => {
  const [examples, setExamples] = useState<ExampleFile[]>([])
  const [loadingExamples, setLoadingExamples] = useState(true)

  const fetchExamples = async () => {
    try {
      setLoadingExamples(true)
      const response = await axios.get(`${API_BASE_URL}/examples`)
      setExamples(response.data)
    } catch (error) {
      console.error('Failed to fetch examples:', error)
    } finally {
      setLoadingExamples(false)
    }
  }

  useEffect(() => {
    fetchExamples()
  }, [])

  return {
    examples,
    loadingExamples,
    refetchExamples: fetchExamples
  }
}