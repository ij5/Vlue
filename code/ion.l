%option noyywrap
%{
	#include<stdio.h>
	#include<string.h>
	#include"ion.tab.h"
	extern int yyerror(char *s);
	int lineno = 1;
%}

newline	[\n]
integer	[0-9]+
variable [a-zA-Z]+[a-zA-Z0-9_]*
whitespace [ \t]

%%


"exit"	{ printf("bye!\n"); exit(0); }
"var"	{ return T_VAR; }
"="		{ return T_EQUAL; }
"if"	{ return T_IF; }
'\('		{ return T_LEFT_SB; }
'\)'		{ return T_RIGHT_SB; }
'\{'	{ return T_LEFT_MB; }
'\}'	{ return T_RIGHT_MB; }
"<"		{ return T_LESS_THAN; }
">"		{ return T_MORE_THAN; }
[a-zA-Z]+[a-zA-Z0-9]*	{ return T_VARIABLE_INDEX; }
[0-9]+ 	{ return T_INT;}

{newline}	{ lineno+=1; return EOL; }
{whitespace}	;

.		;

%%