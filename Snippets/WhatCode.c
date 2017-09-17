#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#define MAX 1000000
#define LIMIT 100000

void initializeCount(int *array)
{
	int counter;
	for(counter=0;counter<MAX;counter++)
	{
		array[counter] = 0;
	}
}

int main()
{
	int count[MAX], random_number, counter, max, min;
	initializeCount(count);
	max=0;
	min=MAX;
	srand(time(NULL));
	for(counter=0;counter<MAX;counter++)
	{
		random_number = (int) (rand()%LIMIT) + 1;
		count[random_number]++;
	}
	for(counter=1;counter<=LIMIT;counter++)
	{
		printf("%d %d\n", counter, count[counter]);
		if(count[counter]>max)
		{
			max=count[counter];
		}
		if(count[counter]<min)
		{
			min=count[counter];
		}
	}
	printf("Max is %d and min is %d\n",max,min);
	return 0;
}	
