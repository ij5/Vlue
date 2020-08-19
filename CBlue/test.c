#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <string.h>
#include <stdbool.h>

#define int long long

int line;

int isCutCharacter(char c){
    switch (c)
    {
    case ' ':
    case '\t':
    case '\r':
    case '\n':
    case '<':
    case '>':
    case '[':
    case ']':
    case '{':
    case '}':
    case '=':
    case '!': 
    case '+':
    case '-':
    case '*':
    case '/':
    case '%':
    case '^': 
    case '?':
    case '.':
    case ':':
    case ';':
    case '(':
    case ')':
    case '|':
        return true;
    default:
        return false;
    }
}

typedef struct _Token
{
    int tokentype;
}Token;


int lexer(char *data){

    Token token[1024];
    
    
    while(*data!=0){
        if(*data=='\n'){
            line++;
        }else if((*data >= 'a' && *data <= 'z') || (*data >= 'A' && *data <= 'Z') || (*data == '_')){

        }
        data++;
    }
}


int main(void){

    lexer("Hello World!");
    return 0;
}