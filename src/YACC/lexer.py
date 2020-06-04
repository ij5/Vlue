from ply import lex
import re

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'function': 'FUNCTION',
    'repeat': 'REPEAT',
    'for': 'FOR',
    'while': 'WHILE',
    'in': 'IN',
    'use': 'USE',
    'try': 'TRY',
    'catch': 'CATCH',
    'global': 'GLOBAL',
    'class': 'CLASS',
    'debug': 'DEBUG',
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
    'PYTHON',
    'DOT',
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
t_DOT = r'\.'

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
    r'\[(((\d\.\d)|(\d)|("(?:\\"|.)*?"|\'(?:\\\'|.)*?\'))+(\,+((\d\.\d)|(\d)|("(?:\\"|.)*?"|\'(?:\\\'|.)*?\'))+)+)*\]'
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
    print("Illegal character '{0}' at line {1}".format(t.value[0], t.lineno))
    t.lexer.skip(1)

lexer = lex.lex()