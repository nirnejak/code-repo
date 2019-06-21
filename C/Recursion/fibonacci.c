#include <stdio.h>

int fib(int n) {
	if(n==0 || n==1) {
		return n;
	}
	else {
		return fib(n-1)+fib(n-2);
	}
}
int main() {
	int a,ans;
	printf("Enter Number : ");
	scanf("%d",&a);
	ans=fib(a);
	printf("Answer is : %d",ans);
	return 0;
}