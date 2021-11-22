grammar Pascal;

// parser = rules for Pascal grammar
// func: return a single value, proc: do not return anything
// ?: either have or not is fine
// .+?: any char/word/string
// *: allow repeat multiple times

program:
    (programName)? (varDeclaration)? (funcDeclaration)? (procDeclaration)? block DOT;

programName:
    'program' .+? SEMI;

varDeclaration:
    'var' varDeclarationBlock (SEMI varDeclarationBlock)* SEMI;

funcDeclaration:
    'function' ID LPAREN (argumentList)? RPAREN COLON varType SEMI varDeclaration block SEMI;

procDeclaration:
    'procedure' ID LPAREN (argumentList)? RPAREN SEMI varDeclaration block SEMI;

varDeclarationBlock:
    varName COLON varType;

varName:
    ID (COMMA ID)*;

varType:
    ('integer' | 'string' | 'real' | 'boolean');

argumentList:
    varName COLON varType;

funcCall:
    ID LPAREN parameter RPAREN;

procCall:
    ID LPAREN parameter RPAREN SEMI;

parameter:
    |
    expression (SEMI expression)*;

block:
    'begin' statements SEMI? 'end';

statements:
    statement (SEMI statement)*;

statement:
    writelnReadln
    | readln
    | writeln
    | block
    | assignmentStatement
    | ifStatement
    | funcCall
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
    (LPAREN expression RPAREN | CONST_INT | CONST_STR | ID | funcCall) (operators expression)*;

operators:
    EQUAL | NOT_EQUAL | LT | LE | GE | GT | OR | AND | DIV | MOD | PLUS | MINUS | STAR | SLASH;

ifStatement:
    'if' expression 'then' (block|blockBody) elseStatement?;

elseStatement:
    'else' (block|blockBody);

blockBody:
    statement;

// lexer = produce tokens from input
SEMI: ';';
COLON: ':';
COMMA: ',';
DOT: '.';
LPAREN: '(';
RPAREN: ')';
ASSIGN: ':=';

PLUS: '+';
MINUS: '-';
STAR: '*';
SLASH: '/';
DIV: '//';
MOD: '%';

EQUAL: '=';
NOT_EQUAL: '<>';
LT: '<';
LE: '<=';
GT: '>';
GE: '>=';
OR: 'or';
AND: 'and';

ID: [a-zA-Z][a-zA-Z0-9_]*;
CONST_INT: [0-9]+;
CONST_STR: '\'' ('\'\'' | ~ ('\''))* '\'';
WS: [ \t\r\n]+ -> skip;
COMMENT: '(*' .*? '*)' -> skip;
