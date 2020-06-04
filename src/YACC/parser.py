from ply import yacc

from lexer import tokens

def p_statement(t):
    '''
    statement : statement expression
        | statement if_statement
        | expression
        | if_statement
    '''
    pass

def p_if_statement(t):
    '''
    if_statement : IF LSB expression RSB LMB statement RMB
    '''
    pass

def p_expression(t):
    '''
    expression : condition
        | empty
    '''
    pass

def p_condition(t):
    '''
    condition : INT operator INT
    '''
    pass

def p_operator(t):
    '''
    operator : LB
        | RB
        | LB EQUAL
        | RB EQUAL
        | PLUS
        | MINUS
        | EQUAL
        | empty
    '''
    pass

def p_empty(t):
    '''
    empty : 
    '''
    t[0] = ""

def p_error(t):
    if(t):
        print("Error on token '"+t.value+"', line " + str(t.lineno))
    else:
        print("Error on EOF")

parser = yacc.yacc()

data = '''
if(3 <4){}
if(
'''

parser.parse(data)