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


    # Enter a parse tree produced by PascalParser#funcDeclaration.
    def enterFuncDeclaration(self, ctx:PascalParser.FuncDeclarationContext):
        pass

    # Exit a parse tree produced by PascalParser#funcDeclaration.
    def exitFuncDeclaration(self, ctx:PascalParser.FuncDeclarationContext):
        pass


    # Enter a parse tree produced by PascalParser#procDeclaration.
    def enterProcDeclaration(self, ctx:PascalParser.ProcDeclarationContext):
        pass

    # Exit a parse tree produced by PascalParser#procDeclaration.
    def exitProcDeclaration(self, ctx:PascalParser.ProcDeclarationContext):
        pass


    # Enter a parse tree produced by PascalParser#varDeclarationBlock.
    def enterVarDeclarationBlock(self, ctx:PascalParser.VarDeclarationBlockContext):
        pass

    # Exit a parse tree produced by PascalParser#varDeclarationBlock.
    def exitVarDeclarationBlock(self, ctx:PascalParser.VarDeclarationBlockContext):
        pass


    # Enter a parse tree produced by PascalParser#varName.
    def enterVarName(self, ctx:PascalParser.VarNameContext):
        pass

    # Exit a parse tree produced by PascalParser#varName.
    def exitVarName(self, ctx:PascalParser.VarNameContext):
        pass


    # Enter a parse tree produced by PascalParser#varType.
    def enterVarType(self, ctx:PascalParser.VarTypeContext):
        pass

    # Exit a parse tree produced by PascalParser#varType.
    def exitVarType(self, ctx:PascalParser.VarTypeContext):
        pass


    # Enter a parse tree produced by PascalParser#argumentList.
    def enterArgumentList(self, ctx:PascalParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by PascalParser#argumentList.
    def exitArgumentList(self, ctx:PascalParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by PascalParser#funcCall.
    def enterFuncCall(self, ctx:PascalParser.FuncCallContext):
        pass

    # Exit a parse tree produced by PascalParser#funcCall.
    def exitFuncCall(self, ctx:PascalParser.FuncCallContext):
        pass


    # Enter a parse tree produced by PascalParser#procCall.
    def enterProcCall(self, ctx:PascalParser.ProcCallContext):
        pass

    # Exit a parse tree produced by PascalParser#procCall.
    def exitProcCall(self, ctx:PascalParser.ProcCallContext):
        pass


    # Enter a parse tree produced by PascalParser#parameter.
    def enterParameter(self, ctx:PascalParser.ParameterContext):
        pass

    # Exit a parse tree produced by PascalParser#parameter.
    def exitParameter(self, ctx:PascalParser.ParameterContext):
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


    # Enter a parse tree produced by PascalParser#ifStatement.
    def enterIfStatement(self, ctx:PascalParser.IfStatementContext):
        pass

    # Exit a parse tree produced by PascalParser#ifStatement.
    def exitIfStatement(self, ctx:PascalParser.IfStatementContext):
        pass


    # Enter a parse tree produced by PascalParser#elseStatement.
    def enterElseStatement(self, ctx:PascalParser.ElseStatementContext):
        pass

    # Exit a parse tree produced by PascalParser#elseStatement.
    def exitElseStatement(self, ctx:PascalParser.ElseStatementContext):
        pass


    # Enter a parse tree produced by PascalParser#blockBody.
    def enterBlockBody(self, ctx:PascalParser.BlockBodyContext):
        pass

    # Exit a parse tree produced by PascalParser#blockBody.
    def exitBlockBody(self, ctx:PascalParser.BlockBodyContext):
        pass



del PascalParser