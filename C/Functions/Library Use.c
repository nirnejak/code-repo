#include <stdio.h>
#include "my_lib.h"
int main(){
	int a,b=10,c;
	a=20;
	if(a) {
		int b=3;
		printf("\nb in if %d",b);
	}
	printf("\nb is %d\n",b);
	c=test_fun(a);
	printf("C is = %d\n",c);
	return 0;
}
