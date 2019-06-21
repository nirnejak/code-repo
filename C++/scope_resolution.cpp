#include <iostream>
using namespace std;

class M{
	public:
		void display(){
			cout<<"M"<<endl;
		}
};
class N{
	public:
		void display(){
			cout<<"N"<<endl;
		}
};
class P:public M, public N{
	public:
		void display(){
			cout<<"P"<<endl;
		}
		void displayAll(){
			M::display();
			N::display();
			display();
		}
};

int main(){
	P obj;
	obj.displayAll();
	return 0;
}