#include<stdio.h>
#include<stdlib.h>

int NumberOfHandShakes(int number_of_people)
{
	return (number_of_people*(number_of_people-1))/2;
}

int main()
{
	int test_cases, number_of_people, counter;
	scanf("%d", &test_cases);
	for(counter=0;counter<test_cases;counter++)
	{
		scanf("%d", &number_of_people);
		printf("%d\n", NumberOfHandShakes(number_of_people));
	}
	return 0;
}
