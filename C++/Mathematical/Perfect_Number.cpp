#include <iostream>
using namespace std;

long int fact(int x){
    int i,n=1;
    for(i=1;i<=x;i++)
        n*=i;
    return n;
}
int main(){
    int num,sum=0,temp;
    cout<<"Enter Number : ";
    cin>>num;
    temp=num;
    while(num){
        sum+=fact(num%10);
        num=num/10;
    }
        if(sum==temp)
            cout<<"Number is Perfect";
        else
            cout<<"Number is not Perfect";
    return 0;
}