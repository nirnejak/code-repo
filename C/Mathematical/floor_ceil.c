#include<stdio.h>
#include<math.h>
int main(){
	float a=16.0/3.0,b,c;
	b = floor(a);
	c = ceil(a);
	printf("floor = %d",b);
	printf("ceil = %d",c);
	return 0;
}
