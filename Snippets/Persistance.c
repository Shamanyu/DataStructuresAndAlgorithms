#include<stdio.h>

int main()
{
	long long int digits;
	scanf("%lld", &digits);
	for(counter=0;counter<digits;counter++)
	{
		lower_limit *= 10;
	}
	upper_limit = lower_limit*10;
	best_persistance_value = -1;
	best_persistance_number = -1;
	for(counter=lower_limit;counter<upper_limit;counter++)
	{
		
