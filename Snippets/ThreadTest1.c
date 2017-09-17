#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>

#define MAX 99999

void * thread(void* i)
{
    sleep(100);//make the thread still alive
    return 0;
}

int main()
{
    pthread_t thrd[MAX];
    int i, err;
    for(i=0;i<MAX;i++)
    {
        err=pthread_create(&thrd[i],NULL,thread,(void*)i);
        if(err!=0)
	{
	    printf("\nThread creation failed: %d withh error code %d", i, err);
            break;
	}
    }
    return 0;
}
