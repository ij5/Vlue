%{
void yyerror(char *);
int yylex(void);
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int lineno = 0;

%}

%union{
    long ip;
    float fp;
    char *string;
}

%token T_INT T_IDENTIFIER T_FLOAT 
%token T_ADD T_SUB T_MUL T_DIV
%token T_LSB T_RSB T_LMB T_RMB
%token T_EQUAL T_VAR T_FUNCTION
%token T_NEWLINE
%token T_EXIT
%token T_COMMA

%left T_ADD T_SUB
%left T_MUL T_DIV
%nonassoc T_UMINUS

%type<ip> expression T_INT
%type<fp> expression T_FLOAT
%type<string> expression T_IDENTIFIER

%start program

%%

program: 
    program statement
    |
    ;

statement: 
    expression T_NEWLINE    { 
        lineno++;
        printf("%d\n", $1); 
    }
    | declaration
    | T_EXIT { yyerror("Program exited."); }
    ;

declaration: 
    T_VAR T_IDENTIFIER T_EQUAL expression
    ;

function_declaration:
    T_FUNCTION T_IDENTIFIER T_LSB params T_RSB T_LMB statement T_RMB
;

params: 
    expression
    | params T_COMMA params
;

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