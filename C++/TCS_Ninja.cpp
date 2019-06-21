#include <iostream>
using namespace std;

int pow(int n, int p){
    int i, ans=1;
    for(i=0;i<p;i++){
        ans*=n;
    }
    return ans;
}

int main(){
    int n;
    cin>>n;
    if(n%2==0)
        cout<<pow(2, n/2-1)<<"\t";
    else
        cout<<pow(3, n/2)<<"\t";
    return 0;
}