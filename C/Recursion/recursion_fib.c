#include <stdio.h>
int num=0;
int f=0,f1=1,f2=0;
int fabb(int n){
	if(num<n){
		printf("%d\t",f);
		f2=f1;
		f1=f;
		f=f1+f2;
		num++;
		fabb(n);
	}
}

int main(){
	fabb(10);
	return 0;
}
