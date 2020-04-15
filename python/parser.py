from ply import yacc
import lexer

tokens = lexer.tokens

def p_elements_outside(t):
    '''
    elements_outside : LSB elements_inside_comma RSB
    '''
    print(t[2])

def p_elements_inside_comma1(t):
    '''
    elements_inside_comma : elements_inside_equal COMMA elements_inside_equal
    '''
    t[0] = t[1]+t[2]+t[3]

def p_elements_inside_comma2(t):
    '''
    elements_inside_comma : elements_inside_equal
        | empty
    '''
    t[0] = t[1]

def p_elements_inside_equal(t):
    '''
    elements_inside_equal : attr EQUAL attr
    '''
    t[0] = t[1]+t[2]+t[3]

def p_attr1(t):
    '''
    attr : attr IDENTIFIER
        | attr OTHER
    '''
    t[0] = t[1] + t[2]

def p_attr2(t):
    '''
    attr : IDENTIFIER
        | OTHER
    '''
    t[0] = t[1]


def p_empty(t):
    'empty : '
    pass

def p_error(t):
    if(t):
        print("Error on token '%s'" % t.value)
    else:
        print("Error on EOF")


parser = yacc.yacc()

data = '''
(href =https://www.google.com/)
'''
result = parser.parse(data)
