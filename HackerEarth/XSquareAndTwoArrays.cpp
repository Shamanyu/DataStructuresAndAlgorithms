#include<stdio.h>
#include<stdlib.h>
#define MAX 100000

unsigned long long int A[MAX];
unsigned long long int B[MAX]; 
unsigned long long int ASum[MAX];
unsigned long long int BSum[MAX];

long long int N, Q;

void constructASum()
{
	long long int position;
	for(position=0;position<N;position++)
	{
		if(position > 1)
		{
			ASum[position] = A[position] + B[position-1] + ASum[position-2];
		}
		else if(position == 1)
		{
			ASum[position] = A[position] + B[position-1];
		}
		else
		{
			ASum[position] = A[position];
		}
	}
}

void constructBSum()
{
	unsigned long long int position;
        for(position=0;position<N;position++)
        {
                if(position > 1)
                {
                        BSum[position] = B[position] + A[position-1] + BSum[position-2];
                }
                else if(position == 1)
                {
                        BSum[position] = B[position] + A[position-1];
                }
                else
                {
                        BSum[position] = B[position];
                }
	}
}

int main()
{
	int matrix;
	long long int counter, L, R;
	unsigned long long int end;
	scanf("%lld", &N);
	scanf("%lld", &Q);
	for(counter=0;counter<N;counter++)
	{
		scanf("%llu", &A[counter]);
	}
	for(counter=0;counter<N;counter++)
	{
		scanf("%llu", &B[counter]);
	}
	constructASum();
	constructBSum();
	for(counter=0;counter<N;counter++)
	{
		scanf("%d", &matrix);
		scanf("%lld", &L);
		scanf("%lld", &R);
		if(matrix == 1)
		{
			if((R-L)%2 == 0)
			{	
				end = ASum[R-1];
			}
			else
			{
				end = BSum[R-1];
			}
			if(L == 1)
			{
				printf("%llu\n", end);
			}
			else
			{
				printf("%llu\n", end-BSum[L-1-1]);
			}
		}
		else
		{
			if((R-L)%2 == 0)
			{
				end = BSum[R-1];
			}
			else
			{
				end = ASum[R-1];
			}
			if(L == 1)
			{
				printf("%llu\n", end);
			}
			else
			{
				printf("%llu\n", end-ASum[L-1-1]);
			}
		}
	}
	return 0;
}
