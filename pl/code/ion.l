%{
    #include <string.h>
    #include <stdlib.h>
    // #include "y.tab.h"
    extern int yylex();
    void extern yyerror(char*);
    void InvalidToken();
%}
%option noyywrap

space_required	[ \t]+
space_optional	[ \t]*
eol		\n

%%

"exit"	|
"quit"			{ printf("bye!"); exit(0); }
[0-9]+\.[0-9]+	{ printf("find float"); }
[-+]?[0-9]+			{ printf("find integer"); }
[-+]?[a-zA-Z]+[_0-9a-zA-Z]*		{ printf("found variable");  }

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

int main(void){
	yylex();
	return 0;
}