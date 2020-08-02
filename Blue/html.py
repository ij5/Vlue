
############################
#####LEXER
############################

from ply import lex


class Lexer(object):

    tokens = [
        'IDENTIFIER',
        'LSB',
        'LMB',
        'RSB',
        'RMB',
        'COMMA',
        'OTHER',
        'EQUAL',
        'STRING',
        'BLUE',
    ]

    t_ignore = ' \t'

    def t_BLUE(self, t):
        r'\<\?(?:\\"|.)*?\?\>'
        return t

    def t_IDENTIFIER(self, t):
        r'[a-zA-Z0-9ㄱ-ㅎㅏ-ㅣ가-힣_]+[a-zA-Z0-9ㄱ-ㅎㅏ-ㅣ가-힣_]*'
        return t

    def t_LSB(self, t):
        r'\('
        return t

    def t_LMB(self, t):
        r'\{'
        return t

    def t_RSB(self, t):
        r'\)'
        return t

    def t_RMB(self, t):
        r'\}'
        return t

    def t_COMMA(self, t):
        r','
        return t

    def t_STRING(self, t):
        r'("(?:\\"|.)*?"|\'(?:\\\'|.)*?\')'
        t.value = bytes(t.value, "utf-8").decode("unicode_escape")
        return t

    def t_EQUAL(self, t):
        r'='
        return t

    def t_NEWLINE(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        t.lexer.linepos = 0
        pass

    def t_OTHER(self, t):
        r'[^\{\}]+'
        return t

    def t_error(self, t):
        print("error on token %s" % t.value)
        t.lexer.skip(1)

    def __init__(self):
        self.lexer = lex.lex(module=self)

    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)


# data = '''
# if(a<b){
#     a = b;
# }else{
# a = b;
# }
# '''
#
# lexer.input(data)

# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)
# print()


###################
#####PARSER
###################

from ply import yacc
import re
from InsideHTML import ElementaryParser

def DecodeEscape(s):
    res = ''
    i = iter(s)
    for c in i:
        if c == '\\':
            c = next(i)
            if c == 'n':
                res += '\n'
            elif c == 'r':
                res += '\r'
            elif c == 't':
                res += '\t'
            elif c == '"':
                res += '"'
            elif c == "'":
                res += "'"
            elif c == 'x':
                try:
                    x = next(i)
                except StopIteration:
                    res += "\\x"
                    break
                try:
                    x += next(i)
                except StopIteration:
                    pass
                try:
                    x = int(x, 16)
                    res += chr(x)
                except ValueError:
                    res += '\\x' + x
            elif c == '\\':
                res += '\\'
            else:
                res += c
        else:
            res += c
    return res


class BaseNode():
    def __init__(self, VALUE=None, RETURN=None):
        self.VALUE = VALUE
        self.RETURN = RETURN


namespace = []


def flatten(listdata):
    return listdata[0]


def lookup(s, lookups):
    for pattern, value in lookups:
        if re.search(pattern, s):
            return value
    return None


def get_value(dic):
    try:
        return next(iter(dic.values()))
    except StopIteration:
        return None

from io import StringIO
import contextlib
import sys
from astor import code_gen

@contextlib.contextmanager
def StdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


'''
program : root

root : root root
    | expression
    
expression : identifier LSB parameter RSB LMB root RMB

parameter : parameter COMMA parameter
    | identifier EQUAL string
    
    
identifier : identifier identifier
    | BLUE
    | IDENTIFIER
    
string : STRING
'''

class HTMLParser(object):
    tokens = Lexer.tokens
    debug = False

    ##################### PROGRAM

    def p_program(self, t):
        '''
        program : root
        '''
        t[0] = t[1]

    ##################### ROOT

    def p_root(self, t):
        '''
        root : root root
            | expression
        '''


    def p_expression(self, t):
        '''expression : IDENTIFIER LSB parameter RSB LMB root RMB'''

    def p_parameter(self, t):
        '''parameter : parameter COMMA parameter'''

    def p_parameter_2(self, t):
        '''parameter : i_b EQUAL i_b'''

    def p_i_b(self, t):
        '''
        i_b : IDENTIFIER
            | BLUE
        '''


    #
    # def p_root(self, t):
    #     '''
    #     root : root root
    #         | expression
    #         | other
    #         | empty
    #     '''
    #     if(len(t)==3):
    #         t[0] = t[1] + t[2]
    #     else:
    #         t[0] = t[1]
    #
    # def p_expression(self, t):
    #     '''expression : IDENTIFIER LSB parameter RSB LMB root RMB'''
    #     if(t[3]==""):
    #         t[0] = "<" + t[1] + "" + t[3] + ">" + t[6] + "</" + t[1] + ">"
    #     else:
    #         t[0] = "<" + t[1] + " " + t[3] + ">" + t[6] + "</" + t[1] + ">"
    #
    # def p_parameter(self, t):
    #     '''
    #     parameter : parameter COMMA parameter
    #         | empty
    #     '''
    #     if(len(t)==2):
    #         t[0] = ""
    #     else:
    #         t[0] = t[1] + " " + t[3]
    #
    # def p_parameter_2(self, t):
    #     '''parameter : IDENTIFIER EQUAL STRING'''
    #     t[0] = t[1] + t[2] + '"' + t[3][1:-1] + '"'
    #
    # def p_other(self, t):
    #     '''
    #     other : other other
    #         | OTHER
    #         | IDENTIFIER
    #         | LSB
    #         | RSB
    #         | STRING
    #     '''
    #     if(len(t)==3):
    #         t[0] = t[1] +" " + t[2]
    #     else:
    #         t[0] = t[1]

    def p_other_2(self, t):
        '''other : BLUE'''
        parser = ElementaryParser()
        result = parser.parser.parse(t[1][2:-2])
        result = code_gen.to_source(result.VALUE)
        with StdoutIO() as s:
            exec(result)
        t[0] = s.getvalue()

    ############ EMPTY

    def p_empty(self, t):
        'empty : '
        t[0] = ""

    # 토큰 에러 처리
    def p_error(self, t):
        if (t):
            print("Error on token '" + str(t.value) + "', line " + str(t.lineno))
        else:
            print("Error on EOF")

    def __init__(self):
        self.lexer = Lexer()
        self.parser = yacc.yacc(module=self)


def error(s):
    print(s)
    exit(-1)


lexer = Lexer()
lexer.test(''' "<??>" ''')
