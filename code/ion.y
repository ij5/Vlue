%{
	#include<stdio.h>
	extern int yyparse();
	extern void yyerror(char *s);
	extern int yylex();
	extern int lineno;
%}

%token T_VAR EOL
%token space_optional space_required

%%

expression: T_VAR {printf("Find variable on line %d", lineno); }

%%

void yyerror(char *s){
	printf("error on line %d: %s\n", lineno, s);
}

int main(void){
	yyparse();
}