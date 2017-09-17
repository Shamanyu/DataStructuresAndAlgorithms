#include<stdio.h>
#define MAX 1000

int main()
{
	int N, lengthCount[MAX+1], sticksLeft;
	int length, counter;
	scanf("%d", &N);
	sticksLeft = N;
	for(counter=0;counter<MAX+1;counter++)
	{
		lengthCount[counter]=0;
	}
	for(counter=0;counter<N;counter++)
	{
		scanf("%d", &length);
		lengthCount[length]++;
	}
	for(counter=0;counter<MAX+1;counter++)
	{
		if(lengthCount[counter] > 0)
		{
			printf("%d\n", sticksLeft);
			sticksLeft = sticksLeft - lengthCount[counter];
		}
	}
	return 0;
}
