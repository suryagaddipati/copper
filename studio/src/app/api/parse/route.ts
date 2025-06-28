import { NextRequest, NextResponse } from 'next/server';
import { validateCopperSyntax } from '@/lib/parser/simple';

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { content } = body;

    if (!content || typeof content !== 'string') {
      return NextResponse.json(
        { error: 'Content is required and must be a string' },
        { status: 400 }
      );
    }

    const result = validateCopperSyntax(content);
    
    // Convert parsed nodes to serializable format
    const models = result.models.map(model => ({
      name: model.name,
      type: model.type,
      line_number: model.line_number,
      properties: model.properties,
      children: model.children.map(child => ({
        name: child.name,
        type: child.type,
        line_number: child.line_number,
        properties: child.properties
      }))
    }));

    const views = result.views.map(view => ({
      name: view.name,
      type: view.type,
      line_number: view.line_number,
      properties: view.properties,
      children: view.children.map(child => ({
        name: child.name,
        type: child.type,
        line_number: child.line_number,
        properties: child.properties
      }))
    }));

    return NextResponse.json({
      valid: result.valid,
      errors: result.errors,
      warnings: result.warnings,
      statistics: result.statistics,
      models,
      views
    });

  } catch (error) {
    return NextResponse.json(
      { error: `Parse error: ${error instanceof Error ? error.message : String(error)}` },
      { status: 500 }
    );
  }
}