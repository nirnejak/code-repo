/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include<stdio.h>
#include<conio.h>
void main(){
    int a[3][3],i,j,k=1,l,n,amt;
    for(i=0;i<3;i++)
        for(j=0;j<3;j++)
        a[i][j]=0;
    while(k!=0)
    {
        printf("Enter the amount");
        scanf("%d",&amt);
        printf("Enter the person");
        scanf("%d",&n);
        amt=amt/3;
        for(i=0;i<3;i++){
            if(n!=i)
            {
                if(a[n][i]==0 &&  a[i][n]==0)
                a[i][n]=amt;
                else if(a[n][i]==0 &&  a[i][n]!=0){
                    if(amt>a[i][n])
                    {
                        a[n][i]=amt-a[i][n];
                        a[i][n]=0;
                    }
                    else
                        a[i][n]-=amt;
                }
                else if(a[n][i]!=0 &&  a[i][n]==0){
                    if(amt>a[n][i])
                    {
                        a[i][n]=amt-a[n][i];
                        a[n][i]=0;
                    }
                    else
                        a[n][i]-=amt;
                }
            }
        }
         for(i=0;i<3;i++){
             printf("\n");
        for(j=0;j<3;j++){
            printf("\t%d",a[i][j]);
            }
            }
            printf("continue? press 1");
            scanf("%d",&k);
    }
    getch();
    
}
