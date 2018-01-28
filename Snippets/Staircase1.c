#include<stdio.h>

int main()
{
	int steps,spaces;
	int counter,counter2;;
	scanf("%d", &steps);
	for(counter=0;counter<steps;counter++)
	{
		spaces = steps - counter - 1 ;
		for(counter2=0;counter2<spaces;counter2++)
		{
			printf(" ");
		}
		for(counter2=0;counter2<steps-spaces;counter2++)
		{
			printf("#");
		}
		printf("\n");
	}
	return 0;
}
