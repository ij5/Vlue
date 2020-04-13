from ply import yacc
import lexer

tokens = lexer.tokens


def p_html_inside_identifier(t):
    '''
    html_inside : LMB contents_expr RMB
    '''
    pass

def p_contents_expr(t):
    '''
    contents_expr : contents_expr
        | IDENTIFIER
    '''
    pass

def p_elements_expr(t):
    '''
    elements_expr : LSB elements RSB
    '''
    pass


def p_elements_comma(t):
    '''
    elements : elements COMMA elements
    '''
    pass


def p_elements_equal(t):
    '''
    elements : IDENTIFIER EQUAL IDENTIFIER
    '''
    pass

def p_error(t):
    if(t):
        print("Error on token '%s'" % t.value)
    else:
        print("Error on EOF")


parser = yacc.yacc()

data = '{asd..}'
result = parser.parse(data)
