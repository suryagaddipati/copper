import { useState, useEffect } from 'react'
import axios from 'axios'

const API_BASE_URL = 'http://localhost:8000'

interface ParseResult {
  valid: boolean
  errors: string[]
  warnings: string[]
  statistics: {
    total_models: number
    total_views: number
    total_dimensions: number
    total_measures: number
    total_joins: number
  }
  models: any[]
  views: any[]
}

export const useParseCode = (code: string) => {
  const [parseResult, setParseResult] = useState<ParseResult | null>(null)
  const [isLoading, setIsLoading] = useState(false)

  const parseCode = async (content: string) => {
    if (!content.trim()) {
      setParseResult(null)
      return
    }

    try {
      setIsLoading(true)
      const response = await axios.post(`${API_BASE_URL}/parse`, {
        content: content
      })
      setParseResult(response.data)
    } catch (error) {
      console.error('Parse error:', error)
      setParseResult({
        valid: false,
        errors: ['Failed to connect to parser API'],
        warnings: [],
        statistics: {
          total_models: 0,
          total_views: 0,
          total_dimensions: 0,
          total_measures: 0,
          total_joins: 0
        },
        models: [],
        views: []
      })
    } finally {
      setIsLoading(false)
    }
  }

  // Parse code whenever it changes with debouncing
  useEffect(() => {
    const timeoutId = setTimeout(() => {
      parseCode(code)
    }, 500)

    return () => clearTimeout(timeoutId)
  }, [code])

  return {
    parseResult,
    isLoading,
    parseCode: () => parseCode(code)
  }
}