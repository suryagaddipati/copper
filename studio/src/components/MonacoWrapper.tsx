'use client';

import { useEffect, useState } from 'react';
import dynamic from 'next/dynamic';

// Dynamically import Monaco Editor with no SSR
const MonacoEditor = dynamic(
  () => import('@monaco-editor/react').then((mod) => mod.default),
  { 
    ssr: false,
    loading: () => (
      <div className="flex items-center justify-center h-full bg-gray-50 dark:bg-gray-900">
        <div className="text-gray-500 dark:text-gray-400">Loading editor...</div>
      </div>
    )
  }
);

interface MonacoWrapperProps {
  value: string;
  onChange: (value: string | undefined) => void;
  language?: string;
  theme?: string;
  options?: any;
  height?: string | number;
  beforeMount?: (monaco: any) => void;
  onMount?: (editor: any, monaco: any) => void;
}

export function MonacoWrapper({
  value,
  onChange,
  language = 'copper',
  theme = 'vs-dark',
  options = {},
  height = '100%',
  beforeMount,
  onMount
}: MonacoWrapperProps) {
  const [isClient, setIsClient] = useState(false);

  useEffect(() => {
    setIsClient(true);
  }, []);

  if (!isClient) {
    return (
      <div className="flex items-center justify-center h-full bg-gray-50 dark:bg-gray-900">
        <div className="text-gray-500 dark:text-gray-400">Loading editor...</div>
      </div>
    );
  }

  return (
    <MonacoEditor
      value={value}
      onChange={onChange}
      language={language}
      theme={theme}
      height={height}
      beforeMount={beforeMount}
      onMount={onMount}
      options={{
        minimap: { enabled: false },
        fontSize: 14,
        lineNumbers: 'on',
        wordWrap: 'on',
        automaticLayout: true,
        scrollBeyondLastLine: false,
        ...options
      }}
    />
  );
}