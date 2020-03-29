%{
	#include<stdio.h>
	#include<stdlib.h>

	extern void yyerror();
	extern int yylex();
	extern char* yytext;
	extern int yylineno;
%}

%union{
	int int_val;
	char* datatype;
}

%token	T_VAR T_VAR_INDEX T_FLOAT T_INT

%token <int_val> T_INT


%%

declaration_expression: T_VAR T_VAR_INDEX	{ }

%%

int main(void){
	yyparse();
	printf("no erros");
	return 0;
}