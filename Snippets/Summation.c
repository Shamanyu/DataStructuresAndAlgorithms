#include<stdio.h>

int main()
{
	long long int N,sum,input,counter;
	scanf("%lld",&N);
	sum=0;
	for (counter=0;counter<N;counter++)
	{
		scanf("%lld", &input);
		sum+=input;
	}
	printf("%lld",sum);
	return 0;
}
