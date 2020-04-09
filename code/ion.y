%{
	#include<stdio.h>
	#include<stdlib.h>
	#include<string.h>
	extern int yyparse();
	extern void yyerror(char *s);
	extern int yylex();
	extern int lineno;
	extern FILE* yyin;
%}

%union{
	int int_val;
	char* variable_index;
}

%token T_VAR T_EQUAL //declaration expression
%token T_IF T_LEFT_SB T_RIGHT_SB T_LEFT_MB T_RIGHT_MB T_MORE_THAN T_LESS_THAN	//if expression
%token EOL	//End of line
%token <int_val> T_INT	//type declaration
%token <variable_index> T_VARIABLE_INDEX	// variable index. 	ex) var (a) = 1

%right '='
%left '+' '-'
%left '*' '/'
%left '!'

%start expression

%%

expression: 
	| expression declaration_expression EOL
	| expression if_expression EOL
;

if_expression: T_IF T_LEFT_SB condition_expression T_RIGHT_SB
	| T_IF T_LEFT_SB condition_expression T_RIGHT_SB T_LEFT_MB expression T_RIGHT_MB
;

condition_expression: T_INT T_MORE_THAN T_INT
	| T_INT T_MORE_THAN T_VARIABLE_INDEX
	| T_VARIABLE_INDEX T_MORE_THAN T_INT
	| T_VARIABLE_INDEX T_MORE_THAN T_VARIABLE_INDEX

	| T_INT T_LESS_THAN T_INT
	| T_INT T_LESS_THAN T_VARIABLE_INDEX
	| T_VARIABLE_INDEX T_LESS_THAN T_INT
	| T_VARIABLE_INDEX T_LESS_THAN T_VARIABLE_INDEX
;

declaration_expression: T_VAR T_VARIABLE_INDEX T_EQUAL T_INT 	{ printf("found variable declaration.\n"); }
	| T_VAR T_VARIABLE_INDEX 	{ printf("found variable\n"); }
;

%%

int main(void){
	printf("version 5\n");
	yyin=stdin;
	do{
		yyparse();
	}while(!feof(yyin));

	return 0;
}


void yyerror(char *s){
	fprintf(stderr, "error on line %d: %s\n", lineno, s);
	exit(1);
}