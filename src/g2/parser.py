from ply import yacc
import lexer

tokens = lexer.tokens

def p_test(t):
    'test : NEWLINE IDENTIFIER NEWLINE'
    t[0] = t[2]
    print(t[0])

def p_empty(t):
    'empty : '
    pass

def p_error(t):
    if(t):
        print("Error on token '%s'" % t.value)
    else:
        print("Error on EOF")

parser = yacc.yacc()

data = """
asdasd\t
"""

result = parser.parse(data)

