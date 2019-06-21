#include <stdio.h>
union Number{
	int x;
	float y;
};
int main(){
	union Number value;
	value.x=50;
	printf("%d",value.x);
	return 0;
}
