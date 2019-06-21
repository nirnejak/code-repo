#include <iostream>
using namespace std;
int main(){
    int num,check=0,temp;
    cout<<"Enter Number : ";
    cin>>num;
    temp=num;
    while(num){
        check=check*10+num%10;
        num/=10;
    }
    if(check==temp)
        cout<<"Number is Palindrome Number";
    else
        cout<<"Number is not Palindrome Number";
    return 0;
}