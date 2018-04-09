#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define MAX 100000
#define COMPANY_LENGTH_MAX 100

char companies[MAX][COMPANY_LENGTH_MAX];
long int sales_count[MAX];

int main()
{
	long int N, counter, inner_counter, limit, max_count;
	char company[COMPANY_LENGTH_MAX];
	limit = 0;
	max_count = 0;
	scanf("%ld", &N);
	for(counter=0;counter<N;counter++)
	{
		scanf("%s", company);
		for(inner_counter=0;inner_counter<limit;inner_counter++)
		{
			if(strcmp(companies[inner_counter], company) == 0)
			{
				sales_count[inner_counter] += 1;
				break;
			}
		}
		if(inner_counter == limit)
		{
			strcpy(companies[inner_counter], company);
			sales_count[inner_counter] = 1;
			limit++;
		}
	}
	for(counter=0;counter<limit;counter++)
	{
		if(sales_count[counter] > max_count || (sales_count[counter] == max_count && strcmp(companies[counter], company) < 0))
		{
			strcpy(company, companies[counter]);
			max_count = sales_count[counter];
		}
	}
	puts(company);
}
