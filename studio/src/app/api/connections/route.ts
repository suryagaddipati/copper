import { NextRequest, NextResponse } from 'next/server';

// Mock connection data for now - TODO: Implement proper database connection logic
interface Connection {
  id: string;
  name: string;
  type: string;
  is_active: boolean;
}

// In-memory storage for demo purposes
let connections: Connection[] = [
  {
    id: "demo-sqlite",
    name: "Demo SQLite",
    type: "sqlite",
    is_active: false
  }
];

export async function GET() {
  try {
    return NextResponse.json(connections);
  } catch (error) {
    return NextResponse.json(
      { error: `Failed to fetch connections: ${error instanceof Error ? error.message : String(error)}` },
      { status: 500 }
    );
  }
}

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { name, type, host, port, database, username, password, file_path } = body;

    if (!name || !type) {
      return NextResponse.json(
        { error: 'Name and type are required' },
        { status: 400 }
      );
    }

    const newConnection: Connection = {
      id: `conn-${Date.now()}`,
      name,
      type: type.toLowerCase(),
      is_active: false
    };

    connections.push(newConnection);

    return NextResponse.json(newConnection, { status: 201 });
  } catch (error) {
    return NextResponse.json(
      { error: `Failed to create connection: ${error instanceof Error ? error.message : String(error)}` },
      { status: 500 }
    );
  }
}