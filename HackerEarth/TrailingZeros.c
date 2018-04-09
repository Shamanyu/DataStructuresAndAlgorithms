#include<stdio.h>
#include<stdlib.h>

int main()
{
	int number, trailing_zeros, divider, adder;
	scanf("%d", &number);
	trailing_zeros=0;
	divider=5;
	adder=number/divider;
	while(adder>0)
	{
		trailing_zeros+=adder;
		divider*=5;
		adder=number/divider;
	}
	printf("%d", trailing_zeros);
	return 0;
}
