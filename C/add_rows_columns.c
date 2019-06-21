#include <stdio.h>
int main(){
	int a[2][2],sum_r[2],sum_c[2],i,j;
	printf("Enter the Numbers : \n");
	for (i = 0; i < 2; ++i){
		for (j = 0; j < 2; ++j)
			scanf("%d",&a[i][j]);
	}
	for (i = 0; i < 2; ++i){
		sum_r[i]=0;
		for (j = 0; j < 2; ++j)
			sum_r[i]+=a[i][j];
	}
	for (i = 0; i < 2; ++i){
		sum_c[i]=0;
		for (j = 0; j < 2; ++j)
			sum_c[i]+=a[j][i];
	}
	printf("Sum of Rows : \n");
	for (i = 0; i < 2; ++i)
		printf("%d ",sum_r[i]);
	printf("\n");
	printf("Sum of Columns : \n");
	for (i = 0; i < 2; ++i)
		printf("%d ",sum_c[i]);
	return 0;
}