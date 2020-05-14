from ply import lex


############################
#####LEXER
############################

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'function': 'FUNCTION',
    'repeat': 'REPEAT',
    'for': 'FOR',
    'while': 'WHILE',
    'in': 'IN',
    'use': 'USE',
}

tokens = [
    'IDENTIFIER',
    'VAR',
    'EQUAL',
    'INT',
    'FLOAT',
    'STRING',
    'LB',
    'RB',
    'COLON',
    'SEMI',
    'PLUS',
    'MINUS',
    'DIV',
    'MUL',
    'RSB',
    'LSB',
    'RMB',
    'LMB',
    'COMMA',
    'LIST',
] + list(reserved.values())

t_EQUAL = r'='
t_DIV = r'\/'
t_MUL = r'\*'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_LSB = r'\('
t_RSB = r'\)'
t_LMB = r'\{'
t_RMB = r'\}'
t_LB = r'\<'
t_RB = r'\>'
t_COLON = r'\:'
t_SEMI = r'\;'
t_COMMA = r'\,'

t_ignore = ' \t'

def t_VAR(t):
    r'var'
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'("(?:\\"|.)*?"|\'(?:\\\'|.)*?\')'
    t.value = bytes(t.value, "utf-8").decode("unicode_escape")
    return t

def t_LIST(t):
    r'\[((\d\.\d)|(\d)|("(?:\\"|.)*?"|\'(?:\\\'|.)*?\'))+(\,+((\d\.\d)|(\d)|("(?:\\"|.)*?"|\'(?:\\\'|.)*?\'))+)*\]'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_]+[a-zA-Z_0-9]*'
    #if 등 정의
    t.type = reserved.get(t.value, t.type)
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.lexer.linepos = 0
    pass

def t_error(t):
    print("error on token %s" % t.value)
    t.lexer.skip(1)

lexer = lex.lex()

data = '''var a = 4;
var b = 34.88;
var c = a * b;
var d = "Hello World!";
var e = " Hello?";
e = "var";
var str = d+e;
function
repeat
'''

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
print()


###################
#####PARSER
###################

from ply import yacc
import ast
import re
import os

variable = {}
code = "buf___ = 0\n"
state = []
f = []
fi = -1

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MUL', 'DIV'),
    ('right', 'UMINUS')
)


################ ROOT

def p_root(t):
    '''
    root : expression
    '''
    global code
    if(t[1]==None):
        code = code + ""
    else:
        code = code + t[1]

################ EXPRESSION

# EXPRESSION EXPRESSION

def p_expression_variable(t):       #TODO 변수 중복 선언 문제
    '''
    expression : expression variable_declaration SEMI
        | expression variable_value_change SEMI
    '''
    global code
    # if(t[1]==None):
    #     if(t[2]==None):
    #         code = code + ""
    #     else:
    #         code = code + t[2]
    # else:
    #     if(t[2]==None):
    #         code = code + t[1]
    #     else:
    #         code = code + t[2]
    t[0] = t[1] + t[2]

def p_expression_if_statement(t):
    '''
    expression : expression if_statement
    '''
    global code
    # if(t[1]==None):
    #     code = code + t[2]
    # else:
    #     code = code + t[2]
    t[0] = t[1] + t[2]

def p_expression_function(t):
    '''
    expression : expression function
        | expression function_call SEMI
    '''
    t[0] = t[1] + t[2]

def p_expression_repeat(t):
    '''
    expression : expression repeat
    '''
    t[0] = t[1] + t[2]

def p_expression_for(t):
    '''
    expression : expression for
    '''
    t[0] = t[1] + t[2]

def p_expression_while(t):
    '''
    expression : expression while
    '''
    t[0] = t[1] + t[2]

def p_expression_use(t):
    '''
    expression : expression use
    '''
    t[0] = t[1] + t[2]

# EXPRESSION

def p_expression_variable_2(t):       #TODO 변수 중복 선언 문제
    '''
    expression : variable_declaration SEMI
        | variable_value_change SEMI
    '''
    global code
    # if(t[1]==None):
    #     code = code + ""
    # else:
    #     code = code + t[1]
    t[0] = t[1]

def p_expression_if_statement_2(t):
    '''
    expression : if_statement
    '''
    global code
    # code = code + t[1]
    t[0] = t[1]

def p_expression_function_2(t):
    '''
    expression : function
        | function_call
    '''
    t[0] = t[1]

def p_expression_repeat_2(t):
    '''
    expression : repeat
    '''
    t[0] = t[1]

def p_expression_for_2(t):
    '''
    expression : for
    '''
    t[0] = t[1]

def p_expression_while_2(t):
    '''
    expression : while
    '''
    t[0] = t[1]

def p_expression_use_2(t):
    '''
    expression : use
    '''
    t[0] = t[1]

# EMPTY

def p_expression_empty(t):
    '''
    expression : empty
    '''
    global code
    code = code + ""

############### FOR

def p_for(t):
    '''
    for : for_head for_body
    '''
    for_body = re.sub("\n", "\n\t", t[2])
    for_body = for_body[:-1]
    t[0] = t[1] + for_body

def p_for_head(t):
    '''
    for_head : FOR LSB IDENTIFIER IN IDENTIFIER RSB
    '''
    t[0] = "for " + t[3] + " in " + t[5] + ":\n\t"

def p_for_body(t):
    '''
    for_body : LMB expression RMB
    '''
    if(t[2]==None):
        t[0] = "buf___ = 0\n"
    else:
        t[0] = t[2]

############### WHILE

def p_while(t):
    '''
    while : while_head while_body
    '''
    while_body = re.sub("\n", "\n\t", t[2])
    while_body = while_body[:-1]
    t[0] = t[1] + while_body

def p_while_head(t):
    '''
    while_head : WHILE LSB condition RSB
    '''
    t[0] = "while("+t[3]+"):\n\t"

def p_while_body(t):
    '''
    while_body : LMB expression RMB
    '''
    if(t[2]==None):
        t[0] = "buf___ = 0\n"
    else:
        t[0] = t[2]


############### REPEAT

def p_repeat(t):
    '''
    repeat : repeat_head repeat_body
    '''
    repeat_body = re.sub("\n", "\n\t", t[2])
    repeat_body = repeat_body[:-1]
    t[0] = t[1] + repeat_body

def p_repeat_head(t):
    '''
    repeat_head : REPEAT LSB calculate RSB
    '''
    t[0] = "for repeat___ in range(0," + str(t[3]) + "):\n\t"

def p_repeat_body(t):
    '''
    repeat_body : LMB expression RMB
    '''
    if(t[2]==None):
        t[0] = "buf___ = 0\n"
    else:
        t[0] = t[2]

############### FUNCTION

# DECLARATION

def p_function(t):
    '''
    function : function_head function_body
    '''
    function_body = re.sub("\n", "\n\t", t[2])
    function_body = function_body[:-1]
    t[0] = t[1] + ":" + "\n\t" + function_body

def p_function_head(t):
    '''
    function_head : FUNCTION IDENTIFIER LSB empty RSB
        | FUNCTION IDENTIFIER LSB parameter RSB
    '''
    if(t[4]==None):
        t[0] = "def " + t[2] + t[3] + "" + t[5]
    else:
        t[0] = "def " + t[2] + t[3] + t[4] + t[5]

def p_function_body(t):
    '''
    function_body : LMB expression RMB
    '''
    if(t[2]==None):
        t[0] = "buf__ = 0\n"
    else:
        t[0] = t[2]

# CALL

def p_function_call(t):
    '''
    function_call : IDENTIFIER LSB parameter RSB
    '''
    t[0] = t[1] + t[2] + t[3] + t[4] + "\n"

# PARAMETER

def p_parameter(t):
    '''
    parameter : parameter COMMA calculate
    '''
    t[0] = t[1] + t[2]

def p_parameter_2(t):
    '''
    parameter : calculate
        | empty
    '''
    if(t[1]==None):
        t[0] = ""
    else:
        t[0] = t[1]

############### IF STATEMENT

def p_if_statement(t):
    '''
    if_statement : if_statement_1 if_statement_2 if_statement_3
    '''

def p_if_statement_1:
    '''

    '''

def p_if_statement_2:
    '''
    '''

def p_if_statement_3:
    '''

    '''



############ CONDITION

def p_condition(t):
    '''
    condition : condition LB calculate
        | condition RB calculate
    '''
    t[0] = str(t[1]) + t[2] + str(t[3])

def p_condition_2(t):
    '''
    condition : condition LB EQUAL calculate
        | condition RB EQUAL calculate
    '''
    t[0] = str(t[1]) + t[2] + t[3] + str(t[4])

def p_condition_3(t):
    '''
    condition : condition EQUAL calculate
    '''
    t[0] = str(t[1]) + "==" + str(t[3])

def p_condition_4(t):
    '''
    condition : calculate
    '''
    t[0] = t[1]

############## LIBRARY

############### USE

def p_use(t):       #TODO
    '''
    use : USE IDENTIFIER
    '''
    global f
    global fi
    filename = t[2]+".blib"
    if os.path.isfile("./lib/"+filename):
        fi += 1
        f.append(open("./lib/"+filename, 'r', encoding='UTF-8'))
    else:
        error("존재하지 않는 라이브러리입니다.")
    t[0] = ""


############### CHANGE VARIABLE VALUE

def p_variable_value_change_list(t):
    '''
    variable_value_change : IDENTIFIER EQUAL LIST
    '''
    t[0] = t[1] + t[2] + t[3] + "\n"

def p_variable_value_change(t):
    '''
    variable_value_change : IDENTIFIER EQUAL calculate
    '''
    global code
    if variable.get(t[1]):
        variable[t[1]] = t[3]
        t[0] = t[1]+t[2]+str(t[3])+"\n"
    else:
        print(variable)
        error("변수는 선언 후 사용할 수 있습니다.")

# def p_variable_value_change_string(t):
#     '''
#     variable_value_change : IDENTIFIER EQUAL STRING
#     '''
#     global code
#     if variable.get(t[1]):
#         variable[t[1]] = t[3]
#         code = code + '{0} ={1}\n'.format(t[1], t[3])
#     else:
#         error("변수는 선언 후 사용할 수 있습니다.")
#     print(variable)

######### VARIABLE DECLARATION

def p_variable_declaration_list(t):
    '''
    variable_declaration : VAR IDENTIFIER EQUAL LIST
    '''
    t[0] = t[2] + t[3] + t[4] + "\n"

def p_variable_declaration_2(t):
    '''
    variable_declaration : VAR IDENTIFIER EQUAL calculate
    '''
    global code
    variable[t[2]] = t[4]
    t[0] = t[2] + t[3] + str(t[4])+"\n"

# def p_variable_declaration_2_string(t):
#     '''
#     variable_declaration : VAR IDENTIFIER EQUAL STRING
#     '''
#     global code
#     variable[t[2]] = t[4]
#     code = code + '{0} = {1}\n'.format(t[2], t[4])

def p_variable_declaration_1(t):
    '''
    variable_declaration : VAR IDENTIFIER
    '''
    global code
    t[0] = t[1] + " = 0"
    variable[t[2]] = 0

########### STRING

# def p_string_plus(t):       #TODO 문자열 오류
#     '''
#     string_plus : string_plus PLUS STRING
#     '''
#     global code
#     t[0] = t[1] + t[3]
#
# def p_string_plus_2(t):     #TODO 문자열 오류 2
#     '''
#     string_plus : STRING
#     '''
#     t[0] = t[1]
#
# def p_string_plus_3(t):
#     '''
#     string_plus : IDENTIFIER
#     '''

######### CALCULATE

def p_add(t):   #TODO add error
    'calculate : calculate PLUS calculate'
    try:
        if(t[1].startswith('"')):
            if(t[3].startswith('"')):
                t[0] = t[1][:-1] + t[3][1:]
            elif(t[3].startswith("'")):
                t[0] = t[1][:-1] + t[3][1:-1]+'"'
        elif(t[1].startswith("'")):
            if(t[3].startswith('"')):
                t[0] = t[1][:-1] + t[3][1:-1]+"'"
            elif(t[3].startswith("'")):
                t[0] = t[1][:-1] + t[3][1:]
        else:
            if(isinstance(t[1], str)):
                if(isinstance(t[3], str)):
                    t[0] = t[1] + t[3]
                else:
                    t[0] = t[1] + "+" + str(t[3])
            else:
                if(isinstance(t[3], str)):
                    t[0] = str(t[1]) + "+" + t[3]
                else:
                    t[0] = t[1] + t[3]
    except AttributeError:
        if (isinstance(t[1], str)):
            if (isinstance(t[3], str)):
                t[0] = t[1] + t[3]
            else:
                t[0] = t[1] + "+" + str(t[3])
        else:
            if (isinstance(t[3], str)):
                t[0] = str(t[1]) + "+" + t[3]
            else:
                t[0] = t[1] + t[3]

def p_sub(t):
    'calculate : calculate MINUS calculate'
    t[0] = t[1] - t[3]

def p_calculate2uminus(t):
    'calculate : MINUS calculate %prec UMINUS'
    t[0] = - t[2]

def p_mul_div(t):
    '''
    calculate : calculate MUL calculate
        | calculate DIV calculate
    '''
    if(t[2]=='*'):
        t[0] = t[1] * t[3]
    else:
        if(t[3]==0):
            error("0으로 나눌 수 없습니다.")
        t[0] = t[1] / t[3]

def p_calculate2num(t):
    '''
    calculate : INT
        | FLOAT
        | STRING
    '''
    t[0] = t[1]

def p_calculate2str(t):
    '''
    calculate : IDENTIFIER
    '''
    try:
        t[0] = t[1]
    except LookupError:
        error("Unknown variable "+t[1])

def p_parens(t):
    'calculate : LSB calculate RSB'
    t[0] = t[2]

############ CALCULATE END

def p_empty(t):
    'empty : '
    pass

# 토큰 에러 처리
def p_error(t):
    if(t):
        print("Error on token '"+t.value+"', line " + str(t.lineno))
    else:
        print("Error on EOF")

# 에러 처리
def error(s):
    print(s)
    exit(-1)

parser = yacc.yacc()

data = """
var a = 3;
var b = 2;
if(a<b){
    a = b;
}else{
a=b;
}

function fn(){}
var c = 5;
repeat(5){
c = c + 1;
}
c = [1,2,"3",5.6,76];

for(i in c){
    c = 4+5+6;
}

while(c<9){
    c = 5;
    c = c+1;
}

fn();

use test

"""
# while True:
#     buf = input(">>> ")
#     if(buf=="exit"):
#         break
#     data = data+buf

result = parser.parse(data)
print(variable)
print(code)
exec(code)