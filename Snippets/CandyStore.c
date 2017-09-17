#include<stdio.h>
#include<stdlib.h>

#define LIMIT 1000000000

long long unsigned int Permutations(int number_of_candies, int to_buy_candies)
{
	long long unsigned int permutations = 1;
	if(to_buy_candies > number_of_candies)
	{
		to_buy_candies = number_of_candies;
	}
	while(to_buy_candies > 0)
	{
		permutations *= number_of_candies;
		if(permutations >= LIMIT)
		{
			permutations %= LIMIT;
		}
		to_buy_candies--;
	}
	return permutations;
}

int main()
{
	int test_cases, counter, number_of_candies, to_buy_candies;
	scanf("%d", &test_cases);
	for(counter=0;counter<test_cases;counter++)
	{
		scanf("%d", &number_of_candies);
		scanf("%d", &to_buy_candies);
		printf("%llu\n", Permutations(number_of_candies, to_buy_candies));
	}
	return 0;
}
