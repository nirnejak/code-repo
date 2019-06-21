#include <iostream>
using namespace std;

class B{
		int a;
	public:
		int b;
		void getAB();
		int getA();
		void showA();
};

class D:public B{
		int c;
	public:
		void mul();
		void display();
};

int main(){
	D obj;
	obj.getAB();
	cout<<obj.getA()<<endl;
	obj.showA();
	obj.mul();
	obj.display();
	obj.b=20;
	obj.mul();
	obj.display();
	return 0;
}

void B::getAB(){
	a=5;
	b=10;
}

void B::showA(){
	cout<<getA()<<endl;
}

int B::getA(){
	return a;
}

void D::mul(){
	c=b*getA();
}

void D::display(){
	cout<<"a"<<getA()<<endl;
	cout<<"b"<<b<<endl;
	cout<<"c"<<c<<endl;
}