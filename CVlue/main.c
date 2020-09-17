/*
 __     __  __        __    __  ________ 
/  |   /  |/  |      /  |  /  |/        |
$$ |   $$ |$$ |      $$ |  $$ |$$$$$$$$/ 
$$ |   $$ |$$ |      $$ |  $$ |$$ |__    
$$  \ /$$/ $$ |      $$ |  $$ |$$    |   
 $$  /$$/  $$ |      $$ |  $$ |$$$$$/    
  $$ $$/   $$ |_____ $$ \__$$ |$$ |_____ 
   $$$/    $$       |$$    $$/ $$       |
    $/     $$$$$$$$/  $$$$$$/  $$$$$$$$/ 
*/



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

void error(const char *msg){
    fputs(msg, stderr);
    exit(1);
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
    int position;
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
    T_LSB,
    T_RSB,
    T_ADD,
    T_SUB,
    T_MUL,
    T_DIV,
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
    if(data=="") error("It's empty.");
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
            token[i].position = 0;
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

                token[i].position++;
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

                token[i].position++;
            }

            if(*data=='.'){
                data++;
                token[i].position++;
                tempcount++;
                temp[tempcount] = '.';
                tempcount++;
                for(;isCutCharacter(*data)==false;tempcount++){
                    temp[tempcount] = *data;
                    temp[tempcount+1] = '\0';
                    data+=1;
                    token[i].position++;
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

            token[i].position++;
        }else if(*data==' '||*data=='\t'||*data=='\r'){
            data++;
            i--;

            token[i].position++;
        }else if(*data==';'){
            printf("SEMI\n");
            data++;
            token[i].num = i+1;
            token[i].type = T_SEMI;
            token[i].value = malloc(sizeof(*data));
            strcpy(token[i].value, ";\0");
            token[i].lineno = line;
            token[i].position++;
        }else if(*data==':'){
            printf("COLON\n");
            data++;
            token[i].num = i+1;
            token[i].type = T_SEMI;
            token[i].value = malloc(sizeof(*data));
            strcpy(token[i].value, ":\0");
            token[i].lineno = line;
            token[i].position++;
        }else if(*data=='('){
            printf("LSB\n");
            data++;
            token[i].num = i+1;
            token[i].type = T_LSB;
            token[i].value = malloc(sizeof(*data));
            strcpy(token[i].value, "(\0");
            token[i].lineno = line;
            token[i].position++;
        }else if(*data==')'){
            printf("RSB\n");
            data++;
            token[i].num = i+1;
            token[i].type = T_RSB;
            token[i].value = malloc(sizeof(*data));
            strcpy(token[i].value, ")\0");
            token[i].lineno = line;
        }else if(*data=='+'){
            printf("ADD\n");
            data++;
            token[i].num = i+1;
            token[i].type = T_ADD;
            token[i].value = malloc(sizeof(*data));
            strcpy(token[i].value, "+\0");
            token[i].lineno = line;
            token[i].position++;
        }else if(*data=='-'){
            printf("SUB\n");
            data++;
            token[i].num = i+1;
            token[i].type = T_SUB;
            token[i].value = malloc(sizeof(*data));
            strcpy(token[i].value, "-\0");
            token[i].lineno = line;
            token[i].position++;
        }else if(*data=='*'){
            printf("MUL\n");
            data++;
            token[i].num = i+1;
            token[i].type = T_MUL;
            token[i].value = malloc(sizeof(*data));
            strcpy(token[i].value, "*\0");
            token[i].lineno = line;
            token[i].position++;
        }else if(*data=='/'){
            if(*(data+1)=='*'){
                data+=2;
                while(!(*data=='*'&&*(data+1)=='/')&&(*data!='\0')){
                    data++;
                    token[i].position++;
                }
                if(*data!='\0'){
                    data++;
                    token[i].position++;
                    data++;
                    token[i].position++;
                }
                i--;
                printf("COMMENT\n");
            }else{
                printf("DIV\n");
                data++;
                token[i].num = i+1;
                token[i].type = T_DIV;
                token[i].value = malloc(sizeof(*data));
                strcpy(token[i].value, "/\0");
                token[i].lineno = line;
                token[i].position++;
            }
        }else{
            printf("OTHER\n");

            printf("Error on token %c, line %d\n", *data, line);

            data+=1;
            i--;
            token[i].position++;
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
    int ProgramCounter;         // program counter
    int StackPointer;         // stack pointer
    int FramePointer;         // frame pointer
    int repeat;
}VM;

VM *initVM(int *code, int pc, int datasize, int repeat){
    VM *vm = (VM*)malloc(sizeof(VM));
    memset(vm, '\0', sizeof(VM));
    vm->code = code;
    vm->ProgramCounter = pc;
    vm->FramePointer = 0;
    vm->StackPointer = -1;
    vm->locals = (int*)malloc(sizeof(int)*datasize);
    vm->stack = (int*)malloc(sizeof(int)*STACK_SIZE);
    vm->repeat = repeat;

    return vm;
}

void rmVM(VM *vm){
    free(vm->locals);
    free(vm->stack);
    free(vm);
}

enum {
    OP_ADD     = 0x80,
    OP_SUB     = 0x81,
    OP_MUL     = 0x82,
    OP_DIV     = 0x83,
    OP_RB      = 0x84,
    OP_LB      = 0x85,
    OP_EQ      = 0x86,
    OP_JMP     = 0x87,
    OP_JMPT    = 0x88,
    OP_JMPF    = 0x89,
    OP_CONST   = 0x8A,
    OP_LOAD    = 0x8B,
    OP_GLOAD   = 0x8C,
    OP_STORE   = 0x8D,
    OP_GSTORE  = 0x8E,
    OP_PRINT   = 0x8F,
    OP_POP     = 0x90,
    OP_HALT    = 0x91,
    OP_CALL    = 0x92,
    OP_RET     = 0x93,
};

void push(VM *vm, int v){
    vm->stack[++vm->StackPointer] = v;
}

int pop(VM *vm){
    return vm->stack[vm->StackPointer--];
}

int  next(VM *vm){
    return vm->code[vm->ProgramCounter++];
}

#define OP(x) case OP_##x

void runVM(VM *vm){
    do{
        int opcode = next(vm);
        break;
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

typedef struct _Node{
    int type;
    struct _Node *op1;
    struct _Node *op2;
}Node;


enum{
    N_NUM = 2048,
    N_ROOT,
    N_FACTOR,
    N_TERM,

};

int match(Token *token, int t);
int parse(Token *token);
int program(Token *token, Node *node);
int expression(Token *token, Node *node);
int factor(Token *token, Node *node);
int term(Token *token, Node *node);
int factor_tail(Token *token, Node *node);
int term_tail(Token *token, Node *node);

int i = 0;

int match(Token *token, int t){
    if(token[i].type!=t){
        printf("Expected token: %s\n", token[i].value);
        exit(-1);
    }    
    i++;
}

int parse(Token *token){
    Node node;

    program(token, &node);
}

int program(Token *token, Node *node){
    expression(token, node);
}

int expression(Token *token, Node *node){
    term(token, node);
}

int factor(Token *token, Node *node){
    int value = 0;
    if(token[i].type==T_LSB){
        match(token, T_LSB);
        value = expression(token, node);
        match(token, T_RSB);
    }
}

int term(Token *token, Node *node){
    
}

int term_tail(Token *token, Node *node){

}

/*
    ====================
    MAIN
    ====================
*/



int main(int argc, char *argv[]){

    Token *t = lexer("(1+2)*3/4-5/*hello World!*/");
    
    int program[] = {};
    
    parse(t);

    VM *vm = initVM(program, 0/*program count*/, 0/*LOCAL*/, 26/*repeat*/);

    runVM(vm);
    rmVM(vm);

    free(t);


    /*
        BUILD
    */
    char build[30] = {0};
    FILE *rbuildp = fopen("BUILD", "r");
    fgets(build, sizeof(build), rbuildp);
    int buildi = atoi(build);
    buildi++;
    sprintf(build, "%d", buildi);
    FILE *wbuildp = fopen("BUILD", "w");
    fputs(build, wbuildp);
    fclose(rbuildp);
    fclose(wbuildp);
    printf("\nBUILD: %d\n", buildi);
    /*
        END
    */

    return 0;
}
