grammar Pascal;

// parser
program:
    (programName)? (globalVarDeclaration)? block DOT;

programName:
    'program' .+? SEMI;

globalVarDeclaration:
    'var' variableDeclaration (SEMI variableDeclaration)* SEMI;

variableDeclaration:
    varName COLON varType;

varName:
    ID (COMMA ID)*;

varType:
    ('integer' | 'real' | 'string');

block:
    'begin' statements SEMI? 'end';

statements:
    statement (SEMI statement)*;

statement:
    writelnReadln
    | readln
    | writeln
    | assignmentStatement
    | block
    ;

writelnReadln:
    'writeln' LPAREN CONST_STR RPAREN SEMI
    'readln' LPAREN ID RPAREN;

readln:
    'readln' LPAREN varName RPAREN;

writeln:
    'writeln' LPAREN expressions RPAREN;

assignmentStatement:
    ID ASSIGN expression;

expressions:
    expression (COMMA expression)*;

expression:
    (LPAREN expression RPAREN | CONST_INT | CONST_STR | ID) (operators expression)*;

operators:
    DIV | MOD | PLUS | MINUS | MUL | SLASH;

blockBody:
    statement;

// lexer
SEMI: ';';
COLON: ':';
COMMA: ',';
DOT: '.';
LPAREN: '(';
RPAREN: ')';
ASSIGN: ':=';

PLUS: '+';
MINUS: '-';
MUL: '*';
SLASH: '/';
DIV: '//';
MOD: '%';

ID: [a-zA-Z][a-zA-Z0-9_]*;
CONST_INT: [0-9]+;
CONST_STR: '\'' ('\'\'' | ~ ('\''))* '\'';
WS: [ \t\r\n]+ -> skip;
COMMENT: '(*' .*? '*)' -> skip;