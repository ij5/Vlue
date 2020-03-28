%{
	#include<stdio.h>
	#include<stdlib.h>

	extern void yyerror();
	extern int yylex();
	extern char* yytext;
	extern int yylineno;
%}