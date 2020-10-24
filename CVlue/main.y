%{
void yyerror(char *);
int yylex(void);

#include "node.h"

int lineno = 0;

%}

%token T_INT T_IDENTIFIER 
%token T_ADD T_SUB T_MUL T_DIV
%token T_LSB T_RSB
%token T_EQUAL T_VAR
%token T_NEWLINE
%token T_EXIT

%left T_ADD T_SUB
%left T_MUL T_DIV
%nonassoc T_UMINUS


%%

program: 
    program statement
    |
    ;

statement: 
    expression NEWLINE    { 
        lineno++;
        printf("%d\n", $1); 
    }
    | declaration
    | T_EXIT { exit(0); }
    ;

declaration: 
    T_VAR T_IDENTIFIER T_EQUAL expression   

expression: 
    T_INT     { $$ = $1; }
    | T_IDENTIFIER            { $$ = $1; }
    | expression T_ADD expression       { $$ = $1 + $3; }
    | expression T_SUB expression       { $$ = $1 - $3; }
    | expression T_MUL expression       { $$ = $1 * $3; }
    | expression T_DIV expression       { $$ = $1 / $3; }
    | T_SUB expression %prec T_UMINUS     { $$ = -$2; }
    | T_LSB expression T_RSB        { $$ = $2; }
    ;

%%
void yyerror(char *s)
{
    printf("%s\n", s);
}

int main(void)
{
// #ifdef YYDEBUG
//     yydebug = 1;
// #endif
    yyparse();
    return 0;
}