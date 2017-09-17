#include<stdio.h>

long long int factorial(long long int num)
{
	long long int res;
	if(num!=0)
	{
		res=num*factorial(num-1);
		return res;
	}
	else
	{
		return 1;
	}
}

int main()
{
	long long int num,result;
	printf("\nEnter number:\t");
	scanf("%lld",&num);
	result=factorial(num);
	printf("\nHere is the result: %lld\n",result);
	return 0;
}
