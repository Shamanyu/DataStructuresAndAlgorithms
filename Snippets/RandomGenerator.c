#include<stdio.h>
#include <time.h>
#include <stdlib.h>
#include<unistd.h>
#define MAX 10000

int main()
{
	int counter,temp;
	int sameer, abhishek, shubham, mahesh;
	sameer = abhishek = shubham = mahesh = 0;
	printf("\nWill display count after every 25 chances\n");
	for(counter=0;counter<MAX;counter++)
	{
		temp = rand() % 4 +1;
		if (temp == 1)
		{
			abhishek++;
		}
		else if(temp == 2)
		{
			sameer++;
		}
		else if(temp == 3)
		{
			mahesh++;
		}
		else if(temp ==4)
		{
			shubham++;
		}
		else
		{
			printf("\nNo one's gonna rent it up");
		}
		//printf("%d\n",temp);
		if((counter+1)%25 == 0)
		{
			sleep(1);
			printf("After %d chances: Sameer = %d, Abhishek = %d, Shubham = %d, Mahesh = %d\n",counter+1, sameer, abhishek, shubham, mahesh);}
	}
	return 0;
}
