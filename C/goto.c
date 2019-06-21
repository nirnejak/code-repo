#include<stdio.h>
#include<stdlib.h>
int main(){
	int a;
	printf("Enter a : ");
	scanf("%d",&a);
	if(a>20)
		printf("a is greater than 20 \n");
	else
		goto thispart;
	thispart:;
	printf("a is %d",a);
	return 0;
}
