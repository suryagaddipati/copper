import { NextRequest, NextResponse } from 'next/server';

interface RouteParams {
  params: {
    id: string;
  };
}

// Mock connection data - this should be replaced with proper database logic
const connections = new Map([
  ["demo-sqlite", {
    id: "demo-sqlite",
    name: "Demo SQLite",
    type: "sqlite",
    is_active: false
  }]
]);

export async function GET(request: NextRequest, { params }: RouteParams) {
  try {
    const { id } = params;
    const connection = connections.get(id);
    
    if (!connection) {
      return NextResponse.json(
        { error: 'Connection not found' },
        { status: 404 }
      );
    }

    return NextResponse.json(connection);
  } catch (error) {
    return NextResponse.json(
      { error: `Failed to get connection: ${error instanceof Error ? error.message : String(error)}` },
      { status: 500 }
    );
  }
}

export async function DELETE(request: NextRequest, { params }: RouteParams) {
  try {
    const { id } = params;
    
    if (!connections.has(id)) {
      return NextResponse.json(
        { error: 'Connection not found' },
        { status: 404 }
      );
    }

    connections.delete(id);
    return NextResponse.json({ message: 'Connection deleted' });
  } catch (error) {
    return NextResponse.json(
      { error: `Failed to delete connection: ${error instanceof Error ? error.message : String(error)}` },
      { status: 500 }
    );
  }
}