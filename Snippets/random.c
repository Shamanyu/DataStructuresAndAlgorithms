#include<stdio.h>
#include<time.h>
#define LIMIT 10000

int main()
{
	srand(time(NULL));
	int lower,upper,counter1,counter2,counter3,temp,max;
	for(counter3=0;counter3<LIMIT;counter3++)
	{
		max=0;
		lower = rand() % 10000;
		upper = rand() % 99999;
		if(lower > upper)
		{
			lower = upper + lower;
			upper = lower - upper;
			lower = lower - upper;
		}
		for(counter1=lower;counter1<=upper;counter1++)
		{
			for(counter2=lower;counter2<=upper;counter2++)
			{
				temp = counter1^counter2;
				if (temp > max)
				{
					max=temp;
				}
			}
		}
		printf("%d\n",max);
	}
	return 0;
}