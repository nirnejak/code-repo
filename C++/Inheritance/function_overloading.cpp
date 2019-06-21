#include <iostream>
using namespace std;

void swap(int *a,int *b);
void swap(float *a,float *b);

int main(){
	int x=10,y=20;
	float p=12.2,q=61.2;

	swap(&x,&y);				//for integer values
	swap(&p,&q);				//for integer values

	cout<<x<<endl<<y<<endl;
	cout<<p<<endl<<q<<endl;
	return 0;
}

void swap(int *a,int *b){
	*a=*a+*b;
	*b=*a-*b;
	*a=*a-*b;
}
void swap(float *a,float *b){
	*a=*a+*b;
	*b=*a-*b;
	*a=*a-*b;
}

// J2EE
// 