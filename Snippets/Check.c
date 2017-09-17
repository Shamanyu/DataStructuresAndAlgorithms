#include<stdio.h>
#include<stdlib.h>

int main()
{
	int N1=2;
	int N2=2;
	int X1=2;
	int Y1=1;
	int X2=1;
	int Y2=1;
	printf("%d\n",( (X1 - 1) * N2 + N2 -Y1) * N1 * N2 + (X2 - 1) * N2 + N2 - Y2 + 1);
	return 0;
}
