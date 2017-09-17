#include<stdio.h>
#include<stdlib.h>

#define MAX 100
#define USE 30

typedef unsigned char byte;

typedef struct
{
	byte length1;
	byte length2;
	byte length3;
	byte length4;
	int a;
	int b;
	int c;
	int d;
	int value[MAX];
}TEST;

int write_exact(byte *buffer, int length)
{
  int count, wrote = 0;
  do
  {
    if ((count = write(1, buffer+wrote, length-wrote)) <= 0)
      return (count);
    wrote += count;
  }while (wrote<length);
 // return (length);
}

void func(int* c)
{
	int counter;
	for(counter=0;counter<USE;counter++)
	{
		c[counter] = counter + 5;
	}
}

int main()
{
	int counter;
	long length;
	TEST test;
	length = sizeof(TEST) - sizeof(byte)*4;
	test.length1 = (length >> 24) & 0xff;
	test.length2 = (length >> 16) & 0xff;
	test.length3 = (length >> 8) & 0xff;
	test.length4 = length & 0xff;
	test.a = 1;
	test.b = 2;
	test.c = 3;
	test.d = 3; 
	func(test.value);
	printf("%lu", sizeof(byte)*4 + sizeof(int)*4 + sizeof(int)*test.c*test.d);
	//write_exact((byte*)&test, sizeof(byte)*4 + sizeof(int)*4 + sizeof(int)*test.c*test.d);
	return 0;
}

