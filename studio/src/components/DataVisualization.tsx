'use client';

import { useState, useMemo } from 'react';
import { BarChart, Bar, LineChart, Line, PieChart, Pie, Cell, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { BarChart3, LineChart as LineChartIcon, PieChart as PieChartIcon, Table, ChevronUp, ChevronDown } from 'lucide-react';
import clsx from 'clsx';

interface DataVisualizationProps {
  data: Record<string, string | number>[];
  dimensions: string[];
  measures: string[];
}

type ChartType = 'table' | 'bar' | 'line' | 'pie';

const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042', '#8884D8', '#82CA9D'];

export function DataVisualization({ data, dimensions, measures }: DataVisualizationProps) {
  const [chartType, setChartType] = useState<ChartType>('table');
  const [sortColumn, setSortColumn] = useState<string | null>(null);
  const [sortDirection, setSortDirection] = useState<'asc' | 'desc'>('asc');

  // Handle column sorting
  const handleSort = (column: string) => {
    if (sortColumn === column) {
      setSortDirection(sortDirection === 'asc' ? 'desc' : 'asc');
    } else {
      setSortColumn(column);
      setSortDirection('asc');
    }
  };

  // Sort data based on current sort settings
  const sortedData = useMemo(() => {
    if (!sortColumn) return data;

    return [...data].sort((a, b) => {
      const aVal = a[sortColumn];
      const bVal = b[sortColumn];

      // Handle different data types
      if (typeof aVal === 'number' && typeof bVal === 'number') {
        return sortDirection === 'asc' ? aVal - bVal : bVal - aVal;
      }

      const aStr = String(aVal).toLowerCase();
      const bStr = String(bVal).toLowerCase();
      
      if (sortDirection === 'asc') {
        return aStr.localeCompare(bStr);
      } else {
        return bStr.localeCompare(aStr);
      }
    });
  }, [data, sortColumn, sortDirection]);

  if (data.length === 0) {
    return (
      <div className="bg-white rounded-lg border border-gray-200 h-full flex items-center justify-center">
        <div className="text-center">
          <BarChart3 className="w-16 h-16 text-gray-300 mx-auto mb-4" />
          <h3 className="text-lg font-medium text-gray-900 mb-2">No Data</h3>
          <p className="text-gray-600">Select dimensions and measures to visualize your data</p>
        </div>
      </div>
    );
  }

  const chartOptions = [
    { type: 'table' as ChartType, icon: Table, label: 'Table' },
    { type: 'bar' as ChartType, icon: BarChart3, label: 'Bar Chart' },
    { type: 'line' as ChartType, icon: LineChartIcon, label: 'Line Chart' },
    { type: 'pie' as ChartType, icon: PieChartIcon, label: 'Pie Chart' },
  ];

  const renderChart = () => {
    const xAxisKey = dimensions[0];
    const yAxisKey = measures[0];

    switch (chartType) {
      case 'bar':
        return (
          <ResponsiveContainer width="100%" height={400}>
            <BarChart data={data}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey={xAxisKey} />
              <YAxis />
              <Tooltip />
              <Legend />
              {measures.map((measure, index) => (
                <Bar key={measure} dataKey={measure} fill={COLORS[index % COLORS.length]} />
              ))}
            </BarChart>
          </ResponsiveContainer>
        );

      case 'line':
        return (
          <ResponsiveContainer width="100%" height={400}>
            <LineChart data={data}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey={xAxisKey} />
              <YAxis />
              <Tooltip />
              <Legend />
              {measures.map((measure, index) => (
                <Line 
                  key={measure} 
                  type="monotone" 
                  dataKey={measure} 
                  stroke={COLORS[index % COLORS.length]}
                  strokeWidth={2}
                />
              ))}
            </LineChart>
          </ResponsiveContainer>
        );

      case 'pie':
        const pieData = data.map((item, index) => ({
          name: item[xAxisKey],
          value: item[yAxisKey],
          fill: COLORS[index % COLORS.length]
        }));

        return (
          <ResponsiveContainer width="100%" height={400}>
            <PieChart>
              <Pie
                data={pieData}
                cx="50%"
                cy="50%"
                labelLine={false}
                label={({ name, percent }) => `${name} ${((percent || 0) * 100).toFixed(0)}%`}
                outerRadius={120}
                fill="#8884d8"
                dataKey="value"
              >
                {pieData.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={entry.fill} />
                ))}
              </Pie>
              <Tooltip />
            </PieChart>
          </ResponsiveContainer>
        );

      case 'table':
      default:
        const allColumns = [...dimensions, ...measures];
        
        return (
          <div className="overflow-x-auto">
            <table className="min-w-full divide-y divide-gray-200">
              <thead className="bg-gray-50">
                <tr>
                  {allColumns.map((column) => (
                    <th
                      key={column}
                      className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer hover:bg-gray-100 select-none"
                      onClick={() => handleSort(column)}
                    >
                      <div className="flex items-center space-x-1">
                        <span>{column.replace(/_/g, ' ')}</span>
                        <div className="flex flex-col">
                          <ChevronUp 
                            className={clsx(
                              'w-3 h-3',
                              sortColumn === column && sortDirection === 'asc' 
                                ? 'text-blue-600' 
                                : 'text-gray-300'
                            )}
                          />
                          <ChevronDown 
                            className={clsx(
                              'w-3 h-3 -mt-1',
                              sortColumn === column && sortDirection === 'desc' 
                                ? 'text-blue-600' 
                                : 'text-gray-300'
                            )}
                          />
                        </div>
                      </div>
                    </th>
                  ))}
                </tr>
              </thead>
              <tbody className="bg-white divide-y divide-gray-200">
                {sortedData.map((row, index) => (
                  <tr key={index} className={index % 2 === 0 ? 'bg-white' : 'bg-gray-50'}>
                    {allColumns.map((column) => (
                      <td key={column} className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                        {typeof row[column] === 'number' 
                          ? row[column].toLocaleString() 
                          : row[column]
                        }
                      </td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        );
    }
  };

  return (
    <div className="bg-white rounded-lg border border-gray-200 h-full flex flex-col">
      {/* Visualization Controls */}
      <div className="flex items-center justify-between p-4 border-b border-gray-200">
        <h3 className="text-lg font-medium text-gray-900">
          Results ({data.length} rows)
        </h3>
        
        <div className="flex items-center space-x-1">
          {chartOptions.map((option) => {
            const Icon = option.icon;
            return (
              <button
                key={option.type}
                onClick={() => setChartType(option.type)}
                className={clsx(
                  'flex items-center px-3 py-2 text-sm rounded-lg',
                  chartType === option.type
                    ? 'bg-blue-100 text-blue-700'
                    : 'text-gray-600 hover:text-gray-900 hover:bg-gray-100'
                )}
              >
                <Icon className="w-4 h-4 mr-1" />
                {option.label}
              </button>
            );
          })}
        </div>
      </div>

      {/* Chart Content */}
      <div className="flex-1 p-4">
        {renderChart()}
      </div>
    </div>
  );
}