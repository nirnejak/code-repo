#include <stdio.h>
#include <string.h>
struct movie
{
	char name[20];
	char name_hero[20];
	char name_heroine[20];
	char name_director[20];
};

int main(){
	int i;
	struct movie mov[10];
	for(i=0;i<10;i++){
		printf("\nEnter Name of Movie %d : ", i+1);
		gets(mov[i].name);
		printf("\nEnter Name of Hero of Movie %d : ", i+1);
		gets(mov[i].name_hero);
		printf("\nEnter Name of Heroine of Movie %d : ", i+1);
		gets(mov[i].name_heroine);
		printf("\nEnter Name of Director of Movie %d : ", i+1);
		gets(mov[i].name_director);
	}
	char direct[20]="Silver Spilberg";
	for(i=0;i<10;i++){
		if(!(strcmp(mov[i].name_director,direct))){
			printf("\nMovie %s",mov[i].name);
			printf("\nHero of Movie %s",mov[i].name_hero);
			printf("\nHeroine of Movie %s",mov[i].name_heroine);
			printf("\nDirector of Movie %s",mov[i].name_director);
		}
	}
	return 0;
}