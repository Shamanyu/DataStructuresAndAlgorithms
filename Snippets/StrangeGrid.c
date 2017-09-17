#include<stdio.h>
#include<stdlib.h>

#define NUMBER_OF_COLUMNS 5

long long int FindNumber(long long int row, long long int column)
{
	if(row%2 != 0)
	{
		return (row/2)*10+2*(column-1);
	}
	else
	{
		return row/2*10-2*(NUMBER_OF_COLUMNS-column+1)+1;
	}
}

int main()
{
	long long int row, column;
	scanf("%lld", &row);
	scanf("%lld", &column);
	printf("%lld", FindNumber(row, column));
	return 0;
}
