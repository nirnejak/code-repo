#include <iostream>
using namespace std;
int main(int argc, char const *argv[]){
	string str1,str2;
	cout<<"Enter First String : ";
	getline(cin,str1);
	cout<<"Enter Second String : ";
	getline(cin,str2);
	if(str1.compare(str2)==0)
		cout<<"Both Strings are equal";
	else if(str1.compare(str2)>0)
		cout<<"String 1 is Greater than String 2";
	else
		cout<<"String 1 is Less than String 2";
	return 0;
}