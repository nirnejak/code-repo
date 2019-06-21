#include <iostream>
using namespace std;

int main(){
	int a,b,c;
	cin>>a>>b;
	try{
		if(b)
			cout<<"Result is "<<(a/b);
		else
			throw(b);
	}
	catch(int i){
		cout<<"Cannot divided by zero";
	}
	return 0;
}