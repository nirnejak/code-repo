#include <iostream>
using namespace std;

int main(){
    int m=3,n=3;
    int a[m][n],b[m][n],mul[m][n];
    cout<<"Enter 1st Matrix\n";
    for(int i=0;i<m;i++) {
        for(int j=0;j<n;j++)
            cin>>a[i][j];
    }
        
    cout<<"Enter 2nd Matrix\n";
    for(int i=0;i<m;i++) {
        for(int j=0;j<n;j++)
            cin>>b[i][j];
    }

    //calculation
	for(int i=0;i<3;i++) {
		for(int j=0;j<3;j++){	
            mul[i][j]=0;
			for(int k=0;k<3;k++)
			    mul[i][j]+=a[i][k]*b[k][j];
		}
	}

    //output
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++)
            cout<<mul[i][j]<<"\t";
        cout<<endl;
    }
    return 0;
}