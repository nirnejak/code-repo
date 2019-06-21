#include <iostream>
using namespace std;

long int fact(int x){
    int i,n=1;
    for(i=1;i<=x;i++)
        n*=i;
    return n;
}
int main(){
    int num;
    long ans;
    cout<<"Enter Number : ";
    cin>>num;
    ans=fact(num);
    cout<<"Factorial of "<<num<<" is "<<ans;
    return 0;
}