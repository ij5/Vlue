from sly import Lexer
import .errors

class BLUELexer(Lexer):
    # 토큰 정의
    tokens = {
        'PRINT', 'IF', 'ELSE', 'FUNCTION', 'RETURN', 'WHILE', 'VAR',
        'IDENTIFIER',
        'INT', 'FLOAT', 'STRING', 'BOOL',
        'PLUS', 'MINUS', 'MUL', 'DIV', 'SEMI', 'COMMA', 'DOT'
        'EQUAL', 'LT', 'LE', 'GT', 'GE', 'OR', 'NOT',
        'LB', 'RB', 'LSB', 'RSB', 'LMB', 'RMB'
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

    def error(self, t):
        error(self.lineno, "Illegal character %r" % t.value[0])
        self.index += 1