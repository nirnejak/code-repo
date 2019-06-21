#include <iostream>
#include <algorithm>
using namespace std;
int main(){
	int n;
	
	cout<<"Enter Number of Elements : ";
	cin>>n;
	cout<<"Now Enter "<<n<<" elements to sort"<<endl;

	int a[n],max=0;
	for(int i=0;i<n;i++)
		cin>>a[i];
	cout<<endl;
	sort(a,a+n);
	for(int i=0;i<n;i++)
		cout<<a[i]<<"\n";
	return 0;
}