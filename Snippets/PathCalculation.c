#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define TIME_FOR_ONE 27
#define TIME_FOR_TWO 42
#define TIME_FOR_MAX 12
#define COST_OF_TURN 4000

int time(int distance){
	if(distance == 0)
		return 0;
	else if(distance < 244){
		return (distance * TIME_FOR_ONE);
	}
	else{
		return (int)(TIME_FOR_TWO*100 + (distance - 244)*TIME_FOR_MAX);
	}
	return 0;
}

int main()
{
	printf("%d\n, %d\n, %d\n, %d\n, %d\n, %d\n, %d\n", time(0), time(100), time(243), time(244), time(245), time(300), time(301));
	printf("\n\n\n%d, \n%d, \n%d \n%d\n", time(122), time(244), time(366), time(488));
	return 0;
}