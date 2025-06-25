# Generated from Copper.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CopperParser import CopperParser
else:
    from CopperParser import CopperParser

# This class defines a complete listener for a parse tree produced by CopperParser.
class CopperListener(ParseTreeListener):

    # Enter a parse tree produced by CopperParser#program.
    def enterProgram(self, ctx:CopperParser.ProgramContext):
        pass

    # Exit a parse tree produced by CopperParser#program.
    def exitProgram(self, ctx:CopperParser.ProgramContext):
        pass


    # Enter a parse tree produced by CopperParser#statement.
    def enterStatement(self, ctx:CopperParser.StatementContext):
        pass

    # Exit a parse tree produced by CopperParser#statement.
    def exitStatement(self, ctx:CopperParser.StatementContext):
        pass


    # Enter a parse tree produced by CopperParser#comment.
    def enterComment(self, ctx:CopperParser.CommentContext):
        pass

    # Exit a parse tree produced by CopperParser#comment.
    def exitComment(self, ctx:CopperParser.CommentContext):
        pass


    # Enter a parse tree produced by CopperParser#modelStatement.
    def enterModelStatement(self, ctx:CopperParser.ModelStatementContext):
        pass

    # Exit a parse tree produced by CopperParser#modelStatement.
    def exitModelStatement(self, ctx:CopperParser.ModelStatementContext):
        pass


    # Enter a parse tree produced by CopperParser#modelBody.
    def enterModelBody(self, ctx:CopperParser.ModelBodyContext):
        pass

    # Exit a parse tree produced by CopperParser#modelBody.
    def exitModelBody(self, ctx:CopperParser.ModelBodyContext):
        pass


    # Enter a parse tree produced by CopperParser#dimensionStatement.
    def enterDimensionStatement(self, ctx:CopperParser.DimensionStatementContext):
        pass

    # Exit a parse tree produced by CopperParser#dimensionStatement.
    def exitDimensionStatement(self, ctx:CopperParser.DimensionStatementContext):
        pass


    # Enter a parse tree produced by CopperParser#measureStatement.
    def enterMeasureStatement(self, ctx:CopperParser.MeasureStatementContext):
        pass

    # Exit a parse tree produced by CopperParser#measureStatement.
    def exitMeasureStatement(self, ctx:CopperParser.MeasureStatementContext):
        pass


    # Enter a parse tree produced by CopperParser#viewStatement.
    def enterViewStatement(self, ctx:CopperParser.ViewStatementContext):
        pass

    # Exit a parse tree produced by CopperParser#viewStatement.
    def exitViewStatement(self, ctx:CopperParser.ViewStatementContext):
        pass


    # Enter a parse tree produced by CopperParser#viewBody.
    def enterViewBody(self, ctx:CopperParser.ViewBodyContext):
        pass

    # Exit a parse tree produced by CopperParser#viewBody.
    def exitViewBody(self, ctx:CopperParser.ViewBodyContext):
        pass


    # Enter a parse tree produced by CopperParser#fromStatement.
    def enterFromStatement(self, ctx:CopperParser.FromStatementContext):
        pass

    # Exit a parse tree produced by CopperParser#fromStatement.
    def exitFromStatement(self, ctx:CopperParser.FromStatementContext):
        pass


    # Enter a parse tree produced by CopperParser#joinStatement.
    def enterJoinStatement(self, ctx:CopperParser.JoinStatementContext):
        pass

    # Exit a parse tree produced by CopperParser#joinStatement.
    def exitJoinStatement(self, ctx:CopperParser.JoinStatementContext):
        pass


    # Enter a parse tree produced by CopperParser#extendsStatement.
    def enterExtendsStatement(self, ctx:CopperParser.ExtendsStatementContext):
        pass

    # Exit a parse tree produced by CopperParser#extendsStatement.
    def exitExtendsStatement(self, ctx:CopperParser.ExtendsStatementContext):
        pass


    # Enter a parse tree produced by CopperParser#extensionStatement.
    def enterExtensionStatement(self, ctx:CopperParser.ExtensionStatementContext):
        pass

    # Exit a parse tree produced by CopperParser#extensionStatement.
    def exitExtensionStatement(self, ctx:CopperParser.ExtensionStatementContext):
        pass


    # Enter a parse tree produced by CopperParser#dimensionParameter.
    def enterDimensionParameter(self, ctx:CopperParser.DimensionParameterContext):
        pass

    # Exit a parse tree produced by CopperParser#dimensionParameter.
    def exitDimensionParameter(self, ctx:CopperParser.DimensionParameterContext):
        pass


    # Enter a parse tree produced by CopperParser#typeParameter.
    def enterTypeParameter(self, ctx:CopperParser.TypeParameterContext):
        pass

    # Exit a parse tree produced by CopperParser#typeParameter.
    def exitTypeParameter(self, ctx:CopperParser.TypeParameterContext):
        pass


    # Enter a parse tree produced by CopperParser#dimensionType.
    def enterDimensionType(self, ctx:CopperParser.DimensionTypeContext):
        pass

    # Exit a parse tree produced by CopperParser#dimensionType.
    def exitDimensionType(self, ctx:CopperParser.DimensionTypeContext):
        pass


    # Enter a parse tree produced by CopperParser#measureParameter.
    def enterMeasureParameter(self, ctx:CopperParser.MeasureParameterContext):
        pass

    # Exit a parse tree produced by CopperParser#measureParameter.
    def exitMeasureParameter(self, ctx:CopperParser.MeasureParameterContext):
        pass


    # Enter a parse tree produced by CopperParser#measureTypeParameter.
    def enterMeasureTypeParameter(self, ctx:CopperParser.MeasureTypeParameterContext):
        pass

    # Exit a parse tree produced by CopperParser#measureTypeParameter.
    def exitMeasureTypeParameter(self, ctx:CopperParser.MeasureTypeParameterContext):
        pass


    # Enter a parse tree produced by CopperParser#measureType.
    def enterMeasureType(self, ctx:CopperParser.MeasureTypeContext):
        pass

    # Exit a parse tree produced by CopperParser#measureType.
    def exitMeasureType(self, ctx:CopperParser.MeasureTypeContext):
        pass


    # Enter a parse tree produced by CopperParser#joinParameter.
    def enterJoinParameter(self, ctx:CopperParser.JoinParameterContext):
        pass

    # Exit a parse tree produced by CopperParser#joinParameter.
    def exitJoinParameter(self, ctx:CopperParser.JoinParameterContext):
        pass


    # Enter a parse tree produced by CopperParser#joinTypeParameter.
    def enterJoinTypeParameter(self, ctx:CopperParser.JoinTypeParameterContext):
        pass

    # Exit a parse tree produced by CopperParser#joinTypeParameter.
    def exitJoinTypeParameter(self, ctx:CopperParser.JoinTypeParameterContext):
        pass


    # Enter a parse tree produced by CopperParser#joinType.
    def enterJoinType(self, ctx:CopperParser.JoinTypeContext):
        pass

    # Exit a parse tree produced by CopperParser#joinType.
    def exitJoinType(self, ctx:CopperParser.JoinTypeContext):
        pass


    # Enter a parse tree produced by CopperParser#relationshipParameter.
    def enterRelationshipParameter(self, ctx:CopperParser.RelationshipParameterContext):
        pass

    # Exit a parse tree produced by CopperParser#relationshipParameter.
    def exitRelationshipParameter(self, ctx:CopperParser.RelationshipParameterContext):
        pass


    # Enter a parse tree produced by CopperParser#relationshipType.
    def enterRelationshipType(self, ctx:CopperParser.RelationshipTypeContext):
        pass

    # Exit a parse tree produced by CopperParser#relationshipType.
    def exitRelationshipType(self, ctx:CopperParser.RelationshipTypeContext):
        pass


    # Enter a parse tree produced by CopperParser#expressionParameter.
    def enterExpressionParameter(self, ctx:CopperParser.ExpressionParameterContext):
        pass

    # Exit a parse tree produced by CopperParser#expressionParameter.
    def exitExpressionParameter(self, ctx:CopperParser.ExpressionParameterContext):
        pass


    # Enter a parse tree produced by CopperParser#primaryKeyParameter.
    def enterPrimaryKeyParameter(self, ctx:CopperParser.PrimaryKeyParameterContext):
        pass

    # Exit a parse tree produced by CopperParser#primaryKeyParameter.
    def exitPrimaryKeyParameter(self, ctx:CopperParser.PrimaryKeyParameterContext):
        pass


    # Enter a parse tree produced by CopperParser#valueFormatParameter.
    def enterValueFormatParameter(self, ctx:CopperParser.ValueFormatParameterContext):
        pass

    # Exit a parse tree produced by CopperParser#valueFormatParameter.
    def exitValueFormatParameter(self, ctx:CopperParser.ValueFormatParameterContext):
        pass


    # Enter a parse tree produced by CopperParser#labelParameter.
    def enterLabelParameter(self, ctx:CopperParser.LabelParameterContext):
        pass

    # Exit a parse tree produced by CopperParser#labelParameter.
    def exitLabelParameter(self, ctx:CopperParser.LabelParameterContext):
        pass


    # Enter a parse tree produced by CopperParser#descriptionParameter.
    def enterDescriptionParameter(self, ctx:CopperParser.DescriptionParameterContext):
        pass

    # Exit a parse tree produced by CopperParser#descriptionParameter.
    def exitDescriptionParameter(self, ctx:CopperParser.DescriptionParameterContext):
        pass


    # Enter a parse tree produced by CopperParser#hiddenParameter.
    def enterHiddenParameter(self, ctx:CopperParser.HiddenParameterContext):
        pass

    # Exit a parse tree produced by CopperParser#hiddenParameter.
    def exitHiddenParameter(self, ctx:CopperParser.HiddenParameterContext):
        pass


    # Enter a parse tree produced by CopperParser#tiersParameter.
    def enterTiersParameter(self, ctx:CopperParser.TiersParameterContext):
        pass

    # Exit a parse tree produced by CopperParser#tiersParameter.
    def exitTiersParameter(self, ctx:CopperParser.TiersParameterContext):
        pass


    # Enter a parse tree produced by CopperParser#sqlLatitudeParameter.
    def enterSqlLatitudeParameter(self, ctx:CopperParser.SqlLatitudeParameterContext):
        pass

    # Exit a parse tree produced by CopperParser#sqlLatitudeParameter.
    def exitSqlLatitudeParameter(self, ctx:CopperParser.SqlLatitudeParameterContext):
        pass


    # Enter a parse tree produced by CopperParser#sqlLongitudeParameter.
    def enterSqlLongitudeParameter(self, ctx:CopperParser.SqlLongitudeParameterContext):
        pass

    # Exit a parse tree produced by CopperParser#sqlLongitudeParameter.
    def exitSqlLongitudeParameter(self, ctx:CopperParser.SqlLongitudeParameterContext):
        pass


    # Enter a parse tree produced by CopperParser#unitsParameter.
    def enterUnitsParameter(self, ctx:CopperParser.UnitsParameterContext):
        pass

    # Exit a parse tree produced by CopperParser#unitsParameter.
    def exitUnitsParameter(self, ctx:CopperParser.UnitsParameterContext):
        pass


    # Enter a parse tree produced by CopperParser#daxExpression.
    def enterDaxExpression(self, ctx:CopperParser.DaxExpressionContext):
        pass

    # Exit a parse tree produced by CopperParser#daxExpression.
    def exitDaxExpression(self, ctx:CopperParser.DaxExpressionContext):
        pass


    # Enter a parse tree produced by CopperParser#daxContent.
    def enterDaxContent(self, ctx:CopperParser.DaxContentContext):
        pass

    # Exit a parse tree produced by CopperParser#daxContent.
    def exitDaxContent(self, ctx:CopperParser.DaxContentContext):
        pass


    # Enter a parse tree produced by CopperParser#daxToken.
    def enterDaxToken(self, ctx:CopperParser.DaxTokenContext):
        pass

    # Exit a parse tree produced by CopperParser#daxToken.
    def exitDaxToken(self, ctx:CopperParser.DaxTokenContext):
        pass


    # Enter a parse tree produced by CopperParser#identifier.
    def enterIdentifier(self, ctx:CopperParser.IdentifierContext):
        pass

    # Exit a parse tree produced by CopperParser#identifier.
    def exitIdentifier(self, ctx:CopperParser.IdentifierContext):
        pass


    # Enter a parse tree produced by CopperParser#contextualKeyword.
    def enterContextualKeyword(self, ctx:CopperParser.ContextualKeywordContext):
        pass

    # Exit a parse tree produced by CopperParser#contextualKeyword.
    def exitContextualKeyword(self, ctx:CopperParser.ContextualKeywordContext):
        pass


    # Enter a parse tree produced by CopperParser#stringLiteral.
    def enterStringLiteral(self, ctx:CopperParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by CopperParser#stringLiteral.
    def exitStringLiteral(self, ctx:CopperParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by CopperParser#numberLiteral.
    def enterNumberLiteral(self, ctx:CopperParser.NumberLiteralContext):
        pass

    # Exit a parse tree produced by CopperParser#numberLiteral.
    def exitNumberLiteral(self, ctx:CopperParser.NumberLiteralContext):
        pass


    # Enter a parse tree produced by CopperParser#booleanValue.
    def enterBooleanValue(self, ctx:CopperParser.BooleanValueContext):
        pass

    # Exit a parse tree produced by CopperParser#booleanValue.
    def exitBooleanValue(self, ctx:CopperParser.BooleanValueContext):
        pass


    # Enter a parse tree produced by CopperParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:CopperParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by CopperParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:CopperParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by CopperParser#formatName.
    def enterFormatName(self, ctx:CopperParser.FormatNameContext):
        pass

    # Exit a parse tree produced by CopperParser#formatName.
    def exitFormatName(self, ctx:CopperParser.FormatNameContext):
        pass


    # Enter a parse tree produced by CopperParser#units.
    def enterUnits(self, ctx:CopperParser.UnitsContext):
        pass

    # Exit a parse tree produced by CopperParser#units.
    def exitUnits(self, ctx:CopperParser.UnitsContext):
        pass


    # Enter a parse tree produced by CopperParser#identifierList.
    def enterIdentifierList(self, ctx:CopperParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by CopperParser#identifierList.
    def exitIdentifierList(self, ctx:CopperParser.IdentifierListContext):
        pass


    # Enter a parse tree produced by CopperParser#stringList.
    def enterStringList(self, ctx:CopperParser.StringListContext):
        pass

    # Exit a parse tree produced by CopperParser#stringList.
    def exitStringList(self, ctx:CopperParser.StringListContext):
        pass


    # Enter a parse tree produced by CopperParser#numberList.
    def enterNumberList(self, ctx:CopperParser.NumberListContext):
        pass

    # Exit a parse tree produced by CopperParser#numberList.
    def exitNumberList(self, ctx:CopperParser.NumberListContext):
        pass



del CopperParser