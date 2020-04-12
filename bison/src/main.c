#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int isCutCharacter(char c){
	switch(c){
		case ' ':
		case '=':
			return 1;
		default:
			return 0;
	}
}

int lex(char *s){
	for(int i=0;i<strlen(s);i++){
		if(isCutCharacter(s[i])){
			printf("cut");
		}
	}
}

int main(void){
	char s[] = "var a= 0";
	lex(s);
	printf("done.");
}
