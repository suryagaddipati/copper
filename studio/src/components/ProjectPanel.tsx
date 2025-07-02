'use client';

import { useState } from 'react';
import { ChevronRight, ChevronDown, Folder, Database, BarChart3, Settings, FolderOpen, Plus } from 'lucide-react';
import clsx from 'clsx';
import { ExampleModel, loadProjectFromDirectory } from '../lib/example-models';

interface ProjectPanelProps {
  availableProjects: ExampleModel[];
  currentProject: ExampleModel | null;
  onProjectChange: (project: ExampleModel) => void;
  onProjectLoaded?: (project: ExampleModel) => void;
  isLoading?: boolean;
}

export function ProjectPanel({ availableProjects, currentProject, onProjectChange, onProjectLoaded, isLoading }: ProjectPanelProps) {
  const [isExpanded, setIsExpanded] = useState(true);
  const [showLoadForm, setShowLoadForm] = useState(false);
  const [directoryPath, setDirectoryPath] = useState('');
  const [isLoadingProject, setIsLoadingProject] = useState(false);
  const [loadError, setLoadError] = useState<string | null>(null);

  const handleLoadProject = async () => {
    if (!directoryPath.trim()) {
      setLoadError('Please enter a directory path');
      return;
    }

    setIsLoadingProject(true);
    setLoadError(null);

    try {
      const project = await loadProjectFromDirectory(directoryPath.trim());
      onProjectLoaded?.(project);
      onProjectChange(project);
      setShowLoadForm(false);
      setDirectoryPath('');
    } catch (error) {
      setLoadError(`Failed to load project: ${error instanceof Error ? error.message : 'Unknown error'}`);
    } finally {
      setIsLoadingProject(false);
    }
  };

  if (isLoading) {
    return (
      <div className="w-80 bg-white border-r border-gray-200 flex flex-col">
        <div className="p-4 border-b border-gray-200">
          <h2 className="text-lg font-semibold text-gray-900">Projects</h2>
        </div>
        <div className="flex-1 flex items-center justify-center">
          <div className="animate-spin rounded-full h-6 w-6 border-b-2 border-blue-600"></div>
        </div>
      </div>
    );
  }

  return (
    <div className="w-80 bg-white border-r border-gray-200 flex flex-col">
      {/* Panel Header */}
      <div className="p-4 border-b border-gray-200">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-lg font-semibold text-gray-900">Projects</h2>
            <p className="text-sm text-gray-600">Select a project to explore</p>
          </div>
          <button
            onClick={() => setShowLoadForm(!showLoadForm)}
            className="p-2 text-gray-400 hover:text-gray-600 hover:bg-gray-100 rounded-md transition-colors"
            title="Load project from directory"
          >
            <Plus className="w-5 h-5" />
          </button>
        </div>
      </div>

      {/* Load Project Form */}
      {showLoadForm && (
        <div className="p-4 border-b border-gray-200 bg-gray-50">
          <h3 className="text-sm font-medium text-gray-900 mb-3">Load Project from Directory</h3>
          <div className="space-y-3">
            <div>
              <input
                type="text"
                value={directoryPath}
                onChange={(e) => setDirectoryPath(e.target.value)}
                placeholder="/example-projects/my-project"
                className="w-full px-3 py-2 text-sm border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                disabled={isLoadingProject}
              />
              <p className="text-xs text-gray-500 mt-1">
                Path to directory containing project.yaml
              </p>
            </div>
            {loadError && (
              <div className="text-xs text-red-600 bg-red-50 p-2 rounded border border-red-200">
                {loadError}
              </div>
            )}
            <div className="flex items-center space-x-2">
              <button
                onClick={handleLoadProject}
                disabled={isLoadingProject || !directoryPath.trim()}
                className={clsx(
                  'flex items-center px-3 py-1.5 text-sm font-medium rounded-md transition-colors',
                  isLoadingProject || !directoryPath.trim()
                    ? 'bg-gray-100 text-gray-400 cursor-not-allowed'
                    : 'bg-blue-600 text-white hover:bg-blue-700'
                )}
              >
                {isLoadingProject ? (
                  <>
                    <div className="animate-spin rounded-full h-3 w-3 border border-gray-300 border-t-gray-600 mr-2"></div>
                    Loading...
                  </>
                ) : (
                  <>
                    <FolderOpen className="w-3 h-3 mr-2" />
                    Load Project
                  </>
                )}
              </button>
              <button
                onClick={() => {
                  setShowLoadForm(false);
                  setDirectoryPath('');
                  setLoadError(null);
                }}
                className="px-3 py-1.5 text-sm text-gray-600 hover:text-gray-800 transition-colors"
                disabled={isLoadingProject}
              >
                Cancel
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Project List */}
      <div className="flex-1 overflow-y-auto">
        <div className="p-4">
          <button
            onClick={() => setIsExpanded(!isExpanded)}
            className="flex items-center w-full text-left mb-3"
          >
            {isExpanded ? (
              <ChevronDown className="w-4 h-4 mr-2" />
            ) : (
              <ChevronRight className="w-4 h-4 mr-2" />
            )}
            <span className="font-medium text-gray-900">Available Projects</span>
            <span className="ml-auto text-xs text-gray-500">
              {availableProjects.length}
            </span>
          </button>

          {isExpanded && (
            <div className="space-y-2">
              {availableProjects.length === 0 ? (
                <div className="text-center py-8 text-gray-500">
                  <FolderOpen className="w-12 h-12 mx-auto mb-3 text-gray-300" />
                  <p className="text-sm">No projects loaded</p>
                  <p className="text-xs mt-1">Use the + button above to load a project</p>
                </div>
              ) : (
                availableProjects.map((project) => {
                const isSelected = currentProject?.id === project.id;
                
                return (
                  <div
                    key={project.id}
                    className={clsx(
                      'rounded-lg border p-3 cursor-pointer transition-colors',
                      isSelected 
                        ? 'border-blue-500 bg-blue-50' 
                        : 'border-gray-200 hover:border-gray-300 hover:bg-gray-50'
                    )}
                    onClick={() => onProjectChange(project)}
                  >
                    <div className="flex items-start">
                      <Folder className={clsx(
                        'w-5 h-5 mr-3 mt-0.5',
                        isSelected ? 'text-blue-600' : 'text-gray-400'
                      )} />
                      <div className="flex-1 min-w-0">
                        <h3 className={clsx(
                          'font-medium text-sm',
                          isSelected ? 'text-blue-900' : 'text-gray-900'
                        )}>
                          {project.name}
                        </h3>
                        <p className={clsx(
                          'text-xs mt-1 line-clamp-2',
                          isSelected ? 'text-blue-700' : 'text-gray-600'
                        )}>
                          {project.description}
                        </p>
                        <div className="flex items-center mt-2 space-x-3">
                          <span className={clsx(
                            'inline-flex items-center px-2 py-0.5 rounded text-xs font-medium',
                            isSelected 
                              ? 'bg-blue-100 text-blue-800' 
                              : 'bg-gray-100 text-gray-800'
                          )}>
                            {project.domain}
                          </span>
                        </div>
                      </div>
                    </div>
                  </div>
                );
                })
              )}
            </div>
          )}
        </div>

        {/* Current Project Details */}
        {currentProject && (
          <div className="border-t border-gray-200 p-4">
            <h3 className="font-medium text-gray-900 mb-3">Project Details</h3>
            <div className="space-y-3">
              <div className="flex items-center text-sm">
                <Database className="w-4 h-4 mr-2 text-gray-400" />
                <span className="text-gray-600">
                  {Object.keys(currentProject.model.datasources || {}).length} datasources
                </span>
              </div>
              <div className="flex items-center text-sm">
                <BarChart3 className="w-4 h-4 mr-2 text-gray-400" />
                <span className="text-gray-600">
                  {Object.keys(currentProject.model.dimensions || {}).length} dimensions, {' '}
                  {Object.keys(currentProject.model.measures || {}).length} measures
                </span>
              </div>
              <div className="flex items-center text-sm">
                <Settings className="w-4 h-4 mr-2 text-gray-400" />
                <span className="text-gray-600">
                  Path: {currentProject.path}
                </span>
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Panel Footer */}
      <div className="border-t border-gray-200 p-4">
        <div className="text-xs text-gray-500">
          {currentProject ? (
            <>
              Active: <span className="font-medium">{currentProject.name}</span>
            </>
          ) : (
            'No project selected'
          )}
        </div>
      </div>
    </div>
  );
}