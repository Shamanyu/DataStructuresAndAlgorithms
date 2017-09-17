#include<stdio.h>
#include<stdlib.h>

int CalculatePosition(int number_of_balls, int ball_number)
{
	if(ball_number<(number_of_balls-1)/2)
	{
		return ball_number*2+1;
	}
	else
	{
		return (number_of_balls-1-ball_number)*2;
	}
}

int main()
{
	int test_cases, number_of_balls, ball_number, counter;
	scanf("%d", &test_cases);
	for(counter=0;counter<test_cases;counter++)
	{
		scanf("%d", &number_of_balls);
		scanf("%d", &ball_number);
		printf("%d\n", CalculatePosition(number_of_balls, ball_number));
	}
	return 0;
}
