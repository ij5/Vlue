from ply import yacc
import lexer

tokens = lexer.tokens

def p_root(t):
    '''root : head_expr inside'''
    pass

def p_inside(t):
    '''
    inside : LMB inside_content RMB
        | LMB root RMB
    '''
    pass

def p_inside_content(t):
    '''
    inside_content : attr
        | empty
    '''
    pass

def p_head(t):
    '''
    head_expr : HTML elements_outside
    '''         #TODO: 다른 태그 추가

    print(t[1]+', '+t[2])

def p_elements_outside(t):
    '''
    elements_outside : LSB elements_inside_comma RSB
    '''
    t[0] = t[1]+t[2]+t[3]

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
    elements_inside_equal : attr_root EQUAL attr_root
    '''
    t[0] = t[1]+t[2]+t[3]

def p_attr0(t):
    '''
    attr_root : attr attr
    '''
    t[0] = t[1]+t[2]

def p_attr00(t):
    'attr_root : attr'
    t[0] = t[1]

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
        | HTML
    '''     #TODO: 다른 태그 추가

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
html(html=google.com){}
'''
result = parser.parse(data)