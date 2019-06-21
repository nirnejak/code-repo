#include<stdio.h>
struct stud{
	int a;
};

int main(){
	struct stud std[2];	
	std[0].a=2;
	std[1].a=3;
	printf("%d",std[0].a);
	printf("%d",std[1].a);	
	return 0;
}
