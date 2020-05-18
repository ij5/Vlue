from ply import lex

tokens = [
    'IDENTIFIER',
    'PYTHON'
]

def t_IDENTIFIER(t):
    r''