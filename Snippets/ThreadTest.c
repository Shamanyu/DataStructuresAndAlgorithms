#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include <pthread.h>

#define THREAD_LIMIT 100000
#define THREAD_MAX 1000000

void* func(void *Data)
{
	int* DataReceived = Data;
	int counter=5;
	while(counter>0)
	{
		printf("\n%d", *DataReceived);
		int *hey = (int*) malloc(sizeof(int)*100000);
		sleep(1);
		free(hey);
		counter--;
	}
}

int main()
{
	pthread_t threads[THREAD_MAX];
	int counter;
	for(counter=0;counter<THREAD_LIMIT;counter++)
	{
		int* counter_again = (int*) malloc(sizeof(int));
		*counter_again = counter+1;
		if(counter>=THREAD_LIMIT)
			pthread_join(threads[counter-THREAD_LIMIT], NULL);
		pthread_create(&threads[counter], NULL, func, (void*) counter_again);
	}
	pthread_exit(NULL);
}
