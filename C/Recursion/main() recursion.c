#include <stdio.h>
int a=2;
int main(){
	if(a<10){
		a++;
		printf("\nHi there");
		main();
	}
	else{
		return 0;
	}
}
