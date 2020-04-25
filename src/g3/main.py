from ply import lex


############################
#####LEXER
############################

tokens = (
    'IDENTIFIER',
    'VAR',
    'EQUAL',
    'INT',
    'TAB',
    'NEWLINE'
)

t_EQUAL = r'='

t_ignore = ' '

def t_VAR(t):
    r'var'
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_]+[a-zA-Z_0-9]*'
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.lexer.linepos = 0
    return t

def t_error(t):
    print("error on token %s" % t.value)
    t.lexer.skip(1)

lexer = lex.lex()

data = "var asd = 5"

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)


###################
#####PARSER
###################

from ply import yacc

varname = []
varval = []

def p_expression(t):
    'expression : variable_declaration'

def p_variable_declaration_2(t):
    'variable_declaration : VAR IDENTIFIER EQUAL INT'


def p_variable_declaration_1(t):
    'variable_declaration : VAR IDENTIFIER'
    if t[2] in varname:
        error('변수는 중복 선언할 수 없습니다.')
    else:
        varname.append(t[1])
        varval.append(1)

def p_error(t):
    if(t):
        print("Error on token '%s'" % t.value)
    else:
        print("Error on EOF")

def error(s):
    print(s)
    exit()

parser = yacc.yacc()

data = "var asd"

result = parser.parse(data)