#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>

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
    Token *token = malloc(sizeof(Token));  //임시
    int line = 1;

    char temp[128];     //최대 128의 문자열 토큰 길이
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
            for(int j=0;isCutCharacter(*data) == false&&((*data >= 'a' && *data <= 'z') || (*data >= 'A' && *data <= 'Z') || (*data == '_') ||(*data == '0'||*data == '1'||*data == '2'||*data == '3'||*data == '4'||*data == '5'||*data == '6'||*data == '7'||*data == '8'||*data == '9'));j++){
                temp[j] = *data;
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
            token[i].value = malloc(sizeof(temp));
            strcpy(token[i].value, temp);
            printf("%s", token[i].value);
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
            strcpy(token[i].value, "=");
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
            strcpy(token[i].value, ";");
            token[i].lineno = line;
        }else if(*data==':'){
            printf("COLON");
            data++;
            token[i].num = i+1;
            token[i].type = T_SEMI;
            token[i].value = malloc(sizeof(*data));
            strcpy(token[i].value, ":");
            token[i].lineno = line;
        }else{
            printf("OTHER\n");

            printf("Error on token %c\n", *data);

            data+=1;
            i--;
        }
        //printf("value: %s\n", token[i].value);
        //printf("i: %d\n",i);
    }
    return token;
}


typedef struct _AST
{
    int type;
    char *data;
    struct _AST *child[128];
}AST;

enum childstate{
    EXPRESSION = 128,
    ROOT,
    STATEMENT,
    PLUS,
    MINUS,
    DIV,
    MUL,
};

AST *p_root();
AST *p_statement();
AST *p_expression();
AST *p_plus();
AST *p_minus();
AST *p_div();
AST *p_mul();
AST *parser();
AST *p_int();
AST *p_float();

AST *make_node(int type, char *data, AST *n){
    AST *node = malloc(sizeof(AST));
    node->child[0] = n;
    node->type = type;
}


AST *p_root(Token *token){
    AST *root = p_statement(token[0].value);
    root->type = ROOT;
    root->child[0] = root;
    return root;
}


#define CHILD_SIZE sizeof(statement->child)/sizeof(statement->child[0])
AST *p_statement(char *data){
    AST *statement = malloc(sizeof(AST));
    statement->child[0] = p_expression(data);
    return statement;
}

AST *p_expression(char *data){
    AST *expression = malloc(sizeof(AST));
    expression->child[0] = p_plus(data);
    return expression;
}

AST *p_plus(char *data){
    AST *plus = malloc(sizeof(AST));
    plus->child[0] = p_float(data);
    return plus;
}

AST *p_minus(){

}

AST *p_uminus(){

}

AST *p_div(){

}

AST *p_mul(){

}

AST *p_int(){

}

AST *p_float(char *data){
    AST *f = malloc(sizeof(AST));
    f->child[0] = malloc(sizeof(AST));
    return f;
}

AST *parser(){

}

int main(int argc, char *argv[]){

    Token *t = lexer("zdds asd =  45.6;\n");
    printf("%s", t[0].value);
    printf("%s", t[1].value);
    printf("%s", t[2].value);
    printf("%d", t[0].num);


    p_root(t);

    asm(
        ""
        ""
    );


    return 0;
}
