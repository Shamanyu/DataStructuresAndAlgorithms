#include<stdio.h>
#include<stdlib.h>

int main()
{
	unsigned long int jars, operations, counter, candies, starting_jar, ending_jar, sum, average_number;
	scanf("%lu", &jars);
	scanf("%lu", &operations);
	sum = 0;
	for(counter=0;counter<operations;counter++)
	{
		scanf("%lu", &starting_jar);
		scanf("%lu", &ending_jar);
		scanf("%lu", &candies);
		sum += (ending_jar-starting_jar+1)*candies;
	}
	average_number = sum/jars;
	printf("%lu", average_number);
	return 0;
}
