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
%token T_IF T_LEFT_PH T_RIGHT_PH T_LEFT_CB T_RIGHT_CB	//if expression
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
	| expression exp EOL
	| expression exp EOL
;

if_expression: 

;

exp: declaration_expression
	| if_expression
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