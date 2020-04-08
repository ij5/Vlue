#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int *tokens[128];
int tokensArrSize = 0;

void push(int tk){
    tokens[tokensArrSize] = tk;
    tokensArrSize+=1;
    printf(tk);
};

enum TokenType{
    T_VAR = 1,
    T_INT,
    T_EQUAL,
    T_SPACE
}token;

struct Token{
    char* str;
    enum TokenType type;
    int line;
};

int isCutCharacter(char c){
    switch (c){
        case ' ':
        case '=':
            return 1;
        default:
            return 0;
    }
}

int lex(char* s){
    for(int i=0;i<strlen(s);i++){
        if(s[i]==' '){
            push(T_SPACE);
        }else if(s[i]=='v'){
            if(s[i+1]=='a'){
                if(s[i+2]=='r') push(T_VAR);
            }else{
                while(s[i]!=' '){

                }
            }
        }
    }
}

int main() {
    char* str = "Hello World!";
    lex(str);

    printf("Done.");
    return 0;
}
