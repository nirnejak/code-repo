#include <iostream>
#include <cmath>
using namespace std;
int main(){
    int num,sum=0,temp;
    cout<<"Enter Number : ";
    cin>>num;
    temp=num;
    while(num){
        sum+=pow(num%10,3);
        num=num/10;
    }
    if(sum==temp)
        cout<<"Number is Armstrong Number";
    else
        cout<<"Number is not Armstrong Number";
    return 0;
}