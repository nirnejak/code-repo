#include <iostream>
#include <cstring>

using namespace std;

class STR
{
		char a[10];
	public:
		STR(){
			cin>>a;
		}
		int operator ==(STR b){
			if(strcmp(a,b.a))
				return 0;
			else
				return 1;
		}
};

int main(){
	STR A,B;
	int flag;
	flag=A==B;
	if (flag)
		cout<<"Equal";
	else
		cout<<"Not equal";
	return 0;
}