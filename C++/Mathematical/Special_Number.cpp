#include <iostream>
using namespace std;
int main(){
    int i,num,sum=0,temp,temp2;
    cout<<"Enter Number : ";
    cin>>num;
    temp2=num;
    while(num){
        temp=num%10;
        for(i=1;i<temp;i++)
        {
            if(temp%i==0)
                sum+=i;
        }
        num=num/10;
    }
    if(sum==temp2)
        cout<<"Number is Special Number";
    else
        cout<"Number is Not Special Number";
    return 0;
}