from ply import yacc
import lexer

tokens = lexer.tokens


def p_html_inside_identifier(t):
    '''
    html_inside : LMB IDENTIFIER RMB
    '''
    print(t[2])



def p_elements_expr(t):
    '''
    elements_expr : LSB elements RSB
    '''
    t[0] = t[1]+t[2]+t[3]


def p_elements_comma(t):
    '''
    elements : elements COMMA elements
    '''
    t[0] = t[1] + t[2] + t[3]


def p_elements_equal(t):
    '''
    elements : IDENTIFIER EQUAL IDENTIFIER
    '''
    t[0] = t[1]+t[2]+t[3]

def p_error(t):
    if(t):
        print("Error on token '%s'" % t.value)
    else:
        print("Error on EOF")


parser = yacc.yacc()

data = '{asis3o}'
result = parser.parse(data)
