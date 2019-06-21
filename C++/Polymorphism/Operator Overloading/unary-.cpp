#include <iostream>
using namespace std;

class SPACE
{
	int x,y,z;
public:
	void getData(int a,int b, int c){
		x=a;
		y=b;
		z=c;
	}
	void display(){
		cout<<x<<endl<<y<<endl<<z<<endl;
	}
	void operator -(){
		x=-x;
		y=-y;
		z=-z;
	}
};
int main(){
	SPACE obj;
	obj.getData(10,12,35);
	obj.display();
	-obj;
	obj.display();
	return 0;
}