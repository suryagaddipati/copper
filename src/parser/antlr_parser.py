from typing import Optional
import antlr4
from antlr4.error.ErrorListener import ErrorListener
from .ast_nodes import *


class CopperErrorListener(ErrorListener):
    
    def __init__(self):
        super().__init__()
        self.errors = []
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_msg = f"Line {line}:{column} - {msg}"
        self.errors.append(error_msg)


class CopperParser:
    
    def __init__(self):
        self.error_listener = CopperErrorListener()
    
    def parse(self, expression: str) -> ASTNode:
        try:
            from copper.parser.generated.grammar.CopperLexer import CopperLexer
            from copper.parser.generated.grammar.CopperParser import CopperParser as GeneratedParser
            from copper.parser.generated.grammar.CopperVisitor import CopperVisitor
            
            input_stream = antlr4.InputStream(expression)
            lexer = CopperLexer(input_stream)
            lexer.removeErrorListeners()
            lexer.addErrorListener(self.error_listener)
            
            token_stream = antlr4.CommonTokenStream(lexer)
            parser = GeneratedParser(token_stream)
            parser.removeErrorListeners()
            parser.addErrorListener(self.error_listener)
            
            tree = parser.expression()
            
            if self.error_listener.errors:
                raise SyntaxError(f"Parse errors: {'; '.join(self.error_listener.errors)}")
            
            visitor = ASTBuilderVisitor()
            ast = visitor.visit(tree)
            
            return ast
            
        except ImportError:
            raise ImportError(
                "ANTLR generated parser not found. "
                "Run 'make parser' to generate the parser from the grammar."
            )


class ASTBuilderVisitor:
    
    def visit(self, ctx):
        method_name = f'visit{ctx.__class__.__name__}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(ctx)
    
    def generic_visit(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        
        results = []
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if hasattr(child, 'accept'):
                results.append(self.visit(child))
        
        return results[0] if len(results) == 1 else results
    
    def visitExpressionContext(self, ctx):
        return self.visit(ctx.logicalOrExpression())
    
    def visitLogicalOrExpressionContext(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.logicalAndExpression(0))
        
        result = self.visit(ctx.logicalAndExpression(0))
        for i in range(1, len(ctx.logicalAndExpression())):
            right = self.visit(ctx.logicalAndExpression(i))
            result = BinaryOperation(result, 'OR', right)
        
        return result
    
    def visitLogicalAndExpressionContext(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.equalityExpression(0))
        
        result = self.visit(ctx.equalityExpression(0))
        for i in range(1, len(ctx.equalityExpression())):
            right = self.visit(ctx.equalityExpression(i))
            result = BinaryOperation(result, 'AND', right)
        
        return result
    
    def visitEqualityExpressionContext(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.relationalExpression(0))
        
        result = self.visit(ctx.relationalExpression(0))
        for i in range(1, len(ctx.relationalExpression())):
            operator = ctx.getChild(i * 2 - 1).getText()
            right = self.visit(ctx.relationalExpression(i))
            result = BinaryOperation(result, operator, right)
        
        return result
    
    def visitLiteralContext(self, ctx):
        if ctx.NUMBER():
            value = ctx.NUMBER().getText()
            return Literal(float(value) if '.' in value else int(value), 'number')
        elif ctx.STRING():
            value = ctx.STRING().getText()[1:-1]
            return Literal(value, 'string')
        elif ctx.BOOLEAN():
            value = ctx.BOOLEAN().getText().upper() == 'TRUE'
            return Literal(value, 'boolean')
        elif ctx.NULL():
            return Literal(None, 'null')
    
    def visitIdentifierContext(self, ctx):
        if ctx.IDENTIFIER():
            return Identifier(ctx.IDENTIFIER().getText())
        elif ctx.QUOTED_IDENTIFIER():
            name = ctx.QUOTED_IDENTIFIER().getText()[1:-1]
            return Identifier(name)
    
    def visitColumnReferenceContext(self, ctx):
        if ctx.tableName():
            table = self.visit(ctx.tableName()).name
            column = self.visit(ctx.columnName()).name
            return ColumnReference(table, column)
        else:
            column = self.visit(ctx.columnName()).name
            return ColumnReference(None, column)
    
    def visitFunctionCallContext(self, ctx):
        function_name = ctx.functionName().getText()
        
        arguments = []
        if ctx.argumentList():
            for expr_ctx in ctx.argumentList().expression():
                arguments.append(self.visit(expr_ctx))
        
        return FunctionCall(function_name, arguments)
    
    def visitIfExpressionContext(self, ctx):
        expressions = [self.visit(expr) for expr in ctx.expression()]
        return IfExpression(expressions[0], expressions[1], expressions[2])