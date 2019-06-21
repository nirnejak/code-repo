#include<stdio.h>
int main(){
	int a[3],b[3],c[3],n=3;
	int i;
	a[0]=1;
	a[1]=2;
	a[2]=3;
	toh(a,b,c,n);
	for(i=0;i<3;i++)
		printf("%d",c[i]);
	return 0;
}
toh(int A,int B,int C,int n){
	if(n>0){
		toh(A,B,C,n-1);
		printf("Move a disk from %d to %d\n",A,);
		toh(B,A,C,n-1);
	}
}
