import { NextRequest, NextResponse } from 'next/server';

interface RouteParams {
  params: {
    id: string;
  };
}

// Mock projects storage
const projects = new Map();

export async function DELETE(request: NextRequest, { params }: RouteParams) {
  try {
    const { id } = params;
    
    if (!projects.has(id)) {
      return NextResponse.json(
        { error: 'Project not found' },
        { status: 404 }
      );
    }

    projects.delete(id);
    return NextResponse.json({ status: 'deleted' });
  } catch (error) {
    return NextResponse.json(
      { error: `Failed to delete project: ${error instanceof Error ? error.message : String(error)}` },
      { status: 500 }
    );
  }
}