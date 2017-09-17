#include<stdio.h>
#include "BigIntegerLibrary.hh"

BigInteger computeFactorials(int input)
{
	if(input > 1)
	{
		return input * computeFactorial(input-1);
	}
	else
	{
		return 1;
	}
}

int main()
{
	BigInteger result;
	int input, counter;
	scanf("%d", &input);
	result = ComputeFactorials(input);
	printf("%d", result);
	return 0;
}
