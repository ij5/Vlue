%{
    #include <string.h>
    #include <stdlib.h>
    #include "y.tab.h"
    void extern yyerror(char*);
    void InvalidToken();
%}
%option noyywrap

space_required	[ \t\n]+
space_optional	[ \t\n]*
eol		\n
DIGIT	[0-9]

%%

"exit"	|
"quit"			{ printf("bye!"); exit(0); }
"var"			{ printf("found define"); return T_VAR; }
[0-9]+\.[0-9]+					{ printf("find float"); return T_FLOAT; }
[\-\+]?[0-9]+					{ printf("find integer"); return T_INT; }
[\-\+]?[a-zA-Z]+[_0-9a-zA-Z]*	{ printf("found variable"); return T_VAR_INDEX; }

.			{ InvalidToken(); }

%%

void yyerror(char* s){
	printf("error on line %d: %s", 1, s);
	exit(0);
}

void InvalidToken(){
	printf("Invalid Token on line %d: %s", 1, yytext);
	exit(0);
}

