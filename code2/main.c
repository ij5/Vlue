#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>

#define T_EQUAL 276
#define T_LEFT_SB 277
#define T_RIGHT_SB 278
#define T_LEFT_MB 279
#define T_RIGHT_MB 280
#define T_COMMA 281

void resetElement(char *element, char *elementValue, int elementCount, int elementValueCount){
    memset(element, 0, 0);
    memset(elementValue, 0,0);
    elementCount = 0;
    elementValueCount = 0;
}

void lex(char* s, FILE* o){
    char* element;
    char* elementValue;
    int elementCount = 0;
    int elementValueCount = 0;


	for(int i=0;i<strlen(s);i+=1){
		if(s[i]=='('){
			if(s[i-1]=='l'){
				if(s[i-2]=='m'){
					if(s[i-3]=='t'){
						if(s[i-4]=='h'){
						    printf("<html");
							while(s[i]!=')'){   //)로 커서를 옮긴다.
							    i+=1;
							}
							if(s[i-1]!='('){    //만약 ()가 아니라면
							    while(s[i]!='('){   //커서를 (로 옮긴다.
							        i-=1;
							    }
							    i+=1;   //커서를 1 증가시킨다.
							    while(s[i]!='='){   /*=까지 반복.*/
							        element[elementCount] = s[i];   //element에 값을 추가한다.
							        elementCount+=1;                //elementCount
							        i+=1;
							    }
							    i+=1;           //커서를 1 증가시킨다.
							    while(s[i]!=')'){   //)가 나올때까지 반복
							        elementValue[elementValueCount] = s[i];     //element의 값을 elementValue에 추가한다.
							        elementValueCount+=1;
							        i+=1;
							    }
							    printf(" ");    //띄어쓰기
							    printf("%s", element);      //element를 출력한다.
							    printf("\"%s\"", elementValue);  //element의 값을 따옴표에 감싼 채 출력한다.
							    printf(">");    //태그를 닫는다.
							    resetElement(element, elementValue, elementCount, elementValueCount);
							}else{
							    continue;
							}
						}else{
							continue;
						}
					}else{
						continue;
					}
				}else{
					continue;
				}
			}else{
				continue;
			}
		}else{
			continue;
		}
	}
}

int main(void){
	char *s = "html(asd=asd){head(){title(){Hello World!}}}";
	FILE *o = fopen("index.html", "at");
	lex(s, o);
}
