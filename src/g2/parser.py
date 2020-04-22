from ply import yacc
import lexer

tokens = lexer.tokens

def p_head_first(t):
    'head_first : IDENTIFIER'

def p_head_end(t):
    'head_end : IDENTIFIER'



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

