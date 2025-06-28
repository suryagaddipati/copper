import { NextResponse } from 'next/server';

export async function GET() {
  return NextResponse.json({
    message: "Copper Studio API",
    version: "2.0.0",
    endpoints: {
      "/api/parse": "Parse Copper content",
      "/api/examples": "Get example Copper files", 
      "/api/health": "Health check"
    }
  });
}