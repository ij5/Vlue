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

%token	T_VAR T_FLOAT T_INT T_DEF

%token <int_val> T_INT


%%

define_expression: define_variable variable_value	{ }

variable_value: T_VAR	{$$=$1}	

define_variable: T_DEF

%%

int main(void){
	yyparse();
	printf("no erros");
	return 0;
}