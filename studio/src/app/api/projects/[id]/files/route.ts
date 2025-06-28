import { NextRequest, NextResponse } from 'next/server';
import * as fs from 'fs';
import * as path from 'path';

interface RouteParams {
  params: {
    id: string;
  };
}

interface CopperFile {
  name: string;
  path: string;
  content: string;
  relative_path: string;
}

export async function GET(request: NextRequest, { params }: RouteParams) {
  try {
    const { id } = params;
    
    // Map project IDs to actual directories
    const projectPaths: Record<string, string> = {
      'ufc-analytics': '/home/surya/code/copper/example-projects/ufc-analytics',
      'ecommerce-demo': '/home/surya/code/copper/example-projects/ecommerce-demo', 
      'basic-tutorial': '/home/surya/code/copper/example-projects/basic-tutorial'
    };
    
    const projectPath = projectPaths[id];
    if (!projectPath) {
      return NextResponse.json(
        { error: `Project ${id} not found` },
        { status: 404 }
      );
    }
    
    // Load all .copper files from the project directory
    const files: CopperFile[] = [];
    
    if (fs.existsSync(projectPath)) {
      const entries = fs.readdirSync(projectPath);
      
      for (const entry of entries) {
        if (entry.endsWith('.copper')) {
          const filePath = path.join(projectPath, entry);
          const content = fs.readFileSync(filePath, 'utf-8');
          
          files.push({
            name: entry,
            path: filePath,
            content: content,
            relative_path: entry
          });
        }
      }
    }

    return NextResponse.json(files);
  } catch (error) {
    return NextResponse.json(
      { error: `Failed to get project files: ${error instanceof Error ? error.message : String(error)}` },
      { status: 500 }
    );
  }
}