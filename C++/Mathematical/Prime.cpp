#include <iostream>
using namespace std;
int main(){
    int num,i;
    cout<<"Enter Number to Check : ";
    cin>>num;
    for(i=2;i<num;i++){
        if(num%i==0){
            cout<<"The number is not prime";
            break;
        }
    }
    if(i>=num)
        cout<<"The number is prime";
    return 0;
}
