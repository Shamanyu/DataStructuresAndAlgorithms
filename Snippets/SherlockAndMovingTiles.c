#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main()
{
	long long unsigned int length, speed1, speed2, queries, counter, area_in_common;
	double side_in_common, length_in_common, length_moved, time;
	scanf("%llu", &length);
	scanf("%llu", &speed1);
	scanf("%llu", &speed2);
	scanf("%llu", &queries);
	for(counter=0;counter<queries;counter++)
	{
		scanf("%llu", &area_in_common);
		side_in_common = sqrt((double) (area_in_common));
		length_in_common = sqrt(2)*side_in_common;
		length_moved = length*sqrt(2)-length_in_common;
		time = (length_moved)/(speed2-speed1);
		printf("%lf\n", time);
	}
	return 0;
}
