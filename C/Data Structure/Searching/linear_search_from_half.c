#include <stdio.h>
int main() {
	int arr[10],num,mid,pos=0,i;
	printf("Enter Numbers : \n");
	for (i = 0; i < 10; ++i)
		scanf("%d",&arr[i]);
	printf("Enter the Element you want to search\n");
	scanf("%d",&num);
	mid=10/2;
	if (num>arr[mid]) {
		for (i = mid; i < 10; ++i) {
			if (arr[i]==num) {
				pos=i;
				break;
			}
		}
	}
	else{
		for (i = mid; i >= 0; --i) {
			if (arr[i]==num) {
				pos=i;
				break;
			}
		}
	}
	if (pos==0)
		printf("Number is Not Found\n");
	else
		printf("Number is Found at position %d\n", pos+1);
	return 0;
}