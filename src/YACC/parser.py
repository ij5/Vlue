from sly import Parser
from lexer import BLUELexer

class BLUEParser(Parser):
    tokens = BLUELexer.tokens

    precedence = (
        ('left', 'AND', 'NOT'),
        ('nonassoc', 'LBB', 'RBB'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'MUL', 'DIV'),
        ('right', 'UNARY')
    )

    @_('statement')
    def root(self, p):
        