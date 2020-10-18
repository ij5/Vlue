%token_type {int}

%left ADD SUB
%left DIV MUL

%include {
    #include <stdio.h>
    #include <stdlib.h>
}

%token_prefix T_

%syntax_error   { error("Invalid Syntax"); }

root ::= expression ';' root.

expression ::= identifier '=' expression
    | term ('+' | '-') term
;

term ::= factor ('*' | '/') factor
;

factor ::= identifier | number | '(' expression ')'
;