import { NextResponse } from 'next/server';

export async function GET() {
  return NextResponse.json({ 
    status: 'healthy', 
    service: 'copper-studio-api',
    timestamp: new Date().toISOString()
  });
}