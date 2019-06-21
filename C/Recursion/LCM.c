#include <stdio.h>
int num=1;
int lcm_fun(int m,int a[]){
	int flag=0,j;
	for(j=0;j<3;j++){
		if(num%a[j]==0)
			flag++;
	}
	if(flag==3){
		return num;
	}
	else{
		num++;
		return lcm_fun(m,a);
	}
}
int main(){
	int a[3],mul=1,lcm,i;
	printf("Enter Numbers : ");
	for(i=0;i<3;i++)
		scanf("%d",&a[i]);
	for(i=0;i<3;i++)
		mul*=a[i];
	//calling function
	lcm=lcm_fun(mul,a);
	
	printf("LCM is %d",lcm);
	return 0;
}
