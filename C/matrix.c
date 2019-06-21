#include <stdio.h>
int main()
{
	/* Matrix */
	int mat[2][2],choice,r,c,count=0;
	int matStore[2][2];
	int i,j;
	printf("Enter Matrix : \n");
	for (r = 0; r < 2; ++r) {
		for (c = 0; c < 2; ++c) {
			printf("Enter %d %d value\n",r+1 ,c+1);
			scanf("%d",&mat[r][c]);
		}
	}
	printf("Now what you want to do with your Matrix\n");
	printf("\n 1. Display the Matrix");
	printf("\n 2. Display the Lower Triangle of Matrix");
	printf("\n 3. Display the Upper Triangle of Matrix");
	printf("\n 4. Display the Diagonal Elements of Matrix");
	printf("\n 5. Display the Transpose of Matrix");
	printf("\n 6. Check for Symmetric Matrix");
	printf("\n Enter your Choice : ");
	scanf("%d",&choice);
	switch(choice){
		case 1:
			printf("Matrix is : \n");
			for (i = 0; i < 2; ++i) {
				for (j = 0; j < 2; ++j)
					printf("%d\t", mat[i][j]);
			}
			break;
		case 2:
			printf("The Lower Triangle of Matrix is : \n");
			for (i = 0; i < 2; ++i) {
				printf("\n");
				for (j = 0; j<=i; ++j)
					printf("%d\t", mat[i][j]);
			}
			break;
		case 3:
			printf("The Upper Triangle of Matrix is : \n");
			for (i = 0; i < 2; ++i) {
				for (j = 0; j<=i; ++j)
					printf("\t");
				for (j = c; c<=2; ++c)
					printf("%d\t",mat[i][c]);
				printf("\n");
			}
			break;
		case 4:
			printf("The Diagonal Elements of Matrix : \n");
			for (i = 0; i < 2; ++i) {
				for (j = 0; j < count; ++j) {
					if (i==j)
						printf("Diagonal Elements are : \n");
				}
			}
			break;
		case 5:
			printf("Matrix is : \n");
				for (i = 0; i < 2; ++i){
					for (j = 0; j < 2; ++j)
						printf("%d\t", mat[i][j]);
				}
			printf("The\n");
			break;
		default :
			printf("Enter a valid Option\n");

	}
	return 0;
}
