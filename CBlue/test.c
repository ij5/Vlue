#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <string.h>
#include <stdbool.h>

#define int long long

int line;

typedef struct _Token
{
    int num;
    int type;
    int lineno;
    char *value;
}Token;

enum TokenType{
    T_IDENTIFIER = 1024,
    T_NEWLINE,
    T_INT,
    T_FLOAT,
    T_VAR,
    T_EQUAL,
    T_SEMI,
    T_FUNCTION,
    OTHER,
};



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
    case '\0':
        return true;
    default:
        return false;
    }
}


void clearstr(char *c){
    for(int i=0;c[i]!='\0';i++){
        c[i] = 0;
    }
}





#define TOKEN_LENGTH 1024
Token *lexer(char *data){
    Token *token = malloc(sizeof(Token)*TOKEN_LENGTH);  //임시

    char temp[128];     //최대 128의 문자열 토큰 길이
    int tempcount = 0;
    
    int i = 0;
    while(*data!=0){
        if(*data=='\n'){
            line++;

            printf("NEWLINE\n");

            data+=1;
            //i--;
            token[i].num = i+1;
            token[i].value = "\n";
            token[i].lineno = line;
            token[i].type = T_NEWLINE;
        }else if(*data=='v'&&*(data+1)=='a'&&*(data+2)=='r'){

            printf("VAR\n");
            data+=3;
            token[i].num = i+1;
            token[i].type = T_VAR;
            token[i].value = "var";
            token[i].lineno = line;
        }else if(*data=='f'&&*(data+1)=='n'){
            printf("FUNCTION\n");
            data+=2;
            token[i].num = i+1;
            token[i].type = T_FUNCTION;
            token[i].value = "fn";
            token[i].lineno = line;
        }else if((*data >= 'a' && *data <= 'z') || (*data >= 'A' && *data <= 'Z') || (*data == '_')){
            for(
                int j=0;isCutCharacter(*data) == false&&((*data >= 'a' && *data <= 'z') || (*data >= 'A' && *data <= 'Z') || (*data == '_') ||
                (
                *data == '0'||*data == '1'||*data == '2'||*data == '3'||*data == '4'
              ||*data == '5'||*data == '6'||*data == '7'||*data == '8'||*data == '9'
                )
            );j++){
                temp[j] = *data;
                ++data;
            }
            printf("IDENTIFIER\n");

            token[i].num = i+1;
            token[i].type = T_IDENTIFIER;
            token[i].lineno = line;
            token[i].value = temp;
            clearstr(temp);
        }else if(
            *data == '0'||*data == '1'||*data == '2'||*data == '3'||*data == '4'
          ||*data == '5'||*data == '6'||*data == '7'||*data == '8'||*data == '9'
        ){
            for(int j=0;isCutCharacter(*data)==false;j++){
                temp[j] = *data;
                data+=1;
                tempcount = j;
            }
            
            if(*data=='.'){
                data++;
                tempcount++;
                temp[tempcount] = '.';
                tempcount++;
                for(;isCutCharacter(*data)==false;tempcount++){
                    temp[tempcount] = *data;
                    data+=1;
                }
                tempcount = 0;
                printf("FLOAT\n");
                token[i].value = temp;
                token[i].type = T_FLOAT;
                clearstr(temp);
            }else{
                printf("INT\n");
                token[i].value = temp;
                token[i].type = T_INT;
                clearstr(temp);
            }

            token[i].num = i+1;
            token[i].lineno = line;
        }else if(*data=='='){
            printf("EQUAL\n");
            data++;
            token[i].num = i+1;
            token[i].type = T_EQUAL;
            token[i].value = *data+"\0";
            token[i].lineno = line;
        }else if(*data==' '||*data=='\t'||*data=='\r'){
            data++;
            i--;
        }else if(*data==';'){
            printf("SEMI\n");
            data++;
            token[i].num = i+1;
            token[i].type = T_SEMI;
            token[i].value = *data+"\0";
            token[i].lineno = line;
        }else{
            printf("OTHER\n");
            //printf("%c", *data);

            data+=1;
            token[i].num = i+1;
            token[i].type = OTHER;
            token[i].value = *data+"\0";
            token[i].lineno = line;
        }

        i++;
    }
    return token;
}



char *parser(Token *token){
    for(int i=0;token[i].num!=0;i++){
        switch(token[i].type){
            case T_VAR:
            case T_EQUAL:
            case T_FLOAT:
            case T_INT:
            case T_FUNCTION:
            case T_IDENTIFIER:
            case T_NEWLINE:
            case T_SEMI:
            default:
                printf("UNKNOWN ERROR");
        }
    }
}


int main(int argc, char *argv[]){

    Token *t = lexer("var abc    =45.6;var cba =  45;\n");
    parser(t);

    asm(
        ""
        ""
    );
    

    return 0;
}

