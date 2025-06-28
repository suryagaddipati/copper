import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts'

interface ChartData {
  data: Array<Record<string, any>>
  columns: string[]
  row_count: number
  sql: string
}

interface SimpleChartProps {
  data: ChartData
}

export function SimpleChart({ data }: SimpleChartProps) {
  if (!data.data || data.data.length === 0) {
    return (
      <div className="chart-container p-6 border border-gray-200 rounded-lg">
        <p className="text-gray-500 text-center">No data to display</p>
      </div>
    )
  }

  // For this barebones version, we'll try to create a simple chart
  // Take the first two columns - first as X axis, second as Y axis
  const chartColumns = data.columns.slice(0, 2)
  const xKey = chartColumns[0]
  const yKey = chartColumns[1]

  // If we have numeric data in the second column, use it for the chart
  // Otherwise, show a simple data table
  const hasNumericData = data.data.some(row => 
    typeof row[yKey] === 'number' && !isNaN(row[yKey])
  )

  if (!hasNumericData || chartColumns.length < 2) {
    // Show as a data table instead
    return (
      <div className="chart-container p-6 border border-gray-200 rounded-lg">
        <div className="chart-header mb-4">
          <h3 className="text-lg font-semibold text-gray-900">Data Table</h3>
          <p className="text-sm text-gray-600">
            {data.row_count} rows • SQL: {data.sql}
          </p>
        </div>
        
        <div className="overflow-x-auto">
          <table className="min-w-full border border-gray-200">
            <thead className="bg-gray-50">
              <tr>
                {data.columns.map(col => (
                  <th key={col} className="px-4 py-2 text-left text-sm font-medium text-gray-700 border-b">
                    {col}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {data.data.slice(0, 10).map((row, index) => (
                <tr key={index} className="hover:bg-gray-50">
                  {data.columns.map(col => (
                    <td key={col} className="px-4 py-2 text-sm text-gray-900 border-b">
                      {row[col]?.toString() || '-'}
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
          {data.data.length > 10 && (
            <p className="text-sm text-gray-500 mt-2">
              Showing first 10 of {data.data.length} rows
            </p>
          )}
        </div>
      </div>
    )
  }

  // Prepare data for bar chart
  const chartData = data.data.slice(0, 20).map(row => ({
    [xKey]: String(row[xKey] || 'Unknown'),
    [yKey]: Number(row[yKey]) || 0
  }))

  return (
    <div className="chart-container p-6 border border-gray-200 rounded-lg">
      <div className="chart-header mb-4">
        <h3 className="text-lg font-semibold text-gray-900">Chart Visualization</h3>
        <p className="text-sm text-gray-600">
          {data.row_count} rows • SQL: {data.sql}
        </p>
      </div>
      
      <div className="chart-content h-96">
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={chartData} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis 
              dataKey={xKey} 
              tick={{ fontSize: 12 }}
              angle={-45}
              textAnchor="end"
              height={60}
            />
            <YAxis tick={{ fontSize: 12 }} />
            <Tooltip />
            <Legend />
            <Bar dataKey={yKey} fill="#3B82F6" />
          </BarChart>
        </ResponsiveContainer>
      </div>
      
      <div className="chart-footer mt-4 text-xs text-gray-500">
        Showing first 20 records for performance
      </div>
    </div>
  )
}