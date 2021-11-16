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
    'var', 'integer', 'int64', 'real', 'string',
    'begin', 'end', 'program',
    'readln', 'writeln',
    'mod', 'div', 'or', 'and',
)

class Listener(PascalListener):
    def __init__(self):
        self.var_ls = {}
        self.spaces = -4

    def exitInfoPart(self, ctx: PascalParser.InfoPartContext):
        text = ctx.getText().split("program")[-1]
        self._print(f"#program {text}")

    def exitVariableDeclaration(self, ctx: PascalParser.VariableDeclarationContext):
        var_type = ctx.varType().getText()
        for i in ctx.identifierList().getText().split(','):
            self.var_ls[i] = var_type

    def exitWritelnReadln(self, ctx: PascalParser.WritelnReadlnContext):
        var = ctx.ID().getText()
        const = ctx.CONST_STR().getText()
        self._print_input(var, const)

    def enterReadln(self, ctx: PascalParser.ReadlnContext):
        for i in ctx.identifierList().getText().split(','):
            self._print_input(i)

    def exitWriteln(self, ctx: PascalParser.WritelnContext):
        self._print('print({})'.format(ctx.expressions().getText()))

    def exitAssignmentStatement(self, ctx: PascalParser.AssignmentStatementContext):
        var = ctx.ID().getText()
        expr = ctx.expression().getText()
        self._print(f'{var} = {expr}')

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
        try:
            var_type = self.var_ls[var]
        except KeyError:
            raise ValueError(f'variable {var} not defined')
        if var_type in ('integer', 'int64'):
            return 'int'
        elif var_type in ('real'):
            return 'float'
        elif var_type  in ('string'):
            return 'string'
        else:
            raise NotImplementedError(var_type)

    def _print(self, line):  # print line by line
        with open("result.py", "a") as f:
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
        # main('test/test1.pas')
        # main('test/test2.pas')
        # main('test/test3.pas')
        # main('test/test4.pas')
        main('test/test5.pas')
        # main('test/test6.pas')
        # main('test/test7.pas')
        # main('test/test8.pas')
        # main('test/test9.pas')
        # main('test/test10.pas')
