import { useState, useEffect } from 'react'
import { registerCopperLanguage } from './copper-language'
import { CopperEditor } from './components/CopperEditor'
import { ExamplesSidebar } from './components/ExamplesSidebar'
import { ValidationResults } from './components/ValidationResults'
import { useParseCode } from './hooks/useParseCode'
import { useExamples } from './hooks/useExamples'

const defaultCode = `# Welcome to the Copper Language Live Parser
# Select an example from the sidebar or start typing your own Copper code
# This demonstrates enhanced syntax highlighting

model: sample_orders {
  # Primary key dimension
  dimension: order_id {
    type: string
    expression: Orders[OrderID] ;;
    primary_key: yes
    label: "Order ID"
    description: "Unique identifier for each order"
  }
  
  # Date dimension with DAX function
  dimension: order_date {
    type: date
    expression: DATE(YEAR(Orders[OrderDate]), MONTH(Orders[OrderDate]), DAY(Orders[OrderDate])) ;;
    label: "Order Date"
  }
  
  # Complex measure with multi-line DAX
  measure: total_revenue {
    type: sum
    expression: 
      VAR CurrentRevenue = SUM(Orders[Amount])
      VAR FilteredRevenue = CALCULATE(
        CurrentRevenue,
        FILTER(Orders, Orders[Status] = "Completed")
      )
      RETURN FilteredRevenue ;;
    value_format: usd
    label: "Total Revenue"
  }
  
  # Boolean dimension
  dimension: is_weekend {
    type: yesno
    expression: WEEKDAY(Orders[OrderDate]) IN {1, 7} ;;
    label: "Weekend Order"
  }
}`

function App() {
  const [code, setCode] = useState(defaultCode)
  const [isDarkTheme, setIsDarkTheme] = useState(false)
  const { parseResult, isLoading, parseCode } = useParseCode(code)
  const { examples, loadingExamples } = useExamples()

  // Register language early and update document theme
  useEffect(() => {
    registerCopperLanguage()
  }, [])

  useEffect(() => {
    document.documentElement.setAttribute('data-theme', isDarkTheme ? 'dark' : 'light')
  }, [isDarkTheme])

  const handleLoadExample = (example: { name: string; content: string; description: string }) => {
    setCode(example.content)
  }

  const handleClearCode = () => {
    setCode('')
  }

  const handleToggleTheme = () => {
    setIsDarkTheme(!isDarkTheme)
  }

  const handleCodeChange = (value: string) => {
    setCode(value)
  }

  return (
    <div className="app">
      <header className="header">
        <div className="container">
          <h1>Copper Language Parser</h1>
          <p>Live parsing and validation for the Copper metadata language</p>
        </div>
      </header>

      <main className="main-content container">
        <div className="editor-panel">
          <CopperEditor
            code={code}
            onChange={handleCodeChange}
            onParse={parseCode}
            onClear={handleClearCode}
            isLoading={isLoading}
            isDarkTheme={isDarkTheme}
            onToggleTheme={handleToggleTheme}
            parseResult={parseResult}
          />
        </div>

        <div className="sidebar">
          <ExamplesSidebar
            examples={examples}
            loadingExamples={loadingExamples}
            onLoadExample={handleLoadExample}
          />
          <ValidationResults
            parseResult={parseResult}
            isLoading={isLoading}
          />
        </div>
      </main>
    </div>
  )
}

export default App