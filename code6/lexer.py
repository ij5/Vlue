import re
import numpy as np
import ply.lex as lex
import sys

tokens = [
    'TAB',
    'COLON',
    'EQUAL',
    'SPACE'
]

t_COLON = r':'
t_EQUAL = r'='

def t_TAB(t):
    r'\t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Error on token %s" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

lexer.input("a")

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)