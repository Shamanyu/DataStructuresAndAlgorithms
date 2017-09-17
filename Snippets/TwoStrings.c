#include<stdio.h>
#include<stdlib.h>
#define MAX 1000
#define NUMBEROFCHARACTERS 26

int character_count[NUMBEROFCHARACTERS];

int CheckCommonSubstring(char* string1, char* string2)
{
	char counter1, counter2;
	counter1 = 0;
	counter2 = 0;
	while(string2[counter1] != '\0')
	{
		if(string1[counter1] > 97)
		{
			character_count[string1[counter1]-97] = 1;
		}
		else
		{
			character_count[string1[counter1]-65] = 1;
		}
		counter1++;
	}
	while(string2[counter2] != '\0')
	{
		if(string2[counter2] > 97)
		{
			if(character_count[string2[counter2]-97])
			{
				return 1;
			}
		}
		else
		{
			if(character_count[string2[counter2]-65])
			{
				return 1;
			}
		}
		counter2++;
	}
	return 0;
}

int main()
{
	int test_cases, counter, counter1;
	char string1[MAX], string2[MAX];
	scanf("%d", &test_cases);
	for(counter=0;counter<test_cases;counter++)
	{
		for(counter1=0;counter1<NUMBEROFCHARACTERS;counter1++)
		{
			character_count[counter1]=0;
		}
		for(counter1=0;counter1<MAX;counter1++)
		{
			string1[counter1]=string2[counter1] = '\0';
		}
		fgets(string1, MAX, stdin);
		fgets(string2, MAX, stdin);
		//printf("Number1%s", string1);
		//printf("Number2%s", string2);
		int result = CheckCommonSubstring(string1, string2);
		if(result)
		{
			printf("YES\n");
		}
		else
		{
			printf("NO\n");
		}
	}
	return 0;
}
