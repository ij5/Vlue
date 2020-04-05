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

%token T_VAR T_EQUAL EOL
%token <int_val> T_INT
%token <variable_index> T_VARIABLE_INDEX
%token space_optional space_required

%start root

%%

root: 
	|	root line
;

line: EOL
	|	declaration_expression
;

declaration_expression: T_VAR T_VARIABLE_INDEX T_EQUAL T_INT { printf("Find integer declaration on line %d\n", lineno); }
	|	T_VAR T_VARIABLE_INDEX { printf("Find declaration on line %d\n", lineno); /*TODO 이 문장 출력이 한 턴 늦음.*/ }
;

%%

void yyerror(char *s){
	fprintf(stderr, "error on line %d: %s\n", lineno, s);
	exit(1);
}

int main(void){
	printf("version 4\n");

	yyin=stdin;
	do{
		yyparse();
	}while(!feof(yyin));

	return 0;
}