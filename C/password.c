#include<stdio.h>
#include<conio.h>
void main(){
	char p1,p2,p3,p4,p5;
	printf("Hi there\nEnter Password : ");
	p1=getch();
	printf("*");
	p2=getch();
	printf("*");
	p3=getch();
	printf("*");
	p4=getch();
	printf("*");
	p5=getch();
	printf("*");
	if(p1=='1' && p2=='2' && p3=='3' && p4=='4' && p5=='5')
		printf("\nCorrect Password");
	else
		printf("\nIncorrect Password");
}
