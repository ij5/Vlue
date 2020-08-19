#include <stdio.h>
#include <stdlib.h>

int main(void){
	int *pi, i;
	pi = (int *)malloc(5 * sizeof(int));
	if(pi==NULL){
		printf("동적 메모리 할당에 실패했습니다.");
		exit(0);
	}
	pi[0] = 100;
	pi[1] = 150;
	pi[2] = 200;
	pi[3] = 300;
	pi[4] = 400;


	for(int i=0;i < 5; i++){
		printf("%d\n", *(pi + i));
	}

	free(pi);

	return 0;

}