from ply import yacc

from lexer import tokens

def p_statement(t):
    '''
    statement : expression
        | if_statement
    '''
    print("Hello")

def p_if_statement(t):
    '''
    if_statement : IF LSB expression RSB LMB statement RMB
    '''

def p_expression(t):
    '''
    expression : condition
        | empty
    '''

def p_condition(t):
    '''
    condition : INT operator INT
    '''

def p_operator(t):
    '''
    operator : LB
        | RB
    '''

def p_empty(t):
    '''
    empty : 
    '''

def p_error(t):
    print("error on token "+t.value)
    exit(1)

parser = yacc.yacc()

data = '''
if(3 <4){}
'''

parser.parse(data)