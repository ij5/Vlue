from ply import lex
from ply import yacc

data = '''
    'print' LSB RSB `print("Hello")`
    IDENTIFIER RSB LSB `print("HLO")`
'''

tokens = [
    'IDENTIFIER',
    'PYTHON',
    'STRING'
]

def t_IDENTIFIER(t):
    r'[a-zA-Z_]+[a-zA-Z_0-9]*'
    return t

def t_STRING(t):
    r'\'[^\']+\''
    return t

def t_PYTHON(t):
    r'`[^`]*`'
    return t

def t_error(t):
    print("error on token %s" % t.value)
    t.lexer.skip(1)

t_ignore = " \t\n"

lexer = lex.lex()

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
print()


pythoncommand = []
grammar = ""
string = {}
PYTHON = "PYTHON"

def p_root(t):
    '''
    root : expression
    '''
    pass

def p_expression(t):
    '''
    expression : identifier PYTHON
    '''
    t[0] = t[1] + t[2]
    global pythoncommand
    global grammar
    pythoncommand.append(t[2])
    if (grammar == ""):
        grammar = grammar + t[1]
    else:
        grammar = grammar + " | " + t[1]

def p_expression_2(t):
    '''
    expression : expression identifier PYTHON
    '''
    t[0] = t[1] + t[2] + t[3]
    global pythoncommand
    global grammar
    pythoncommand.append(t[3])
    if (grammar == ""):
        grammar = grammar + t[1]
    else:
        grammar = grammar + " | " + t[2]

def p_identifier(t):
    '''
    identifier : identifier IDENTIFIER
    '''
    t[0] = t[1] + " " + t[2]

def p_identifier_string(t):
    '''
    identifier : identifier STRING
    '''
    global string
    t[0] = t[1] + " " + t[2][1:-1].upper()
    string[t[2]] = t[2].upper()

def p_identifier_2(t):
    '''
    identifier : IDENTIFIER
    '''
    t[0] = t[1]

def p_identifier_string_2(t):
    '''
    identifier : STRING
    '''
    global string
    t[0] = t[1][1:-1].upper()
    string[t[1]] = t[1].upper()

def p_error(t):
    if (t):
        print("Error on token '" + t.value + "', line " + str(t.lineno))
    else:
        print("Error on EOF")

def parse(data):
    global pythoncommand
    global grammar
    parser = yacc.yacc()
    parser.parse(data)
    print(pythoncommand)
    print(grammar)

def getpythoncommand():
    global pythoncommand
    return pythoncommand

def getstring():
    global string
    return string

def getgrammar():
    global grammar
    return grammar
parse(data)