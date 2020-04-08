#include <stdio.h>

int str_cmp(char* s, char *ss){
    int i = 0;
    while(s[i]&&ss[i]){
        if(s[i]==ss[i]){
            i+=1;
            continue;
        }else {
            return 0;
        }
    }
    return 1;
}

int main(void){
    char *a = "abc";
    char *b = "abcd";
    if(str_cmp(a,b)==1){
        printf("correct");
    }
}