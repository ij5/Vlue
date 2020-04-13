from ply import lex

#############
#LEXING
#############

tokens = (
	'LSB',
	'RSB',
	'LMB',
	'RMB',
	'IDENTIFIER',
	'EQUAL',
	'COMMA',
	# 'SPACE',
	'NEWLINE'
)

t_LSB = r'\('
t_RSB = r'\)'
t_LMB = r'\{'
t_RMB = r'\}'
t_EQUAL = r'\='
t_COMMA = r'\,'
t_IDENTIFIER = r'[^\{\}\(\)\=\n ]+'
# t_SPACE = '[ ]+'
# t_CONTENTS = r'[^\{\}]+'

def t_NEWLINE(t):
	r'\n+'
	t.lexer.lineno += len(t.value)
	return t

t_ignore = ' \t'

def t_error(t):
	print("error on token %s" % t.value)
	t.lexer.skip(1)

lexer = lex.lex()

data = '''
{as d...}
'''

# lexer.input(data)
#
# while True:
# 	tok = lexer.token()
# 	if not tok:
# 		break
# 	print(tok)




