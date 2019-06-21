#include <iostream>
using namespace std;

int main(){
	int a,b,ans;
	char op;
	cout<<"Enter Expression : ";
	cin>>a>>op>>b;
	switch(op){
		case '+':
			ans=a+b;
			break;
		case '-':
			ans=a-b;
			break;
		case '*':
			ans=a*b;
			break;
		case '/':
			ans=a/b;
			break;
		case '%':
			ans=a%b;
			break;
		case '^':
			ans=a^b;
			break;
		default:
			cout<<"Enter Appropriate Expression";
	}
	cout<<"Answer is "<<ans;
	cout<<endl<<a<<endl<<op<<endl<<b;
	return 0;
}