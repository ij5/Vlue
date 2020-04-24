from ply import yacc
import lexer

tokens = lexer.tokens

def p_root(t):
    '''
    root : NEWLINE root
        | head NEWLINE body
        | head elements
        | head
    '''
    pass

def p_body_exp(t):
    '''
    body : TAB root
        | TAB elements
    '''
    pass

def p_elements(t):
    '''
    elements : elements IDENTIFIER
        | elements EQUAL
        | elements OTHER
        | IDENTIFIER
        | EQUAL
        | OTHER
    '''
    pass

def p_head_exp(t):
    '''
    head : IDENTIFIER attr COLON
        | IDENTIFIER empty COLON
    '''
    t[0] = t[1]+t[2]+t[3]
    print(t[0])

def p_attr(t):
    '''
    attr : attr_equal
        | empty
    '''
    if(t[1]==None):
        t[0] = ""
    else:
        t[0] = t[1]

def p_attr_equal(t):
    '''
    attr_equal : IDENTIFIER EQUAL SQ other SQ
        | IDENTIFIER EQUAL DQ other DQ
    '''
    t[0] = t[1]+t[2]+t[3]+t[4]+t[5]

def p_other(t):
    '''
    other : other EQUAL
        | other COMMA
        | other COLON
        | other IDENTIFIER
        | other OTHER
        | EQUAL
        | COMMA
        | COLON
        | IDENTIFIER
        | OTHER
    '''
    try:
        t[0] = t[1]+t[2]
    except:
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

data = """div class='https://google.com':"""

result = parser.parse(data)

