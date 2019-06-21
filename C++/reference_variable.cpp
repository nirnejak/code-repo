#include <iostream>
using namespace std;

int main(){
    
    int total=100;
    int &sum=total;
    cout<<"Sum is "<<sum<<endl;
    total++;
    cout<<"Sum is "<<sum<<endl;
    sum++;
    cout<<"Total is "<<total;
    //both will share same memory space
    return 0;
}