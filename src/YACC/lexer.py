from ply import lex
import re

tokens = [
    'IF',
    'INT',
    'LSB',
    'RSB',
    'LMB',
    'RMB',
    'LB',
    'RB'
]

t_LSB = r'\('
t_RSB = r'\)'
t_LMB = r'\{'
t_RMB = r'\}'
t_LB = r'\<'
t_RB = r'\>'

def t_IF(t):
    r'if'
    return t

def t_INT(t):
    r'[0-9]+'
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = " \t"

def t_error(t):
    print("Illegal character '{0}' at line {1}".format(t.value[0], t.lineno))
    t.lexer.skip(1)

lexer = lex.lex()