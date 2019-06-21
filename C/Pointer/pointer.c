#include <stdio.h>
int main() {
	int a,*c;
	a=20;
	c=&a;
	a=*c;
	printf("%d",c);
	printf("\n");
	printf("%d",a);
	return 0;
}
