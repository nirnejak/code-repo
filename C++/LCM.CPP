#include <iostream>
using namespace std;
int main(){
	int max=0,multiple_all=1,a[3],flag=0,lcm,i=0;
	cout<<"Enter numbers : \n";
	for(i=0;i<3;i++)
		cin>>a[i];
	for(i=0;i<3;i++){
		if(a[i]>max)
			max=a[i];
	}
	for(i=0;i<3;i++)
		multiple_all*=a[i];
	for(i=max;i<=multiple_all;i++){
		flag=0;
		for(int j=0;j<3;j++){
			if(i%a[j]==0)
				flag+=1;
		}
		if(flag==3){
			lcm=i;
			goto here;
		}
	}
	here:
	cout<<"\nLCM = "<<lcm;
	cout<<"\nMax = "<<max;
	cout<<"\nMultiple All = "<<multiple_all;
	cout<<"\nFlag = "<<flag;
	return 0;
}
