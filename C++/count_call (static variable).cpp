#include <iostream>
using namespace std;

class A{
		int i;
		static int j;
	public:
		A(){
			i=0;
		}
		void fn1();
		void showData(){
			cout<<endl<<"j: "<<j;
			cout<<endl<<"i: "<<i;
		}
};

int A::j;
void A::fn1(){
	i++;
}

int main(){
	A x,y;
	x.fn1();
	x.fn1();
	x.fn1();
	x.fn1();
	x.showData();
	y.fn1();
	y.showData();
	return 0;
}