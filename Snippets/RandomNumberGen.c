#include<stdio.h>
#include<stdlib.h>

float CalculateProbability(float number1, float number2, float max_acceptable)
{
	int counter1, counter2;
	float probability = 0;
	counter2 = number2;
	for(counter1=0;counter1<=number1;counter1++)
	{
		while(counter1+counter2 >= max_acceptable && counter2 >= 0)
		{
			counter2--;
		}
		probability += (1/(number1+1))*((counter2+1)/(number2+1));
	}
	return probability;
}

int main()
{
	int test_cases, counter;
	float input1, input2, max_acceptable; 
	scanf("%d", &test_cases);
	for(counter=0;counter<test_cases;counter++)
	{
		scanf("%f", &input1);
		scanf("%f", &input2);
		scanf("%f", &max_acceptable);
		printf("%f\n", CalculateProbability(input1, input2, max_acceptable));
	}
	return 0;
}
