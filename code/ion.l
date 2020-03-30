%option noyywrap
%{
	#include<stdio.h>
	#include"ion.tab.h"
	extern int yyerror(char *s);
	int lineno = 1;
%}

newline	[\n]

%%

[ \t]+	{ return space_required; }
[ \t]*	{ return space_optional; }
"exit"	{ printf("bye!\n"); exit(0); }
"var"	{ return T_VAR; }
{newline}	{ lineno+=1; }

%%