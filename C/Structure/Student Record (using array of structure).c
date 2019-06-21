#include <stdio.h>

struct student{
	int rollno;
	char name[20];
	int marks;
};

int main(){
	int i,desc_var=50;
	struct student stu_var[5];
	printf("Enter Details of Students\n");
	for(i=0;i<5;i++){
		printf("\nEnter Roll Number : ");
		scanf("%d",&stu_var[i].rollno);
		printf("\nEnter Name of the Student : ");
		scanf("%s",&stu_var[i].name);
		printf("\nEnter Marks : ");
		scanf("%d",&stu_var[i].marks);
	}
	for(i=0;i<5;i++){
		printf("\n");
		if(stu_var[i].marks>desc_var){
			printf("\nRoll No %d",stu_var[i].rollno);
			printf("\nName %s",stu_var[i].name);
			printf("\nMarks",stu_var[i].marks);
		}
	}
	return 0;
}
