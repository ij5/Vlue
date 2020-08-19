#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

typedef struct _Person{
    char name[20];
    int age;
    char address[100];
}Person;

enum{
    A = 0,
    B,
    C,
    D,
    E
};

int main(void){
    
    int num = 5;

    int *numPtr = &num;

    printf("%d\n", *numPtr);

    return 0;
}
