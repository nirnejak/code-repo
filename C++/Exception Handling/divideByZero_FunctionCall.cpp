#include <iostream>
using namespace std;
void divide(int x, int y, int z){
	if(x-y)
		cout<<"Result"<<z/(x-y)<<endl;
	else
		throw(x-y);
}

int main(){
	//first call
	try{
		divide(10,20,30);
	}
	catch(int i){
		cout<<"Cannot divide by zero"<<endl;
	}
	//second call
	try{
		divide(10,10,20);
	}
	catch(int i){
		cout<<"Cannot divide by zero"<<endl;
	}
	return 0;
}