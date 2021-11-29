import re
import sys
import os

from antlr4.InputStream import InputStream
from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.tree.Tree import ParseTreeWalker

from PascalLexer import PascalLexer
from PascalListener import PascalListener
from PascalParser import PascalParser

KEYWORDS = (
    'var', 'integer', 'string', 'real', 'boolean',
    'begin', 'end', 'program', 'function', 'procedure',
     'writeln',
    'mod', 'div', 'or', 'and',
    'if', 'then', 'else',
)

class Listener(PascalListener):
    def __init__(self):
        self.var_ls = {}
        self.spaces = -4

    def exitProgramName(self, ctx: PascalParser.ProgramNameContext):
        text = ctx.getText().split("program")[-1]
        self._print(f"#program {text}")

    def exitVarDeclarationBlock(self, ctx: PascalParser.VarDeclarationBlockContext):
        var_type = ctx.varType().getText()
        for i in ctx.varName().getText().split(','):
            self.var_ls[i] = var_type

    def enterFuncDeclaration(self, ctx: PascalParser.FuncDeclarationContext):
        self.spaces -= 0
        text = ctx.getText().split(';')[0].split('function')[1]
        type = ('string','integer','real','boolean','char')
        for i in type:
            if i in text:
                text = text.replace(i, '')
        if ':' in text:
            text = text.replace(':', '')
        self._print(f"def {text}:")

    def exitFuncDeclaration(self, ctx:PascalParser.FuncDeclarationContext):
        text = ctx.getText().split(';')[-3].split(':')[0]
        self._print(f'    return {text}')


    def exitWriteln(self, ctx: PascalParser.WritelnContext):
        self._print('print({})'.format(ctx.expressions().getText()))

    def exitAssignmentStatement(self, ctx: PascalParser.AssignmentStatementContext):
        var = ctx.ID().getText()
        expr = ctx.expression().getText()
        self._print(f'{var} = {expr}')

    def enterIfStatement(self, ctx: PascalParser.IfStatementContext):
        self._print(f'if {ctx.expression().getText()}:')

    def enterElseStatement(self, ctx: PascalParser.ElseStatementContext):
        self._print('else:')

    def enterCompoundStatement(self, ctx: PascalParser.CompoundStatementContext):
        self.spaces += 0

    def exitCompoundStatement(self, ctx: PascalParser.CompoundStatementContext):
        self.spaces -= 4

    def enterBlock(self, ctx: PascalParser.BlockContext):
        self.spaces += 4

    def exitBlock(self, ctx: PascalParser.BlockContext):
        self.spaces -= 4

    def enterBlockBody(self, ctx: PascalParser.BlockBodyContext):
        self.spaces += 4

    def exitBlockBody(self, ctx: PascalParser.BlockBodyContext):
        self.spaces -= 4

    def _print_input(self, var, const=None):
        const = const or ''
        var_type = self._get_var_type(var)
        if var_type:
            self._print(f'{var} = {var_type}(input({const}))')
        else:
            raise NotImplementedError

    def _get_var_type(self, var):
        type_list = {'integer': 'int', 'string': 'str', 'real': 'float', 'boolean': 'bool'}
        try:
            var_type = self.var_ls[var]
        except KeyError:
            raise ValueError(f'variable {var} not defined')
        if var_type in type_list.keys():
            print(type_list.get(var_type))
        else:
            raise NotImplementedError(var_type)

    def _print(self, line):
        with open("result.py", "a") as f:           # write interpreted code to result.py
            code = ' ' * self.spaces + line + "\n"
            f.write(code)
        print(' ' * self.spaces, line, sep='')


def main(filename):
    with open(filename) as f:
        text = f.read()
    text = re.sub(r'\b({})\b'.format(r'|'.join(KEYWORDS)), lambda m: m.group().lower(), text, flags=re.IGNORECASE)
    print("Pascal Test case:")
    print(text + "\n")

    print("Interpreter to Python:")
    text = text.replace('div', '//').replace('mod', '%')

    lexer = PascalLexer(InputStream(text))
    stream = CommonTokenStream(lexer)

    parser = PascalParser(stream)
    tree = parser.program()

    listener = Listener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    print('\nExecute code in Python:')
    os.system('python result.py')  # execute result.py
    open('result.py', 'w').close()  # clean and close result.py
    # print(listener.var_ls)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        # main('test/test0.pas')
        # main('test/test1.pas')
        # main('test/test2.pas')
        # main('test/test3.pas')
        # main('test/test4.pas')
        # main('test/test5.pas')
        # main('test/test6.pas')
        # main('test/test7.pas')
        # main('test/test8.pas')

