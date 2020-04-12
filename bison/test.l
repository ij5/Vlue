%option noyywrap
%{
    #include<stdio.h>
    
%}

%%

html    { printf("found html"); }
head    printf("found head");
body    printf("found body");

%%

int main(void){
    yylex();
}