#include <iostream>
#include <cstring>
using namespace std;

class STR{
		char a[10];
	public:
		STR(){
			cin>>a;
		}
		int operator +(STR b){
			strcat(a,b.a);
		}
		void show(){
			cout<<a;
		}
};

int main(){
	STR A,B;
	A+B;
	A.show();
	return 0;
}