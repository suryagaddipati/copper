'use client';

import { useState, useEffect } from 'react';
import { QueryBuilder } from '@/components/QueryBuilder';
import { DataVisualization } from '@/components/DataVisualization';
import { Sidebar } from '@/components/Sidebar';
import { ProjectPanel } from '@/components/ProjectPanel';
import { getAvailableModels, ExampleModel } from '@/lib/example-models';

export default function Home() {
  const [selectedDimensions, setSelectedDimensions] = useState<string[]>([]);
  const [selectedMeasures, setSelectedMeasures] = useState<string[]>([]);
  const [queryResult, setQueryResult] = useState<Record<string, string | number>[]>([]);
  const [currentModel, setCurrentModel] = useState<ExampleModel | null>(null);
  const [availableModels, setAvailableModels] = useState<ExampleModel[]>([]);
  const [showProjectPanel, setShowProjectPanel] = useState(true);
  const [isLoading, setIsLoading] = useState(true);
  
  // Load available models on component mount (no default model)
  useEffect(() => {
    const loadModels = async () => {
      try {
        const allModels = await getAvailableModels();
        setAvailableModels(allModels);
      } catch (error) {
        console.error('Failed to load models:', error);
      } finally {
        setIsLoading(false);
      }
    };
    
    loadModels();
  }, []);
  
  const handleProjectChange = (project: ExampleModel) => {
    setCurrentModel(project);
    setSelectedDimensions([]);
    setSelectedMeasures([]);
    setQueryResult([]);
  };

  const handleProjectLoaded = (project: ExampleModel) => {
    // Add the newly loaded project to the available models list
    setAvailableModels(prev => {
      // Check if project already exists
      const existingIndex = prev.findIndex(p => p.id === project.id);
      if (existingIndex >= 0) {
        // Replace existing project
        const updated = [...prev];
        updated[existingIndex] = project;
        return updated;
      } else {
        // Add new project
        return [...prev, project];
      }
    });
  };
  
  // Show loading state while models are being loaded
  if (isLoading) {
    return (
      <div className="flex h-screen items-center justify-center bg-gray-50">
        <div className="text-center">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600 mx-auto mb-4"></div>
          <p className="text-gray-600">Loading Copper Studio...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="flex h-screen bg-gray-50">
      {/* Project Panel */}
      {showProjectPanel && (
        <ProjectPanel
          availableProjects={availableModels}
          currentProject={currentModel}
          onProjectChange={handleProjectChange}
          onProjectLoaded={handleProjectLoaded}
          isLoading={isLoading}
        />
      )}
      
      {/* Sidebar */}
      <Sidebar 
        selectedDimensions={selectedDimensions}
        selectedMeasures={selectedMeasures}
        onDimensionChange={setSelectedDimensions}
        onMeasureChange={setSelectedMeasures}
        model={currentModel}
      />
      
      {/* Main Content */}
      <div className="flex-1 flex flex-col">
        {/* Header */}
        <header className="bg-white border-b border-gray-200 px-6 py-4">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-2xl font-bold text-gray-900">Copper Studio</h1>
              <p className="text-sm text-gray-600">The Universal Semantic Layer</p>
            </div>
            <div className="flex items-center space-x-4">
              <button
                onClick={() => setShowProjectPanel(!showProjectPanel)}
                className="px-3 py-2 text-sm border border-gray-300 rounded-md hover:bg-gray-50"
              >
                {showProjectPanel ? 'Hide Projects' : 'Show Projects'}
              </button>
              {currentModel && (
                <div className="text-sm text-gray-600">
                  Project: <span className="font-medium">{currentModel.name}</span>
                </div>
              )}
            </div>
          </div>
        </header>

        {/* Query Builder and Visualization */}
        {currentModel ? (
          <>
            <QueryBuilder 
              dimensions={selectedDimensions}
              measures={selectedMeasures}
              onResultChange={setQueryResult}
              model={currentModel}
            />

            {/* Visualization Area */}
            <div className="flex-1 p-6">
              <DataVisualization 
                data={queryResult}
                dimensions={selectedDimensions}
                measures={selectedMeasures}
              />
            </div>
          </>
        ) : (
          <div className="flex-1 flex items-center justify-center">
            <div className="text-center">
              <div className="text-gray-400 mb-6">
                <svg className="w-24 h-24 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2-2V7a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 002 2h6a2 2 0 002-2V7a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 00-2 2h-2a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2v-2a2 2 0 00-2-2h-2a2 2 0 00-2-2V9a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2z" />
                </svg>
              </div>
              <h2 className="text-2xl font-bold text-gray-900 mb-4">Welcome to Copper Studio</h2>
              <p className="text-lg text-gray-600 mb-6">Select a project to start exploring your data</p>
              <div className="max-w-md mx-auto text-sm text-gray-500">
                <p>Projects contain semantic models with dimensions and measures that you can use to build queries and visualizations.</p>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}