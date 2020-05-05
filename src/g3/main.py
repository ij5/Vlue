from ply import lex


############################
#####LEXER
############################

reserved = {
    'if': 'IF',
    'else': 'ELSE',
}

tokens = [
    'IDENTIFIER',
    'VAR',
    'EQUAL',
    'INT',
    'FLOAT',
    'STRING',
    'IF',
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

t_ignore = ' \t'

def t_IF(t):
    r'if'
    return t

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

def t_IDENTIFIER(t):
    r'[a-zA-Z_]+[a-zA-Z_0-9]*'
    #if 등 정의
    t.type = reserved.get(t.value, t.type)
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.lexer.linepos = 0

def t_error(t):
    print("error on token %s" % t.value)
    t.lexer.skip(1)

lexer = lex.lex()

data = '''var a = 4;
var b = 34.88;
var c = a * b;
var d = "Hello World!";
var e = " Hello?";
e = "Hello";
var str = d+e;'''

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

variable = {}
code = ""

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MUL', 'DIV'),
    ('right', 'UMINUS')
)


################EXPRESSION

def p_expression(t):
    '''
    expression : expression variable_declaration SEMI
        | expression variable_value_change SEMI
    '''
    global code
    if(t[1]==None):
        if(t[2]==None):
            code = code + ""
        else:
            code = code + t[2]
    else:
        if(t[2]==None):
            code = code + t[1]
        else:
            code = code + t[1] + t[2]

def p_expression_if(t):
    '''
    expression : expression if_statement
    '''
    global code
    if(t[1]==None):
        code = code + t[2]
    else:
        code = code + t[1] + t[2]

def p_expression_2(t):
    '''
    expression : variable_declaration SEMI
        | variable_value_change SEMI
    '''
    global code
    if(t[1]==None):
        code = code + ""
    else:
        code = code + t[1]

def p_expression_2_if(t):
    '''
    expression : if_statement
    '''
    global code
    code = code + t[1]

def p_expression_empty(t):
    '''
    expression : empty
    '''
    global code
    code = code + ""


###############IF STATEMENT

def p_if_statement(t):      #TODO if expression tab problem
    '''
    if_statement : if_statement_head if_statement_body
    '''
    if_statement_body = re.sub("\n", "\n\t", t[2])
    t[0] = t[1] + ":" + "\n" + if_statement_body
    print(if_statement_body)

def p_if_statement_head(t):
    '''
    if_statement_head : IF LSB condition RSB
    '''
    t[0] = t[1] + t[2] + t[3] + t[4]

def p_if_statement_body(t):
    '''
    if_statement_body : LMB expression RMB
    '''
    if(t[2]==None):
        t[0] = ""
    else:
        t[0] = t[2]

############CONDITION

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
    t[0] = t[1] + t[2] + t[3] + t[4]

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

#########CHANGE VARIABLE VALUE
def p_variable_value_change(t):
    '''
    variable_value_change : IDENTIFIER EQUAL calculate
    '''
    global code
    if variable.get(t[1]):
        variable[t[1]] = t[3]
    else:
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

#########VARIABLE DECLARATION

def p_variable_declaration_2(t):
    '''
    variable_declaration : VAR IDENTIFIER EQUAL calculate
    '''
    global code
    variable[t[2]] = t[4]
    code = code + "{0} = {1}\n".format(t[2], t[4])

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
    code = code + "{0} = 0\n".format(t[2])
    variable[t[2]] = 0

###########STRING

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

#########CALCULATE

def p_add(t):
    'calculate : calculate PLUS calculate'
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
        t[0] = variable[t[1]]
    except LookupError:
        error("Unknown variable "+t[1])

def p_parens(t):
    'calculate : LSB calculate RSB'
    t[0] = t[2]

############CALCULATE END

def p_empty(t):
    'empty : '
    pass

#토큰 에러 처리
def p_error(t):
    if(t):
        print("Error on token '%s'" % t.value)
    else:
        print("Error on EOF")

#에러 처리
def error(s):
    print(s)
    exit(-1)

parser = yacc.yacc()

data = """
var a = "Hello World!";
var b = "Hello";
if(a>b){
a = "hello world!";
}
"""
# while True:
#     buf = input(">>> ")
#     if(buf=="exit"):
#         break
#     data = data+buf

result = parser.parse(data)
print(variable)
print(code)