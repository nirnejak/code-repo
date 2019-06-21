#include<iostream>
using namespace std;
int main(){
	int i,s,e,j;
	cout<<"Start of the range : ";
	cin>>s;
	cout<<"End of the range : ";
	cin>>e;
	for(i=s;i<=e;i++){
		for(j=2;j<i;j++){
			if(i%j==0){
				cout<<"";
				break;
			}
		}
		if(j>=i)
			cout<<"\n"<<i;
	}
	return 0;
}