#include <stdio.h>
#include <string.h>

int pop(char x[],int m){
    int a;
    a=strlen(x)-m;
    if(x[a]>=97 && x[a]<=122)
        a=x[a]-96;
    else if(x[a]>=65 && x[a]<=90)
        a=x[a]-64;
    else if(x[a]=='0')
        return 0;
    return a;
}

int main(){
    char st[20],st2[20],a,i;
    int test,num=2;
    gets(st);
    test=pop(st,num);
    printf("\n%d",test);
    for(i=0;i<strlen(st);i++)
        st2[i]=st[i];
    a=strcmp(st,st2);
    printf("\n\n%d",a);
    return 0;
}