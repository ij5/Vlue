#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <string.h>
#define int long long

int token;
int token_val;
int line;
char *src, *old_src;

enum {
    LEA,
    IMM,
    JMP,
    CALL,
    JZ,
    JNZ,
    ENT,
    ADJ,
    LEV,
    LI,
    LC,
    SI,
    SC,
    PUSH,
    OR,
    XOR,
    AND,
    EQ,
    NE,
    LT,
    GT,
    LE,
    GE,
    SHL,
    SHR,
    ADD,
    SUB,
    MUL,
    DIV,
    MOD,
    OPEN,
    READ,
    CLOS,
    PRTF,
    MALC,
    MSET,
    MCMP,
    EXIT
};

enum{
    Num = 128,
    Fun,
    Sys,
    Glo,
    Loc,
    Id,
    Char,
    Else,
    Enum,
    If, 
    Int,
    Return,
    Sizeof,
    While,
    Assign,
    Cond,
    Lor,
    Lan,
    Or,
    Xor,
    And,
    Eq,
    Ne,
    lt,
    Gt,
    Le,
    Ge,
    Shl,
    Shr,
    Add,
    Sub,
    Mul,
    Div,
    Mod,
    Inc,
    Dec,
    Brek
};

enum{
    Token,
    Hash,
    Name,
    type,
    Class,
    Value,
    BType,
    BClass,
    BValue,
    IdSize
};

void next(){
    char *last_pos;
    int hash;

    token = *src;
    while(token){
        ++src;
        if(token=='\n'){
            ++line;
        }else if(token=='#'){
            while(*src != 0 && *src != '\n'){
                src++;
            }
        }else if((token >= 'a' && *src <= 'z') || (*src >= 'A' && *src <= 'Z') || (*src >= '0' && *src <= '9') || (*src == '_')){
            hash = hash * 147 + *src;
            src++;
        }
    }
}

int main(void){
    return 0;
}