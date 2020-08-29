#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>
#include <stdint.h>

/*
    =========
    UTILITIES
    =========
*/


void clearstr(char *c){
    for(int i=0;c[i]!='\0';i++){
        c[i] = 0;
    }
}


/*
    ================
    LEXICAL ANALYZER
    ================
*/


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

#define TOKEN_LENGTH 1024
Token *lexer(char *data){
    Token *token = malloc(sizeof(Token)*TOKEN_LENGTH);  //임시
    int line = 1;
    int TEMP_LENGTH = 128;

    char temp[TEMP_LENGTH];     //최대 128의 문자열 토큰 길이
    clearstr(temp);
    int tempcount = 0;

    for(int i=0;*data!=0;i++){
        if(*data=='\n'){
            line++;

            printf("NEWLINE\n");

            data+=1;
            //i--;
            token[i].num = i+1;
            token[i].value = "\n";
            token[i].lineno = line;
            token[i].type = T_NEWLINE;
        }else if((*data >= 'a' && *data <= 'z') || (*data >= 'A' && *data <= 'Z') || (*data == '_')){
            for(int j=0;isCutCharacter(*data) == false&&((*data >= 'a' && *data <= 'z') || 
                (*data >= 'A' && *data <= 'Z') || 
                (*data == '_') ||
                (*data == '0'||*data == '1'||*data == '2'||*data == '3'||*data == '4'||
                 *data == '5'||*data == '6'||*data == '7'||*data == '8'||*data == '9')
                );j++){
                temp[j] = *data;
                temp[j+1] = '\0';
                ++data;
            }

            if(strcmp(temp, "var")==0){
                printf("VAR\n");
                token[i].type = T_VAR;
            }else{
                printf("IDENTIFIER\n");
                token[i].type = T_IDENTIFIER;
            }

            token[i].num = i+1;
            token[i].lineno = line;
            token[i].value = malloc(TEMP_LENGTH);
            strcpy(token[i].value, temp);           //FIXME: 문자열 문제
            clearstr(temp);
        }else if(
            *data == '0'||*data == '1'||*data == '2'||*data == '3'||*data == '4'
          ||*data == '5'||*data == '6'||*data == '7'||*data == '8'||*data == '9'
        ){
            for(int j=0;isCutCharacter(*data)==false;j++){
                temp[j] = *data;
                temp[j+1] = '\0';
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
                    temp[tempcount+1] = '\0';
                    data+=1;
                }
                tempcount = 0;
                printf("FLOAT\n");
                token[i].value = malloc(sizeof(temp));
                strcpy(token[i].value, temp);
                token[i].type = T_FLOAT;
                clearstr(temp);
            }else{
                printf("INT\n");
                token[i].value = malloc(sizeof(temp));
                strcpy(token[i].value, temp);
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
            token[i].value = malloc(sizeof(*data));
            strcpy(token[i].value, "=\0");
            token[i].lineno = line;
        }else if(*data==' '||*data=='\t'||*data=='\r'){
            data++;
            i--;
        }else if(*data==';'){
            printf("SEMI\n");
            data++;
            token[i].num = i+1;
            token[i].type = T_SEMI;
            token[i].value = malloc(sizeof(*data));
            strcpy(token[i].value, ";\0");
            token[i].lineno = line;
        }else if(*data==':'){
            printf("COLON\n");
            data++;
            token[i].num = i+1;
            token[i].type = T_SEMI;
            token[i].value = malloc(sizeof(*data));
            strcpy(token[i].value, ":\0");
            token[i].lineno = line;
        }else{
            printf("OTHER\n");

            printf("Error on token %c, line %d\n", *data, line);

            data+=1;
            i--;
        }
        //printf("value: %s\n", token[i].value);
        //printf("i: %d\n",i);
    }
    return token;
}


/*
    ===============
    VIRTUAL MACHINE
    ===============
*/




typedef enum{
    OP_CONSTANT,
    OP_NIL,
    OP_TRUE,
    OP_FALSE,
    OP_POP,
    OP_GET_LOCAL,
    OP_SET_LOCAL,
    OP_GET_GLOBAL,
    OP_DEFINE_GLOBAL,
    OP_SET_GLOBAL,
    OP_GET_UPVALUE,
    OP_SET_UPVALUE,
    OP_GET_PROPERTY,
    OP_SET_PROPERTY,
    OP_SET_SUPER,
    OP_EQUAL,
    OP_GRATER,
    OP_LESS,
    OP_ADD,
    OP_SUB,
    OP_MUL,
    OP_DIV,
    OP_NOT,
    OP_NEGATE,
    OP_PRINT,
    OP_JUMP,
    OP_JIF,
    OP_LOOP,
    OP_CALL,
    OP_INVOKE,
    OP_SUPER_INVOKE,
    OP_CLOSURE,
    OP_CLOSE_UPVALUE,
    OP_RETURN,
    OP_CLASS,
    OP_INHERIT,
    OP_METHOD,
}OPCODE;

typedef struct _Chunk{
    int count;
    int capacity;
    uint8_t *code;
    int *lines;
    
}Chunk;

void initChunk(Chunk *chunk){
    chunk->count = 0;
    chunk->capacity = 0;
    chunk->code = NULL;
}

void writeChunk(Chunk *chunk){
    if(chunk->capacity < chunk->count + 1){
        int oldCapacity = chunk->capacity;
        chunk->capacity = GROW_CAPACITY(oldCapacity);
        chunk->code = GROW_ARRAY(uint8_t, chunk->code, oldCapacity, chunk->capacity);
    }
    chunk->code[chunk->count] = byte;
    chunk->count++;
}


/*
    ====================
    ABSTRACT SYNTAX TREE
    ====================
*/

typedef struct _AST
{
    int type;
    char *data;
    struct _AST *child[128];
}AST;



/*
    ====================
    MAIN
    ====================
*/



int main(int argc, char *argv[]){

    Token *t = lexer("var asd:int =  45.6;\n");


    asm(
        ""
        ""
    );

    

    return 0;
}
