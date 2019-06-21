#include <stdio.h>
void print(int n){
	if(n==1)
		printf("1\t");
	else{
		print(n-1);
		printf("%d\t",n*n);
	}
}
int main(){
	int num=5;
	printf("Series Will be : \n");
	print(num);
	printf("\n");
	return 0;
}
