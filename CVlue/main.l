
%{
// #include <stdlib.h>
// #include <stdio.h>
void yyerror(char *);
#include "main.tab.h"
%}

%%


"exit" {
  return T_EXIT;
}

"var" {
  strcpy(yylval, yytext);
  return T_VAR;
}

[a-zA-Z][a-zA-Z0-9_]* {
  strcpy(yylval, yytext);
  return T_IDENTIFIER;
}
 
[0-9]+  {
  yylval = atoi(yytext);
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
