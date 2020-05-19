from ply import lex

tokens = [
    'IDENTIFIER',
    'PYTHON'
]

def t_IDENTIFIER(t):
    r'[a-zA-Z_]+[a-zA-Z_0-9]*'
    return t

def t_PYTHON(t):
    r'`[^`]*`'
    return t

def t_error(t):
    print("error on token %s" % t.value)
    t.lexer.skip(1)

t_ignore = " \t\n"

lexer = lex.lex()

data = """
IDENTIFIER LSB RSB `print("Hello World!")`

"""

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
print()

from ply import yacc

pythoncommand = ""
grammar = ""

def p_root(t):
    '''
    root : expression
        | expression expression
    '''
    t[0] = t[1]

def p_expression(t):
    '''
    expression : identifier PYTHON
    '''
    t[0] = t[1] + t[2]
    pythoncommand

def p_expression_2(t):
    '''
    expression : expression identifier PYTHON
    '''

def p_identifier(t):
    '''
    identifier : identifier IDENTIFIER
    '''
    t[0] = t[1] + t[2]

def p_identifier_2(t):
    '''
    identifier : IDENTIFIER
    '''
    t[0] = t[1]


data = """

"""

parser = yacc.yacc()
result = parser.parse(data)