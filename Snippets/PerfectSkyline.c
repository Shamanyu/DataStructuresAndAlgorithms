#include<stdio.h>
#include<stdlib.h>

#define MAX 100

int main()
{
	int number_of_buildings, counter, heights[MAX], result;
	result = 0;
	scanf("%d", &number_of_buildings);
	for(counter=0;counter<number_of_buildings;counter++)
	{
		scanf("%d", &heights[counter]);
	}
	if(number_of_buildings%2 == 1){
	for(counter=0;counter<=number_of_buildings/2;counter++)
	{
		if(counter == number_of_buildings/2 || (heights[counter] == heights[number_of_buildings-counter-1] && (counter==0 || heights[counter] > heights[counter-1])))
		{
			result = 1;
		}
		else
		{
			result =0;
			break;
		}
	}}
	if(heights[number_of_buildings/2] < heights[number_of_buildings/2-1])
	{
		result = 0;
	}
	if(result)
	{
		printf("Perfect");
	}
	else
	{
		printf("Not perfect");
	}
	return 0;
}
