#include <stdio.h>
int main() {
	/* Linear Search */
	int a[10],i,ser;
	for (i = 0; i < 10; ++i) {
		printf("Enter values : ");
		scanf("%d",&a[i]);
	}
	printf("Enter the value to search : \n");
	scanf("%d",&ser);
	for (i = 0; i < 10; ++i) {
		if (a[i]==ser) {
			printf(" Element found at %d\n", i+1);
			break;
		}
	}
	return 0;
}
