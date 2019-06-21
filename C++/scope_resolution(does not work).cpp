#include <iostream>
using namespace std;

int m=10;

int main(){
    int m=20;
    {

    
    do{
        int k;
        k=m;
        int m=30;

        cout<<k<<endl;
        cout<<m<<endl;
        cout<<::m<<endl;
    }while(0);
    }
    cout<<m<<endl;
    cout<<::m;
    return 0;
}