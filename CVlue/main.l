
%{
#include <stdlib.h>
void yyerror(char *);
#include "main.tab.h"
%}

%%
 /* 변수명을 위한 VARIABLE 토큰을 되돌려 준다 */
 /* 변수명은 a-z 까지 사용될 수 있다.         */ 
 /* 리턴된 값은 cal.y에서 sym테이블을 만들기 위해서 사용된다. */ 
[a-z]   {
          yylval = *yytext - 'a';
          return VARIABLE;
        }
 
 /* 숫자를 만났을 때 */
[0-9]+  {
          yylval = atoi(yytext);
          return INTEGER;
        }
 /* 연산자를 만났을 때 */
[-+()=/*\n] {return *yytext;}

[ \t]   ;     /* 무시한다 */

.       yyerror("invalid character");
%%

int yywrap(void)
{
  return 1;
}
	