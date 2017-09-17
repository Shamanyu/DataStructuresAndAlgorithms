#include<stdio.h>
#include<stdlib.h>

#define MAX 3

int main()
{
	int a[MAX][MAX];
	int counter1, counter2;
	for(counter1=0;counter1<MAX;counter1++)
	{
		for(counter2=0;counter2<MAX;counter2++)
		{
			printf("\n%p", &a[counter1][counter2]);
		}
	}
	return 0;
}
