import { NextRequest, NextResponse } from 'next/server';
import { readFile } from 'fs/promises';
import { join } from 'path';

interface RouteParams {
  params: {
    name: string;
  };
}

export async function GET(request: NextRequest, { params }: RouteParams) {
  try {
    const { name } = params;
    const examplesDir = join(process.cwd(), '..', 'example-projects');
    
    // Convert display name back to filename
    const fileName = name.toLowerCase().replace(/ /g, '_') + '.copper';
    
    // Try to find the file in any subdirectory
    const { readdir } = await import('fs/promises');
    
    const findFile = async (dir: string, targetFile: string): Promise<string | null> => {
      try {
        const entries = await readdir(dir, { withFileTypes: true });
        
        for (const entry of entries) {
          const fullPath = join(dir, entry.name);
          if (entry.isDirectory()) {
            const found = await findFile(fullPath, targetFile);
            if (found) return found;
          } else if (entry.name === targetFile) {
            return fullPath;
          }
        }
      } catch {
        // Ignore errors when traversing directories
      }
      return null;
    };

    const filePath = await findFile(examplesDir, fileName);
    
    if (!filePath) {
      return NextResponse.json(
        { error: `Example '${name}' not found` },
        { status: 404 }
      );
    }

    const content = await readFile(filePath, 'utf-8');
    
    // Extract description
    let description = `Example Copper file: ${name}`;
    const lines = content.split('\n');
    for (const line of lines.slice(0, 5)) {
      if (line.trim().startsWith('#') && line.trim().length > 2) {
        description = line.trim().substring(1).trim();
        break;
      }
    }

    return NextResponse.json({
      name,
      content,
      description
    });

  } catch (error) {
    return NextResponse.json(
      { error: `Error reading example: ${error instanceof Error ? error.message : String(error)}` },
      { status: 500 }
    );
  }
}