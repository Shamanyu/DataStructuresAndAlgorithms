#include<stdio.h>
#include<stdlib.h>

typedef unsigned char byte;

typedef struct
{
	byte length1;
	byte length2;
	byte length3;
	byte length4;
	int s;
	int p;
	int x;
	int y;
	int ShortestPathLength;
}RetString;

int main()
{
	long length;
	RetString ReturnValue;
	length = sizeof(RetString);
	ReturnValue.length1 = (length >> 24) & 0xff;
	ReturnValue.length2 = (length >> 16) & 0xff;
	ReturnValue.length3 = (length >> 8) & 0xff;
	ReturnValue.length4 = length & 0xff;
	ReturnValue.s = 1;
	ReturnValue.p = 1;
	ReturnValue.x = 2;
	ReturnValue.y = 2;
	ReturnValue.ShortestPathLength = 100;
	printf("\n%lu\n%lu\n%lu", sizeof(byte), sizeof(int), sizeof(RetString));
	return 0;
}
