import { NextResponse } from 'next/server';
import { readdir, readFile } from 'fs/promises';
import { join } from 'path';

interface ExampleFile {
  name: string;
  content: string;
  description: string;
}

export async function GET() {
  try {
    const examples: ExampleFile[] = [];
    const examplesDir = join(process.cwd(), '..', 'example-projects');
    
    try {
      // Get all .copper files recursively
      const findCopperFiles = async (dir: string): Promise<string[]> => {
        const files: string[] = [];
        const entries = await readdir(dir, { withFileTypes: true });
        
        for (const entry of entries) {
          const fullPath = join(dir, entry.name);
          if (entry.isDirectory()) {
            files.push(...await findCopperFiles(fullPath));
          } else if (entry.name.endsWith('.copper')) {
            files.push(fullPath);
          }
        }
        return files;
      };

      const copperFiles = await findCopperFiles(examplesDir);
      
      for (const filePath of copperFiles) {
        try {
          const content = await readFile(filePath, 'utf-8');
          const fileName = filePath.split('/').pop() || '';
          const name = fileName.replace('.copper', '').replace('_', ' ').replace(/\b\w/g, l => l.toUpperCase());
          
          // Extract description from first comment if available
          let description = `Example Copper file: ${name}`;
          const lines = content.split('\n');
          for (const line of lines.slice(0, 5)) { // Check first 5 lines for description
            if (line.trim().startsWith('#') && line.trim().length > 2) {
              description = line.trim().substring(1).trim();
              break;
            }
          }
          
          examples.push({
            name,
            content,
            description
          });
        } catch (fileError) {
          // Skip files that can't be read
          continue;
        }
      }
    } catch (dirError) {
      // If examples directory doesn't exist, return empty array
      return NextResponse.json([]);
    }
    
    return NextResponse.json(examples);
    
  } catch (error) {
    return NextResponse.json(
      { error: `Failed to load examples: ${error instanceof Error ? error.message : String(error)}` },
      { status: 500 }
    );
  }
}