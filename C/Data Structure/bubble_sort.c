#include <stdio.h>
int main() {
	int i,j,arr[10],temp;
	printf("Enter Numbers : \n");	
	for (i = 0; i < 10; i++)
		scanf("%d",&arr[i]);
	for (j = 10; j >= 0; j--) {
		for (i = 0; i < 9; i++) {
			if (arr[i]>arr[i+1]) {
				temp=arr[i];
				arr[i]=arr[i+1];
				arr[i+1]=temp;
			}
		}
	}
	for (i = 0; i < 10; i++)
		printf("%d  ",arr[i]);
	return 0;
}