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
    'var', 'integer', 'int64', 'string', 'real',
    'begin', 'end', 'program',
    'readln', 'writeln',
    'mod', 'div', 'or', 'and',
)


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

    listener = PascalListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    print('\nExecute code in Python:')
    os.system('python result.py')  # execute result.py
    open('result.py', 'w').close()  # clean and close result.py

    print(listener.var_ls) # display parse tree

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        # main('test/test1.pas')
        # main('test/test2.pas')
        main('test/test3.pas')
        # main('test/test4.pas')
        # main('test/test5.pas')
        # main('test/test6.pas')
        # main('test/test7.pas')
        # main('test/test8.pas')
        # main('test/test9.pas')
        # main('test/test10.pas')
