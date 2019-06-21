#include<stdio.h>
int main() {
	int num,flag=0,i;
	printf("\nEnter the Number : ");
	scanf("%d",&num);
	for(i=1;i<=num;i++) {
		if(num%i==0)
			flag++;
	}
	if(flag==2)
		printf("Number is Prime\n");
	else
		printf("Number is not Prime\n");
	return 0;
}
