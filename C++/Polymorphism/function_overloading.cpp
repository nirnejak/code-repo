#include <iostream>
using namespace std;

int add(int a, int b);
int add(int a, int b, int c);
int add(int a, int b, int c, int d);

int main(){
    cout<<add(1,2)<<endl;
    cout<<add(1,2,3)<<endl;
    cout<<add(1,2,4);
    return 0;
}

int add(int a, int b){
    return a+b;
}
int add(int a, int b, int c){
    return a+b+c;
}
int add(int a, int b, int c, int d){
    return a+b+c+d;
}