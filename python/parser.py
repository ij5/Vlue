from ply import yacc
import lexer

tokens = lexer.tokens

f = open('index.html', 'a')

final = ''

def p_root(t):
    '''
    root : head_expr inside
    '''
    t[0] = "<"+t[1]+">"+t[2]+"</"+t[1].split(' ')[0]+">"
    global final
    final = t[0]

def p_inside(t):
    '''
    inside : LMB inside_content RMB
        | LMB root RMB
        | empty
    '''
    if(t[1]==None):
        t[0] = ''
    else:
        t[0] = t[2]

def p_inside_content(t):
    '''
    inside_content : attr
        | empty
    '''
    if(t[1]==None):
        t[0] = ''
    else:
        t[0] = t[1]

def p_head(t):
    '''
    head_expr : IDENTIFIER elements_outside
    '''
    if(t[2] == ''):
        t[0] = t[1]
    else:
        t[0] = t[1] + ' ' + t[2]

def p_elements_outside(t):
    '''
    elements_outside : LSB elements_inside_comma RSB
    '''
    t[0] = t[2]

def p_elements_inside_comma1(t):
    '''
    elements_inside_comma : elements_inside_equal COMMA elements_inside_equal
    '''
    t[0] = t[1] + ' ' + t[3]

def p_elements_inside_comma2(t):
    '''
    elements_inside_comma : elements_inside_equal
        | empty
    '''
    if(t[1] == None):
        t[0] = ''
    else:
        t[0] = t[1]

def p_elements_inside_equal(t):
    '''
    elements_inside_equal : attr_root EQUAL attr_root
    '''
    t[0] = t[1] + '=' + '"' + t[3] + '"'

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

# filename = input("Input .ion file(without extension): ")
# outfile = input("Type output HTML file(without extension): ")
# data = open(filename+".ion", 'r')
# output = open(outfile+".html", 'w')
data = '''
html(){

}
'''
result = parser.parse(data)

print(final)