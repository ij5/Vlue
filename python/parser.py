from ply import yacc
import lexer

tokens = lexer.tokens



def p_identifier(t):
    '''
    identifier : IDENTIFIER
        | identifier IDENTIFIER
    '''
    pass

def p_elements(t):
    '''elements : LSB p_elements_inside RSB
        | NONE'''
    print(t[0])

def p_elements_inside(t):
    '''elements_inside : elements_attributes
        | elements_inside COMMA elements_inside'''
    pass

def p_elements_attributes(t):
    '''elements_attributes : IDENTIFIER EQUAL IDENTIFIER'''
    pass

def p_error(t):
    if(t):
        print("Error on token '%s'" % t.value)
    else:
        print("Error on EOF")


parser = yacc.yacc()

data = '''
html(){
    head(){
    
    }
    body(){
        div(class=mainContent, id=mainContent){
            button(class=mainButton){Press me!}
            a(href=https://google.com,class=mainlink){Click me!}
        }
    }
}
'''
result = parser.parse(data)
