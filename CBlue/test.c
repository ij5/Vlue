#define _CRT_SECURE_NO_WARNINGS
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
    Token *token = (Token *)malloc(sizeof(Token)*TOKEN_LENGTH);  //임시
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

#define STACK_SIZE 100

typedef struct _VM{
    int *locals;
    int *code;
    int *stack;
    int pc;
    int sp;
    int fp;
}VM;

VM *initVM(int *code, int pc, int datasize){
    VM *vm = (VM*)malloc(sizeof(VM));
    vm->code = code;
    vm->pc = pc;
    vm->fp = 0;
    vm->sp = -1;
    vm->locals = (int*)malloc(sizeof(int)*datasize);
    vm->stack = (int*)malloc(sizeof(int)*STACK_SIZE);

    return vm;
}

void rmVM(VM *vm){
    free(vm->locals);
    free(vm->stack);
    free(vm);
}

enum {
    ADD = 128,
    SUB,
    MUL,
    DIV,
    LT,
    EQ,
    JMP,
    JMPT,
    JMPF,
    CONST,
    LOAD,
    GLOAD,
    STORE,
    GSTORE,
    PRINT,
    POP,
    HALT,
    CALL,
    RET,
};

#define PUSH(vm, v) vm->stack[++vm->sp] = v
#define POP(vm)     vm->stack[vm->sp--]
#define NCODE(vm)   vm->code[vm->pc++]

void runVM(VM *vm){
    do{
        int opcode = NCODE(vm);
        int v, addr, offset, a, b, argc, rval;

        switch(opcode){
            case HALT:
                return;
            case CONST:
                v = NCODE(vm);
                PUSH(vm, v);
                break;
            case ADD:
                b = POP(vm);
                a = POP(vm);
                PUSH(vm, a+b);
                break;
            case SUB:
                b = POP(vm);
                a = POP(vm);
                PUSH(vm, a-b);
                break;
            case MUL:
                b = POP(vm);
                a = POP(vm);
                PUSH(vm, a*b);
                break;
            case DIV:
                b = POP(vm);
                a = POP(vm);
                PUSH(vm, a/b);
                break;
            case LT:
            case EQ:
            case JMP:
                vm->pc = NCODE(vm);
                break;
            case JMPT:
                addr = NCODE(vm);
                printf("%d", POP(vm));
                break;
            case JMPF:
                break;
            case LOAD:
            case GLOAD:
            case GSTORE:
            case CALL:
            case RET:
            case POP:
                --vm->sp;
                break;
            case PRINT:
                v = POP(vm);
                printf("%d\n", v);
                break;
            default:
                break;
        }
    }while(1);
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
    PARSER
    ====================
*/

/*
    ====================
    MAIN
    ====================
*/



int main(int argc, char *argv[]){

    Token *t = lexer("var asd:int =  45.6;\n");


    int program[] = {
        CONST, 0,
        JMPT, 0
    };

    VM *vm = initVM(program, 0, 0);

    runVM(vm);

    asm(
        ""
        ""
    );

    

    return 0;
}
