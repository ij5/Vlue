%token INTEGER VARIABLE
%left '+' '-'
%left '*' '/'

%{
  void yyerror(char *);
  int yylex(void);
  int sym[26];
%}

%%

program:
    program statement '\n'
    |
    ;

 /* 변수를 만났을 경우                                */
 /* 변수명의 토큰값을 이용해서 심볼릭 테이블을 만든다 */ 
 /* 만약 변수명이 'a'라면 토큰값은 0이 리턴되고       */
 /* sym[0] 에 연산결과가 들어가게 된다.               */   
statement:
    expr                  { printf("계산결과 %d\n", $1); }
    | VARIABLE '=' expr   { sym[$1] = $3; }
    ;

expr:
    INTEGER
    | VARIABLE            { $$ = sym[$1]; }
    | expr '+' expr       { $$ = $1 + $3; }
    | expr '-' expr       { $$ = $1 - $3; }
    | expr '*' expr       { $$ = $1 * $3; }
    | expr '/' expr       { $$ = $1 / $3; }
    | '(' expr ')'        { $$ = $2; }
    ;

%%
void yyerror(char *s)
{
  printf("%s\n", s);
  return 0;
}

int main(void)
{
  yyparse();
  return 0;
}