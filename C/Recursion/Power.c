#include<stdio.h>

rec_power(int x,int y){
	long int p;
	if(y==0)
		p=1;
	else
		p=x*rec_power(x,y-1);
	return p;
}

int main(){
	long int a,b,power;
	printf("Enter the Number : ");
	scanf("%ld",&a);
	printf("Enter the Power : ");
	scanf("%ld",&b);
	power=rec_power(a,b);
	printf("The answer is : %d",power);
	return 0;
}
