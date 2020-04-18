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
	'ABBR',
	'ADDRESS',
	'AREA',
	'ARTICLE',
	'ASIDE',
	'AUDIO',
	'B',

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

def t_ABBR(t):
	r'abbr'
	return t

def t_ADDRESS(t):
	r'address'
	return t

def t_AREA(t):
	r'area'
	return t

def t_ARTICLE(t):
	r'article'
	return t

def t_ASIDE(t):
	r'aside'
	return t

def t_AUDIO(t):
	r'audio'
	return t

def t_B(t):
	r'b'
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




