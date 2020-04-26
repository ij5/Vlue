from ply import lex

tokens = (
    'TAB',
    'SPACE'
)

lexer = lex.lex()

lexer.input(data)

while True:
	tok = lexer.token()
	if not tok:
		break
	print(tok)

print()