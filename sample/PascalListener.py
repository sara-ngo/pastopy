# Generated from Pascal.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PascalParser import PascalParser
else:
    from PascalParser import PascalParser

# This class defines a complete listener for a parse tree produced by PascalParser.
class PascalListener(ParseTreeListener):

    # Enter a parse tree produced by PascalParser#program.
    def enterProgram(self, ctx:PascalParser.ProgramContext):
        pass

    # Exit a parse tree produced by PascalParser#program.
    def exitProgram(self, ctx:PascalParser.ProgramContext):
        pass


    # Enter a parse tree produced by PascalParser#programName.
    def enterProgramName(self, ctx:PascalParser.ProgramNameContext):
        pass

    # Exit a parse tree produced by PascalParser#programName.
    def exitProgramName(self, ctx:PascalParser.ProgramNameContext):
        pass


    # Enter a parse tree produced by PascalParser#varDeclaration.
    def enterVarDeclaration(self, ctx:PascalParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by PascalParser#varDeclaration.
    def exitVarDeclaration(self, ctx:PascalParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by PascalParser#varName.
    def enterVarName(self, ctx:PascalParser.VarNameContext):
        pass

    # Exit a parse tree produced by PascalParser#varName.
    def exitVarName(self, ctx:PascalParser.VarNameContext):
        pass


    # Enter a parse tree produced by PascalParser#varID.
    def enterVarID(self, ctx:PascalParser.VarIDContext):
        pass

    # Exit a parse tree produced by PascalParser#varID.
    def exitVarID(self, ctx:PascalParser.VarIDContext):
        pass


    # Enter a parse tree produced by PascalParser#varType.
    def enterVarType(self, ctx:PascalParser.VarTypeContext):
        pass

    # Exit a parse tree produced by PascalParser#varType.
    def exitVarType(self, ctx:PascalParser.VarTypeContext):
        pass


    # Enter a parse tree produced by PascalParser#block.
    def enterBlock(self, ctx:PascalParser.BlockContext):
        pass

    # Exit a parse tree produced by PascalParser#block.
    def exitBlock(self, ctx:PascalParser.BlockContext):
        pass


    # Enter a parse tree produced by PascalParser#statements.
    def enterStatements(self, ctx:PascalParser.StatementsContext):
        pass

    # Exit a parse tree produced by PascalParser#statements.
    def exitStatements(self, ctx:PascalParser.StatementsContext):
        pass


    # Enter a parse tree produced by PascalParser#statement.
    def enterStatement(self, ctx:PascalParser.StatementContext):
        pass

    # Exit a parse tree produced by PascalParser#statement.
    def exitStatement(self, ctx:PascalParser.StatementContext):
        pass


    # Enter a parse tree produced by PascalParser#writelnReadln.
    def enterWritelnReadln(self, ctx:PascalParser.WritelnReadlnContext):
        pass

    # Exit a parse tree produced by PascalParser#writelnReadln.
    def exitWritelnReadln(self, ctx:PascalParser.WritelnReadlnContext):
        pass


    # Enter a parse tree produced by PascalParser#readln.
    def enterReadln(self, ctx:PascalParser.ReadlnContext):
        pass

    # Exit a parse tree produced by PascalParser#readln.
    def exitReadln(self, ctx:PascalParser.ReadlnContext):
        pass


    # Enter a parse tree produced by PascalParser#writeln.
    def enterWriteln(self, ctx:PascalParser.WritelnContext):
        pass

    # Exit a parse tree produced by PascalParser#writeln.
    def exitWriteln(self, ctx:PascalParser.WritelnContext):
        pass


    # Enter a parse tree produced by PascalParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:PascalParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by PascalParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:PascalParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by PascalParser#expressions.
    def enterExpressions(self, ctx:PascalParser.ExpressionsContext):
        pass

    # Exit a parse tree produced by PascalParser#expressions.
    def exitExpressions(self, ctx:PascalParser.ExpressionsContext):
        pass


    # Enter a parse tree produced by PascalParser#expression.
    def enterExpression(self, ctx:PascalParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PascalParser#expression.
    def exitExpression(self, ctx:PascalParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PascalParser#operators.
    def enterOperators(self, ctx:PascalParser.OperatorsContext):
        pass

    # Exit a parse tree produced by PascalParser#operators.
    def exitOperators(self, ctx:PascalParser.OperatorsContext):
        pass


    # Enter a parse tree produced by PascalParser#blockBody.
    def enterBlockBody(self, ctx:PascalParser.BlockBodyContext):
        pass

    # Exit a parse tree produced by PascalParser#blockBody.
    def exitBlockBody(self, ctx:PascalParser.BlockBodyContext):
        pass



del PascalParser