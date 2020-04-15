from ply import yacc
import lexer

tokens = lexer.tokens

def p_elements_outside(t):
    '''
    elements_outside : LSB elements_inside_comma RSB
    '''
    pass

def p_elements_inside_comma(t):
    '''
    elements_inside_comma : elements_inside_equal COMMA elements_inside_equal
        | elements_inside_equal

    '''
    pass

def p_elements_inside_equal(t):
    '''
    elements_inside_equal : attr EQUAL attr
    '''

def p_attr(t):
    '''
    attr : attr IDENTIFIER
        | attr OTHER
        | IDENTIFIER
        |  OTHER
    '''
    pass


def p_error(t):
    if(t):
        print("Error on token '%s'" % t.value)
    else:
        print("Error on EOF")


parser = yacc.yacc()

data = '''
(class = https://google.com)
'''
result = parser.parse(data)
