# Generated from Pascal.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PascalParser import PascalParser
else:
    from PascalParser import PascalParser

# This class defines a complete listener for a parse tree produced by PascalParser.
class PascalListener(ParseTreeListener):
    def __init__(self):
        self.var_ls = {}
        self.spaces = -4

    # Enter a parse tree produced by PascalParser#program.
    def enterProgram(self, ctx:PascalParser.ProgramContext):
        pass

    # Exit a parse tree produced by PascalParser#program.
    def exitProgram(self, ctx:PascalParser.ProgramContext):
        pass


    # Enter a parse tree produced by PascalParser#infoPart.
    def enterInfoPart(self, ctx:PascalParser.InfoPartContext):
        text = ctx.getText().split("program")[-1]
        self._print(f"#program {text}")

    # Exit a parse tree produced by PascalParser#infoPart.
    def exitInfoPart(self, ctx:PascalParser.InfoPartContext):
        pass


    # Enter a parse tree produced by PascalParser#variableDeclarationPart.
    def enterVariableDeclarationPart(self, ctx:PascalParser.VariableDeclarationPartContext):
        var_type = ctx.varType().getText()
        for i in ctx.identifierList().getText().split(','):
            self.var_ls[i] = var_type

    # Exit a parse tree produced by PascalParser#variableDeclarationPart.
    def exitVariableDeclarationPart(self, ctx:PascalParser.VariableDeclarationPartContext):
        pass


    # Enter a parse tree produced by PascalParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:PascalParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by PascalParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:PascalParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by PascalParser#identifierList.
    def enterIdentifierList(self, ctx:PascalParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by PascalParser#identifierList.
    def exitIdentifierList(self, ctx:PascalParser.IdentifierListContext):
        pass


    # Enter a parse tree produced by PascalParser#varType.
    def enterVarType(self, ctx:PascalParser.VarTypeContext):
        pass

    # Exit a parse tree produced by PascalParser#varType.
    def exitVarType(self, ctx:PascalParser.VarTypeContext):
        pass


    # Enter a parse tree produced by PascalParser#block.
    def enterBlock(self, ctx:PascalParser.BlockContext):
        self.spaces += 4

    # Exit a parse tree produced by PascalParser#block.
    def exitBlock(self, ctx:PascalParser.BlockContext):
        self.spaces -= 4


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
        var = ctx.ID().getText()
        const = ctx.CONST_STR().getText()
        self._print_input(var, const)

    # Exit a parse tree produced by PascalParser#writelnReadln.
    def exitWritelnReadln(self, ctx:PascalParser.WritelnReadlnContext):
        pass


    # Enter a parse tree produced by PascalParser#readln.
    def enterReadln(self, ctx:PascalParser.ReadlnContext):
        for i in ctx.identifierList().getText().split(','):
            self._print_input(i)

    # Exit a parse tree produced by PascalParser#readln.
    def exitReadln(self, ctx:PascalParser.ReadlnContext):
        pass


    # Enter a parse tree produced by PascalParser#writeln.
    def enterWriteln(self, ctx:PascalParser.WritelnContext):
        pass

    # Exit a parse tree produced by PascalParser#writeln.
    def exitWriteln(self, ctx:PascalParser.WritelnContext):
        self._print('print({})'.format(ctx.expressions().getText()))


    # Enter a parse tree produced by PascalParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:PascalParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by PascalParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:PascalParser.AssignmentStatementContext):
        var = ctx.ID().getText()
        expr = ctx.expression().getText()
        self._print(f'{var} = {expr}')


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
        self.spaces += 4

    # Exit a parse tree produced by PascalParser#blockBody.
    def exitBlockBody(self, ctx:PascalParser.BlockBodyContext):
        self.spaces -= 4

    def _print_input(self, var, const=None):
        const = const or ''
        var_type = self._get_var_type(var)
        if var_type:
            self._print(f'{var} = {var_type}(input({const}))')
        else:
            raise NotImplementedError

    def _get_var_type(self, var):
        try:
            var_type = self.var_ls[var]
        except KeyError:
            raise ValueError(f'variable {var} not defined')
        if var_type in ('integer', 'int64'):
            return 'int'
        elif var_type in ('real'):
            return 'float'
        elif var_type in ('string'):
            return 'string'
        else:
            raise NotImplementedError(var_type)

    def _print(self, line):  # print line by line
        with open("result.py", "a") as f:
            code = ' ' * self.spaces + line + "\n"
            f.write(code)
        print(' ' * self.spaces, line, sep='')

del PascalParser