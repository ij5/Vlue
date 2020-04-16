

from ply import lex

#############
#LEXING
#############

tokens = (
	'HTML',
	'HEAD',
	'BODY',
	'DIV',
	'A',

	'LSB',	#(
	'RSB',	#)
	'LMB',	#{
	'RMB',	#}
	'IDENTIFIER',	#a-z
	'EQUAL',	#=
	'COMMA',	#,
	'OTHER'
	# 'SPACE',
	# 'NEWLINE',
)

t_LSB = r'\('
t_RSB = r'\)'
t_LMB = r'\{'
t_RMB = r'\}'
t_EQUAL = r'\='
t_COMMA = r'\,'
t_IDENTIFIER = r'[a-zA-Z]+'
# t_SPACE = '[ ]+'
t_OTHER = r'.'

def t_HTML(t):
	r'html'
	return t

def t_HEAD(t):
	r'head'
	return t

def t_BODY(t):
	r'body'
	return t

def t_DIV(t):
	r'div'
	return t

def t_A(t):
	r'a'
	return t


def t_NEWLINE(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
	print("error on token %s" % t.value)
	t.lexer.skip(1)

lexer = lex.lex()

data = '''
html(href =https://www.google.com/){
html(){}
}
'''

lexer.input(data)

while True:
	tok = lexer.token()
	if not tok:
		break
	print(tok)




