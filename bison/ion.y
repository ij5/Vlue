%{
	#include <stdio.h>
	#include<stdlib.h>

	extern int yylex();
	extern int yyparse();
	extern FILE* yyin;

	void yyerror(const char *s);
%}

%union{

}

%token T_EQUAL T_COLON T_TAB T_OTH

%start root

%%

root: 
	| expr
;
expr: T_EQUAL T_COLON	{ printf("T_EQUAL T_COLON"); }
;

%%

int main(){
	yyin = stdin;
	yyparse();
	return 0;
}

void yyerror(const char* s){
	fprintf(stderr, "Error: %s", s);
	exit(1);
}