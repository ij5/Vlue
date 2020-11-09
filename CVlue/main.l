
%{

#include <stdio.h>
#include <string.h>
#include "main.tab.h"

%%

%option noyywrap


"exit" {
  return T_EXIT;
}

"var" {
  return T_VAR;
}

"function" {
  return T_FUNCTION;
}

[a-zA-Z][a-zA-Z0-9_]* {
  yylval.string = strdup(yytext);
  return T_IDENTIFIER;
}

[0-9]+\.[0-9]+ {
  yylval.fp = atof(yytext);
  return T_FLOAT;
}
 
[0-9]+  {
  yylval.ip = atoi(yytext);
  return T_INT;
}

\+ {
  return T_ADD;
}

\- {
  return T_SUB;
}

\* {
  return T_MUL;
}

\/ {
  return T_DIV;
}

\( {
  return T_LSB;
}

\) {
  return T_RSB;
}

\{ {
  return T_LMB;
}

\} {
  return T_RMB;
}

\, {
  return T_COMMA;
}

\n {
  return T_NEWLINE;
}

\= {
  return T_EQUAL;
}

[ \t\r]   ;

.       yyerror("Invalid character.");
%%

int yywrap(void)
{
  return 1;
}
