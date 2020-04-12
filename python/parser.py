from ply import yacc
import lexer

tokens = lexer.tokens

def p_expr(t):
    'expr : LSB RSB'
    print(t[1])

def p_error(t):
    if(t):
        print("Error on token '%s'" % t.value)
    else:
        print("Error on EOF")


parser = yacc.yacc()

data = '()'
result = parser.parse(data)
