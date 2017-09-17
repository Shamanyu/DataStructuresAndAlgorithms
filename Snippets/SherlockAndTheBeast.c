#include<stdio.h>

int main()
{
	int T, N;
	int numberOfThrees, numberOfFives, flag, temp;
	int counter1;
	scanf("%d", &T);
	for(counter1=0;counter1<T;counter1++)
	{
		scanf("%d", &N);
		numberOfFives = numberOfThrees = 0;
		flag = 0;
		temp = N;
		while(temp > 0)
		{
			if(temp % 3 != 0)
			{
				numberOfThrees += 5;
				temp -= 5;
			}
			else
			{
				numberOfFives = temp;
				flag = 1;
				break;
			}
		}
		if(temp == 0)
		{
			flag = 1;
		}
		if(flag)
		{
			while(numberOfFives > 0)
			{
				printf("5");
				numberOfFives--;
			}
			while(numberOfThrees > 0)
			{
				printf("3");
				numberOfThrees--;
			}
		}
		else
		{
			printf("-1");
		}
		printf("\n");
	}
	return 0;
}
