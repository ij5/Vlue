%option noyywrap
%{
	#include<stdio.h>
	#define YY_DECL int yylex()
	#include "ion.tab.h"
%}

%%

"="		{ return T_EQUAL; }
":"		{ return T_COLON; }
"("		{ return T_LEFT_SB; }
")"		{ return T_RIGHT_SB; }
"{"		{ return T_LEFT_MB; }
"}"		{ return T_RIGHT_MB; }

[ \t\r\v\f]		;
.		{ return T_OTH; }

%%