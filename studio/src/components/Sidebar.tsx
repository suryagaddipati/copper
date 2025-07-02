'use client';

import { useState } from 'react';
import { ChevronDown, ChevronRight, BarChart3, Hash, Calendar, Tag, MapPin } from 'lucide-react';
import clsx from 'clsx';
// Remove unused imports - types are accessed through ExampleModel
import { ExampleModel } from '../lib/example-models';

interface SidebarProps {
  selectedDimensions: string[];
  selectedMeasures: string[];
  onDimensionChange: (dimensions: string[]) => void;
  onMeasureChange: (measures: string[]) => void;
  model: ExampleModel | null;
}

// Icon mapping for dynamic icon resolution
const ICON_MAP = {
  Tag,
  Hash,
  Calendar,
  BarChart3,
  MapPin
};

export function Sidebar({ selectedDimensions, selectedMeasures, onDimensionChange, onMeasureChange, model }: SidebarProps) {
  const [dimensionsExpanded, setDimensionsExpanded] = useState(true);
  const [measuresExpanded, setMeasuresExpanded] = useState(true);
  
  // Handle null model case
  if (!model) {
    return (
      <div className="w-80 bg-white border-r border-gray-200 flex flex-col items-center justify-center">
        <div className="text-center p-8">
          <div className="text-gray-400 mb-4">
            <svg className="w-16 h-16 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1} d="M9 17V7m0 10a2 2 0 01-2 2H5a2 2 0 01-2-2V7a2 2 0 012-2h2a2 2 0 012 2m0 10a2 2 0 002 2h2a2 2 0 002-2M9 7a2 2 0 012-2h2a2 2 0 012 2m0 10V7m0 10a2 2 0 002 2h2a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2h2a2 2 0 002-2z" />
            </svg>
          </div>
          <h3 className="text-lg font-medium text-gray-900 mb-2">No Project Selected</h3>
          <p className="text-sm text-gray-600">Select a project from the panel to explore dimensions and measures.</p>
        </div>
      </div>
    );
  }
  
  // Get dimensions and measures from the semantic model
  const dimensions = model.processor.getDimensions();
  const measures = model.processor.getMeasures();

  const toggleDimension = (dimensionId: string) => {
    const newDimensions = selectedDimensions.includes(dimensionId)
      ? selectedDimensions.filter(d => d !== dimensionId)
      : [...selectedDimensions, dimensionId];
    onDimensionChange(newDimensions);
  };

  const toggleMeasure = (measureId: string) => {
    const newMeasures = selectedMeasures.includes(measureId)
      ? selectedMeasures.filter(m => m !== measureId)
      : [...selectedMeasures, measureId];
    onMeasureChange(newMeasures);
  };

  return (
    <div className="w-80 bg-white border-r border-gray-200 flex flex-col">
      {/* Model Info */}
      <div className="p-4 border-b border-gray-200">
        <h2 className="text-lg font-semibold text-gray-900">Data Model</h2>
        <p className="text-sm text-gray-600">Explore dimensions and measures</p>
        {model && (
          <div className="mt-2 text-xs text-gray-500">
            From project: {model.name}
          </div>
        )}
      </div>

      {/* Fields */}
      <div className="flex-1 overflow-y-auto">
        {/* Dimensions */}
        <div className="p-4">
          <button
            onClick={() => setDimensionsExpanded(!dimensionsExpanded)}
            className="flex items-center w-full text-left"
          >
            {dimensionsExpanded ? (
              <ChevronDown className="w-4 h-4 mr-2" />
            ) : (
              <ChevronRight className="w-4 h-4 mr-2" />
            )}
            <span className="font-medium text-gray-900">Dimensions</span>
            <span className="ml-auto text-xs text-gray-500">
              {selectedDimensions.length > 0 && `(${selectedDimensions.length})`}
            </span>
          </button>

          {dimensionsExpanded && (
            <div className="mt-2 space-y-1">
              {dimensions.map((dimension) => {
                const Icon = ICON_MAP[dimension.icon as keyof typeof ICON_MAP] || Tag;
                const isSelected = selectedDimensions.includes(dimension.id);
                
                return (
                  <button
                    key={dimension.id}
                    onClick={() => toggleDimension(dimension.id)}
                    className={clsx(
                      'w-full flex items-center px-2 py-1 text-sm rounded hover:bg-gray-100',
                      isSelected && 'bg-blue-50 text-blue-700'
                    )}
                    title={dimension.description}
                  >
                    <Icon className="w-4 h-4 mr-2 text-gray-400" />
                    <span className="flex-1 text-left">{dimension.label}</span>
                    {isSelected && (
                      <div className="w-2 h-2 bg-blue-500 rounded-full ml-2" />
                    )}
                  </button>
                );
              })}
            </div>
          )}
        </div>

        {/* Measures */}
        <div className="p-4 border-t border-gray-100">
          <button
            onClick={() => setMeasuresExpanded(!measuresExpanded)}
            className="flex items-center w-full text-left"
          >
            {measuresExpanded ? (
              <ChevronDown className="w-4 h-4 mr-2" />
            ) : (
              <ChevronRight className="w-4 h-4 mr-2" />
            )}
            <span className="font-medium text-gray-900">Measures</span>
            <span className="ml-auto text-xs text-gray-500">
              {selectedMeasures.length > 0 && `(${selectedMeasures.length})`}
            </span>
          </button>

          {measuresExpanded && (
            <div className="mt-2 space-y-1">
              {measures.map((measure) => {
                const Icon = ICON_MAP[measure.icon as keyof typeof ICON_MAP] || Hash;
                const isSelected = selectedMeasures.includes(measure.id);
                
                return (
                  <button
                    key={measure.id}
                    onClick={() => toggleMeasure(measure.id)}
                    className={clsx(
                      'w-full flex items-center px-2 py-1 text-sm rounded hover:bg-gray-100',
                      isSelected && 'bg-green-50 text-green-700'
                    )}
                    title={measure.description}
                  >
                    <Icon className="w-4 h-4 mr-2 text-gray-400" />
                    <span className="flex-1 text-left">{measure.label}</span>
                    {isSelected && (
                      <div className="w-2 h-2 bg-green-500 rounded-full ml-2" />
                    )}
                  </button>
                );
              })}
            </div>
          )}
        </div>
      </div>

      {/* Footer */}
      <div className="p-4 border-t border-gray-200">
        <div className="text-xs text-gray-500">
          <div>Dimensions: {selectedDimensions.length}</div>
          <div>Measures: {selectedMeasures.length}</div>
        </div>
      </div>
    </div>
  );
}