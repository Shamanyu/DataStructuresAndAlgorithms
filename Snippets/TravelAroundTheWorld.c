#include<stdio.h>

#define MAX 100000

long long int N, a[MAX], b[MAX], c[MAX];
long long int capacity;

long long int addOne(long int pos)
{
	if(pos < N-1)
	{
		return pos + 1;
	}
	else
	{
		return 0;
	}
}

long long int subtractOne(long int pos)
{
	if(pos > 0)
	{
		return pos-1;
	}
	else
	{
		return N-1;
	}
}	

int cascadeBack(long int start_pos)
{
	long long int adder, end_pos, curr_pos;
	adder = c[start_pos];
	end_pos = subtractOne(start_pos);
	curr_pos = start_pos;
	if(c[curr_pos] + b[curr_pos] > capacity)
	{
		return 0;
	}
	while (end_pos != start_pos)
	{
		if(c[curr_pos] > 0)
		{
			c[end_pos] += adder;
			if(c[end_pos] <= 0)
			{
				break;
			}
			else if(c[end_pos] + b[end_pos] > capacity)
			{
				return 0;
			}
			end_pos = subtractOne(end_pos);
			curr_pos = subtractOne(curr_pos);
		}
	}
	return 1;
}

int main()
{
	int still_possible;
	long long int counter, result;
	result = 0;
	still_possible = 1;
	scanf("%lld", &N);
	scanf("%lld", &capacity);
	for(counter=0;counter<N;counter++)
	{
		scanf("%lld", &a[counter]);
		if(a[counter] > capacity)
		{
			a[counter] = capacity;
		}
	}
	for(counter=0;counter<N;counter++)
	{
		scanf("%lld", &b[counter]);
		c[counter] = b[counter] - a[counter];
		if(c[counter] >  capacity)
		{
			still_possible = 0;
		}
	}
	if(still_possible)
	{
		for(counter=0;counter<N;counter++)
		{
			if(c[counter] > 0)
			{
				still_possible = cascadeBack(counter);
				if(!still_possible)
				{
					break;
				}
			}
		}
	}
	if(still_possible)
	{
		for(counter=0;counter<N;counter++)
		{
			if(c[counter] <= 0)
			{
				result++;
			}
		}
	}
	printf("%lld",result);
	return 0;
}
