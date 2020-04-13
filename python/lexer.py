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
	'CONTENTS',
	'COMMA'
)

t_LSB = r'\('
t_RSB = r'\)'
t_LMB = r'\{'
t_RMB = r'\}'
t_EQUAL = r'\='
t_COMMA = r'\,'
t_CONTENTS = r'.'

def t_IDENTIFIER(t):
	r'[a-zA-Z]+'
	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
	print("error on token %s" % t.value)
	t.lexer.skip(1)

lexer = lex.lex()

data = '''
html(){
	head%(){}
	body(a=asd){
		Hello World!
		div(){
		
		}
	}	
}
'''

# lexer.input(data)
#
# while True:
# 	tok = lexer.token()
# 	if not tok:
# 		break
# 	print(tok)




