#include <stdio.h>
int main()
{
	int a[5],b,e,m,i,n;
	printf("Enter five Elements : \n");
	for (i = 0; i < 5; ++i)
		scanf("%d",&a[i]);
	printf("Enter the Element you want to search : \n");
	scanf("%d",&n);
	b=0;
	e=4;
	while(b<=e){
		m=(b+e)/2;
		if (a[m]==n){
			m=m+1;
			printf("pos %d\n",m);
			break;
		}
		else {
			if (a[m]<n)
				b=m+1;
			else
				e=m-1;
		}
		if (b>e) {
			printf("Not Found\n");
		}
	}
	return 0;
}