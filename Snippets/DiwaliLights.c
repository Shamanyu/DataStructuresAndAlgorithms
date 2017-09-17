#include<stdio.h>
#include<stdlib.h>

#define MODULO_LIMIT 100000

long int CalculateNumberOfPatterns(long int number_of_lights)
{
	long int number_of_patterns = 2;
	if(number_of_lights == 0)
	{
		return 0;
	}
	while(number_of_lights>1)
	{
		number_of_patterns *= 2;
		if(number_of_patterns>MODULO_LIMIT)
		{
			number_of_patterns %= MODULO_LIMIT;
		}
		number_of_lights--;
	}
	number_of_patterns--;
	return number_of_patterns;
}

int main()
{
	int test_cases, counter;
	long int number_of_lights;
	scanf("%d", &test_cases);
	for(counter=0;counter<test_cases;counter++)
	{
		scanf("%ld", &number_of_lights);
		printf("%ld\n", CalculateNumberOfPatterns(number_of_lights));
	}
	return 0;
}
