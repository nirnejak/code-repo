#include <stdio.h>
int main(){
	int i,j,k,n=9;
	for(i=1;i<=n;i++){
		for(j=1;j<=n-i;j++){
			printf("%d",j);
		}
		for(k=0;k<(i-1)*2;k++){
			printf(" ");
		}
		for(j=n-i;j>=1;j--){
			printf("%d",j);
		}
		printf("\n");
	}
	return 0;
}