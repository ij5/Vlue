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

def p_root(t):
    '''
    root : expression
    '''
    t[0] = t[1]


data = """

"""

parser = yacc.yacc()
result = parser.parse(data)