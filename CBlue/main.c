#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main(void){
    int num1 = 100;

    int *numPtr = &num1;

    printf("%d", *numPtr);
    

    return 0;
}
