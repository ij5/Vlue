from ply import lex

#############
#LEXING
#############

tokens = (
	'HTML',
	'LSB',	#(
	'RSB',	#)
	'LMB',	#{
	'RMB',	#}
	'IDENTIFIER',	#a-z
	'EQUAL',	#=
	'COMMA',	#,
	# 'SPACE',
	# 'NEWLINE',
	'CONTENTS',	#other
	'NONE'
)

t_LSB = r'\('
t_RSB = r'\)'
t_LMB = r'\{'
t_RMB = r'\}'
t_EQUAL = r'\='
t_COMMA = r'\,'
t_IDENTIFIER = r'[a-zA-Z]+'
# t_SPACE = '[ ]+'
t_HTML = r'html'

def t_NEWLINE(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
	print("error on token %s" % t.value)
	t.lexer.skip(1)

lexer = lex.lex()

data = '''
html(){
    head(){
    
    }
    body(){
        div(class=mainContent, id=mainContent){
            button(class=mainButton){Press me!}
            a(href=https://google.com,class=mainlink){Click me!}
        }
    }
}
'''

lexer.input(data)

while True:
	tok = lexer.token()
	if not tok:
		break
	print(tok)




