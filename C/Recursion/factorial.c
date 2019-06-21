#include<stdio.h>
int fact(int n) {
	if(n==0)
		return 1;
	else
		return n*fact(n-1);
}
int main() {
	int a;
	printf("Enter a  : ");
	scanf("%d",&a);
	a=fact(a);
	printf("answer is %d",a);
	return 0;
}
