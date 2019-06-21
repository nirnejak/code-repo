#include <stdio.h>
int main(){
	int f=0,f1=1,f2=0,n=10,i;
	for(i=1;i<=n;i++){
		printf("%d\t",f);
		f2=f1;
		f1=f;
		f=f1+f2;
	}
	return 0;
}
