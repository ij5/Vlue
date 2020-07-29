from ast import *

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
        'OTHER'
    ]

    t_ignore = ' \t'

    def t_IDENTIFIER(self, t):
        r'[a-zA-Z_]+'
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

    def t_OTHER(self, t):
        r'.+'
        return t

    def t_NEWLINE(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        t.lexer.linepos = 0
        pass

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
import os

code = "buf___ = 0\n"
variable = {}
state = []
f = []
debug = False

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MUL', 'DIV'),
    ('nonassoc', 'UMINUS')
)


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


class HTMLParser(object):
    tokens = Lexer.tokens
    precedence = precedence
    debug = False

    ##################### PROGRAM

    def p_program(self, t):
        '''
        program : root
        '''

        ##################### ROOT

    def p_root(self, t):
        '''
        root : root expression
            | expression
            | other
            | empty
        '''

    def p_expression(self, t):
        '''expression : IDENTIFIER lSB parameter RSB LMB root RMB'''

    def p_parameter(self, t):
        '''parameter : parameter '''

    def p_other(self, t):
        '''
        other : other other
            | OTHER
            | IDENTIFIER
            | LSB
            | RSB
        '''

    ############ EMPTY

    def p_empty(self, t):
        'empty : '
        t[0] = BaseNode()
        t[0].VALUE = None
        t[0].TYPE = "EMPTY"

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

testcode = '''
html(){
asdf3
}
'''

l = Lexer()
l.test(testcode)