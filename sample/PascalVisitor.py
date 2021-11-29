# Generated from Pascal.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PascalParser import PascalParser
else:
    from PascalParser import PascalParser

# This class defines a complete generic visitor for a parse tree produced by PascalParser.

class PascalVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PascalParser#program.
    def visitProgram(self, ctx:PascalParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#programName.
    def visitProgramName(self, ctx:PascalParser.ProgramNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#block.
    def visitBlock(self, ctx:PascalParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#varDeclaration.
    def visitVarDeclaration(self, ctx:PascalParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#funcDeclaration.
    def visitFuncDeclaration(self, ctx:PascalParser.FuncDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#funcDeclarationBlock.
    def visitFuncDeclarationBlock(self, ctx:PascalParser.FuncDeclarationBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#varDeclarationBlock.
    def visitVarDeclarationBlock(self, ctx:PascalParser.VarDeclarationBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#varName.
    def visitVarName(self, ctx:PascalParser.VarNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#varType.
    def visitVarType(self, ctx:PascalParser.VarTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#argumentList.
    def visitArgumentList(self, ctx:PascalParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#funcCall.
    def visitFuncCall(self, ctx:PascalParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#parameter.
    def visitParameter(self, ctx:PascalParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#compoundStatement.
    def visitCompoundStatement(self, ctx:PascalParser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#statements.
    def visitStatements(self, ctx:PascalParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#statement.
    def visitStatement(self, ctx:PascalParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#writeln.
    def visitWriteln(self, ctx:PascalParser.WritelnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:PascalParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#expressions.
    def visitExpressions(self, ctx:PascalParser.ExpressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#expression.
    def visitExpression(self, ctx:PascalParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#operators.
    def visitOperators(self, ctx:PascalParser.OperatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#ifStatement.
    def visitIfStatement(self, ctx:PascalParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#elseStatement.
    def visitElseStatement(self, ctx:PascalParser.ElseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#blockBody.
    def visitBlockBody(self, ctx:PascalParser.BlockBodyContext):
        return self.visitChildren(ctx)



del PascalParser