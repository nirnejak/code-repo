#include <iostream>
using namespace std;
int main(){
    int choice,n1,n2,n3,n4,max;
    cout<<"MENU";
    cout<<"\n1.Maximum Number Between 2 Numbers";
    cout<<"\n2.Maximum Number Between 3 Numbers";
    cout<<"\n3.Maximum Number Between 4 Numbers";
    cout<<"\nEnter Your Choice : ";
    cin>>choice;
    switch(choice){
        case 1:
            cout<<"Enter First Number : ";
            cin>>n1;
            cout<<"Enter Second Number : ";
            cin>>n2;
            if(n1>n2)
                cout<<"\nFirst Number is Greater than Second Number";
            if(n2>n1)
                cout<<"\nSecond Number is Greater than First Number";
            if(n2==n1)
                cout<<"\nBoth Numbers are equal";
            break;
        case 2:
            cout<<"Enter First Number : ";
            cin>>n1;
            cout<<"Enter Second Number : ";
            cin>>n2;
            cout<<"Enter Third Number : ";
            cin>>n3;
            if(n1>n2 && n1>n3)
                cout<<"\nFirst Number is Greater than Second and Third Number";
            if(n2>n1 && n2>n3)
                cout<<"\nSecond Number is Greater than First and Third Number";
            if(n3>n1 && n3>n2)
                cout<<"\nThird Number is Greater than First and Second Number";
            if(n2==n1 && n2==n3)
                cout<<"\nAll Numbers are equal";
                break;
            case 3:
            cout<<"\nEnter First Number : ";
            cin>>n1;
            cout<<"\nEnter Second Number : ";
            cin>>n2;
            cout<<"\nEnter Third Number : ";
            cin>>n3;
            cout<<"\nEnter Fourth Number : ";
            cin>>n4;
            if(n1>n2 && n1>n3 && n1>n4)
                cout<<"\nFirst Number is Greater than Second,Third and Fourth Number";
            if(n2>n1 && n2>n3 && n2>n4)
                cout<<"\nSecond Number is Greater than First,Third and Fourth Number";
            if(n3>n1 && n3>n2 && n3>n4)
                cout<<"\nThird Number is Greater than First,Second and Fourth Number";
            if(n4>n1 && n4>n2 && n4>n3)
                cout<<"\nThird Number is Greater than First,Second and Third Number";
            if(n2==n1 && n2==n3 && n2==n4)
                cout<<"\nAll Numbers are equal";
                break;
    }
    return 0;
}