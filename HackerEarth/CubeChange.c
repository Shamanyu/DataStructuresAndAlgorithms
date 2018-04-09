#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main()
{
	int test_cases, counter;
	unsigned long long int sides;
	scanf("%d", &test_cases);
	for(counter=0;counter<test_cases;counter++)
	{
		scanf("%llu", &sides);
		if (sides==1)
		{
			printf("%d\n", 1);
		}
		else
		{
			printf("%llu\n", 6*sides*sides-12*sides+8);
		}
	}
	return 0;
}
