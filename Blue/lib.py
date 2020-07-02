from ply import lex

class Lexer(object):
    tokens = [
        'PYTHON',
        'CODE',
    ]

    def t_CODE(self, t):
        pass

    def t_PYTHON(self, t):
        r'`[^`]+`'
        return t