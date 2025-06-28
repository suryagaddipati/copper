import { NextRequest, NextResponse } from 'next/server';

// Mock project data for now - TODO: Implement proper project management
interface Project {
  id: string;
  name: string;
  path: string;
  file_count: number;
  created_at: string;
}

// In-memory storage for demo purposes
let projects: Project[] = [
  {
    id: 'ufc-analytics',
    name: 'UFC Analytics',
    path: '/home/surya/code/copper/example-projects/ufc-analytics',
    file_count: 4,
    created_at: new Date().toISOString()
  },
  {
    id: 'ecommerce-demo',
    name: 'E-commerce Demo', 
    path: '/home/surya/code/copper/example-projects/ecommerce-demo',
    file_count: 4,
    created_at: new Date().toISOString()
  },
  {
    id: 'basic-tutorial',
    name: 'Basic Tutorial',
    path: '/home/surya/code/copper/example-projects/basic-tutorial', 
    file_count: 2,
    created_at: new Date().toISOString()
  }
];

export async function GET() {
  try {
    return NextResponse.json(projects);
  } catch (error) {
    return NextResponse.json(
      { error: `Failed to fetch projects: ${error instanceof Error ? error.message : String(error)}` },
      { status: 500 }
    );
  }
}

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { path, name } = body;

    if (!path) {
      return NextResponse.json(
        { error: 'Path is required' },
        { status: 400 }
      );
    }

    const newProject: Project = {
      id: `proj-${Date.now()}`,
      name: name || `Project ${projects.length + 1}`,
      path,
      file_count: 0, // TODO: Count actual files
      created_at: new Date().toISOString()
    };

    projects.push(newProject);

    return NextResponse.json(newProject, { status: 201 });
  } catch (error) {
    return NextResponse.json(
      { error: `Failed to create project: ${error instanceof Error ? error.message : String(error)}` },
      { status: 500 }
    );
  }
}