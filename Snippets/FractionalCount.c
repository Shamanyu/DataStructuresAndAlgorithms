#include<stdio.h>

int main()
{
	int N;
	int counter, input;
	float posRatio, negRatio, zeroRatio;
	scanf("%d", &N);
	for(counter=0;counter<N;counter++)
	{
		scanf("%d", &input);
		if(input > 0)
		{
			posRatio++;
		}
		else if(input < 0)
		{
			negRatio++;
		}
		else
		{
			zeroRatio++;
		}
	}
	posRatio = posRatio/N;
	negRatio = negRatio/N;
	zeroRatio = zeroRatio/N;
	printf("%f\n", posRatio);
	printf("%f\n", negRatio);
	printf("%f\n", zeroRatio);
	return 0;
}
