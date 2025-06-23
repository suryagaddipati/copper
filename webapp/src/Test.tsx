import React, { useEffect } from 'react'
import Editor from '@monaco-editor/react'
import { registerCopperLanguage } from './copper-language'

const testCode = `model: test_model {
  dimension: customer_id {
    type: string
    expression: Customers[CustomerID] ;;
    primary_key: yes
    label: "Customer ID"
  }
  
  measure: total_revenue {
    type: sum
    expression: SUM(Orders[Amount]) ;;
    value_format: usd
    label: "Total Revenue"
  }
}`

export default function Test() {
  useEffect(() => {
    registerCopperLanguage()
  }, [])

  return (
    <div style={{ height: '100vh', padding: '20px' }}>
      <h1>Copper Syntax Highlighting Test</h1>
      <div style={{ height: '500px', border: '1px solid #ccc' }}>
        <Editor
          height="500px"
          defaultLanguage="copper"
          theme="copper-dark"
          value={testCode}
          options={{
            minimap: { enabled: false },
            fontSize: 14,
            wordWrap: 'on'
          }}
        />
      </div>
    </div>
  )
}