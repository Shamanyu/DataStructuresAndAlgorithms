#include<stdio.h>
#include<stdlib.h>

long long unsigned int number_of_pieces(long long int cuts)
{
	if(cuts%2 == 0)
	{
		return cuts/2*cuts/2;
	}
	else
	{
		return cuts/2*(cuts/2+1);
	}
}

int main()
{
	int test_cases, counter;
	long long int cuts;
	scanf("%d", &test_cases);
	for(counter=0;counter<test_cases;counter++)
	{
		scanf("%lld", &cuts);
		printf("%llu", number_of_pieces(cuts));
	}
	return 0;
}
