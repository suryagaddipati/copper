'use client';

import { useEffect, useState, useCallback } from 'react';
import { Play, Download, Code, Eye } from 'lucide-react';
import clsx from 'clsx';
import { ExampleModel } from '../lib/example-models';

interface QueryBuilderProps {
  dimensions: string[];
  measures: string[];
  onResultChange: (data: Record<string, string | number>[]) => void;
  model: ExampleModel;
}

export function QueryBuilder({ dimensions, measures, onResultChange, model }: QueryBuilderProps) {
  const [isLoading, setIsLoading] = useState(false);
  const [showSQL, setShowSQL] = useState(false);
  const [generatedSQL, setGeneratedSQL] = useState('');
  
  // Generate real SQL from semantic model
  const generateSQL = useCallback((dims: string[], meas: string[]) => {
    if (dims.length === 0 && meas.length === 0) {
      return '-- No fields selected';
    }
    
    // Get the semantic model to build proper SQL
    const semanticModel = model.processor.getModel();
    const querySpec = {
      dimensions: dims,
      measures: meas,
      filters: [],
      orderBy: {},
      limit: 1000,
    };
    
    try {
      const sql = model.processor.toSQL(querySpec);
      return sql;
    } catch (error) {
      console.error('Failed to generate SQL:', error);
      return `-- Error generating SQL: ${error instanceof Error ? error.message : 'Unknown error'}`;
    }
  }, [model]);

  const executeQuery = useCallback(async () => {
    if (dimensions.length === 0 && measures.length === 0) {
      onResultChange([]);
      return;
    }

    setIsLoading(true);
    
    try {
      // Query using the model's data processor
      const queryResult = await model.processor.queryData(dimensions, measures);
      const queryResults = queryResult.data;
      
      // Generate SQL using the simple generator
      const sql = generateSQL(dimensions, measures);
      setGeneratedSQL(sql);
      
      // Simulate loading delay for realistic UX
      await new Promise(resolve => setTimeout(resolve, 500));
      
      onResultChange(queryResults);
    } catch (error) {
      console.error('Query execution failed:', error);
      onResultChange([]);
    } finally {
      setIsLoading(false);
    }
  }, [dimensions, measures, onResultChange, model, generateSQL]);

  // Auto-execute when fields change
  useEffect(() => {
    executeQuery();
  }, [executeQuery]);


  const getDatasetStats = () => {
    const semanticModel = model.processor.getModel();
    const dimensionCount = Object.keys(semanticModel.dimensions || {}).length;
    const measureCount = Object.keys(semanticModel.measures || {}).length;
    const datasourceCount = Object.keys(semanticModel.datasources || {}).length;
    
    return `${datasourceCount} datasources, ${dimensionCount} dimensions, ${measureCount} measures`;
  };

  const downloadCSV = () => {
    // Would implement CSV download functionality
    console.log('Download CSV functionality would be implemented here');
  };

  return (
    <div className="bg-white border-b border-gray-200">
      {/* Query Controls */}
      <div className="px-6 py-4 flex items-center justify-between">
        <div className="flex items-center space-x-4">
          <button
            onClick={executeQuery}
            disabled={isLoading || (dimensions.length === 0 && measures.length === 0)}
            className={clsx(
              'flex items-center px-4 py-2 rounded-lg font-medium',
              isLoading || (dimensions.length === 0 && measures.length === 0)
                ? 'bg-gray-100 text-gray-400 cursor-not-allowed'
                : 'bg-blue-600 text-white hover:bg-blue-700'
            )}
          >
            <Play className="w-4 h-4 mr-2" />
            {isLoading ? 'Running...' : 'Run Query'}
          </button>

          <div className="text-sm text-gray-600">
            {(dimensions.length > 0 || measures.length > 0) ? (
              <>
                {dimensions.length} dimension{dimensions.length !== 1 ? 's' : ''}, {measures.length} measure{measures.length !== 1 ? 's' : ''} • 
                Dataset: {getDatasetStats()}
              </>
            ) : (
              <>Dataset: {getDatasetStats()}</>
            )}
          </div>
        </div>

        <div className="flex items-center space-x-2">
          <button
            onClick={() => setShowSQL(!showSQL)}
            className="flex items-center px-3 py-2 text-sm text-gray-600 hover:text-gray-900 hover:bg-gray-100 rounded"
          >
            {showSQL ? <Eye className="w-4 h-4 mr-1" /> : <Code className="w-4 h-4 mr-1" />}
            {showSQL ? 'Hide SQL' : 'Show SQL'}
          </button>
          
          <button
            onClick={downloadCSV}
            className="flex items-center px-3 py-2 text-sm text-gray-600 hover:text-gray-900 hover:bg-gray-100 rounded"
          >
            <Download className="w-4 h-4 mr-1" />
            Download
          </button>
        </div>
      </div>

      {/* SQL Display */}
      {showSQL && generatedSQL && (
        <div className="px-6 pb-4">
          <div className="bg-gray-900 text-gray-100 p-4 rounded-lg font-mono text-sm overflow-x-auto">
            <pre>{generatedSQL}</pre>
          </div>
        </div>
      )}
    </div>
  );
}