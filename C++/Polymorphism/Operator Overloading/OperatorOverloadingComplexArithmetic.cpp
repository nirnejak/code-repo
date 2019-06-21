#include <iostream>
using namespace std;

class COMPLEX{
	float i,j;
public:
	COMPLEX(){
	}
	COMPLEX(float a, float b){
		i=a;
		j=b;
	}
	void showNo(){
		cout<<i<<" + i "<<j<<endl;
	}
	COMPLEX operator +(COMPLEX n){
		COMPLEX ans;
		ans.i=i+n.i;
		ans.j=j+n.j;
		return ans;
	}
	COMPLEX operator -(COMPLEX n){
		COMPLEX ans;
		ans.i=i-n.i;
		ans.j=j-n.j;
		return ans;
	}
};

int main(){
	COMPLEX C1(10.2,20.5), C2(30.5,40.1), C3, C4;
	C3=C1+C2;
	C4=C1-C2;
	C1.showNo();
	C2.showNo();
	C3.showNo();
	C4.showNo();
	return 0;
}