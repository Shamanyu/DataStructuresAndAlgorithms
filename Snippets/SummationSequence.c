#include<stdio.h>
#include<stdlib.h>

#define LIMIT 1000000007

long long  unsigned int CalculateSum(long long unsigned int input)
{
	if(input > LIMIT)
	{
		input %= (LIMIT);
	}
	return (input*input) % (LIMIT);
}

int main()
{
	int test_cases, counter;
	long long unsigned int input;
	scanf("%d", &test_cases);
	for(counter=0;counter<test_cases;counter++)
	{
		scanf("%llu", &input);
		printf("%llu\n", CalculateSum(input));
	}
	return 0;
} 
