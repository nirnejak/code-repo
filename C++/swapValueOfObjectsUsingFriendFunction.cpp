#include <iostream>
using namespace std;

class fr2;
class fr1{
	public:
		int a;
		void fn1(int x){
			a=x;
		}
		friend void swap();
};

class fr2{
	public:
		int a;
		void fn2(int x){
			a=x;
		}
		friend void swap(fr1 p,fr2 q);
};

void swap(fr1 p,fr2 q){
	int temp;
	temp=p.a;
	p.a=q.a;
	q.a=temp;
	cout<<"A : "<<p.a<<endl;
	cout<<"B : "<<q.a<<endl;
}

int main(){
	fr1 A;
	fr2 B;
	A.fn1(2);
	B.fn2(3);
	swap(A,B);
	return 0;
}