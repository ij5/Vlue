%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "node.h"


%}

%token T_EXIT
%token T_VAR
%token T_FUNCTION
%token T_IDENTIFIER
%token T_FLOAT
%token T_INT
%token T_ADD
%token T_SUB
%token T_MUL
%token T_DIV
%token 

%right THEN
%right ELSE

%union {
    double val;
    Node *node;
    char str[100];
}

%type <node> program
%type <node> statements
%type <node> statement
%type <node> if_statement

%%

program: statements {}
;

statement: if_statement { $$ = $1; }
;

if_statement: IF LSB expression RSB LMB