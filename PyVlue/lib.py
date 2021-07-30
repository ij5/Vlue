from ply import lex

class Lexer(object):
    tokens = [
        'PYTHON',
        'CODE',
    ]

    t_ignore = " \n"

    def t_PYTHON(self, t):
        r'`[^`]+`'
        return t

    def t_CODE(self, t):
        r'.+'
        return t

    def t_error(self, t):
        print("error on token "+t.value)
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

data = '''
var a = $asd;
`asd = 3`
'''

lexer = Lexer()
lexer.test(data)