from sly import Lexer
from errors import error

class BLUELexer(Lexer):
    # 토큰 정의
    tokens = {
        'PRINT', 'IF', 'ELSE', 'FUNCTION', 'RETURN', 'WHILE', 'VAR',
        'IDENTIFIER',
        'INT', 'FLOAT', 'STRING', 'BOOL',
        'PLUS', 'MINUS', 'MUL', 'DIV', 'SEMI', 'COMMA', 'DOT',
        'EQUAL', 'OR', 'NOT','AND',
        'LB', 'RB', 'LSB', 'RSB', 'LMB', 'RMB', 'LBB', 'RBB'
    }
    # 무시하는 문자 지정
    ignore = " \t\r"

    # 주석 처리
    @_(r'/\*(.|\n)*?\*/')
    def COMMENT_1(self, token):
        self.lineno += token.value.count('\n')
        return None

    @_(r'//.*')
    def COMMENT_2(self, token):
        self.lineno += token.value.count('\n')

    @_(r'\n+')
    def NEWLINE(self, token):
        self.lineno += token.value.count('\n')

    PLUS = r'\+'
    MINUS = r'\-'
    MUL = r'\*'
    DIV = r'\/'
    SEMI = r'\;'
    COMMA = r'\,'
    DOT = r'\.'
    EQUAL = r'\='
    OR = r'\|\|'
    AND = r'&&'
    NOT = r'!'
    LB = r'<'
    RB = r'>'
    LSB = r'\('
    RSB = r'\)'
    LMB = r'\{'
    RMB = r'\}'
    LBB = r'\['
    RBB = r'\]'
    FLOAT = r'(((\d+\.\d*)|(\.\d+))([eE][+-]?\d+)?)|(\d+[eE][+-]?\d+)'
    INT = r'(0x[0-9ABCDEF]+)|(0b[01]+)|(0o[0-5]+)|\d+'
    STRING = r'("(?:\\"|.)*?"|\'(?:\\\'|.)*?\')'
    BOOL = r'(true)|(false)'

    @_(r'[a-zA-Z_][a-zA-Z0-9_]*')
    def IDENTIFIER(self, t):
        keywords = {
            'else',
            'if',
            'function',
            'return',
            'print',
            'while',
            'var'
        }
        if t.value in keywords:
            t.type = t.value.upper()
        return t

    def error(self, t):
        error(self.lineno, "Illegal character %r" % t.value[0])
        self.index += 1


def main():
    import sys
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: python3 -m BLUE.lexer filename\n")
        raise SystemExit(1)

    lexer = BLUELexer()
    data = open(sys.argv[1]).read()
    for token in lexer.tokenize(data):
        print(token)

if __name__ == '__main__':
    main()