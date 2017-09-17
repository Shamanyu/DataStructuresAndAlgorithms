#include<stdio.h>
#include <time.h>
#include <stdlib.h>
#include<unistd.h>

int main()
{
	int user_move,computer_move,user_wins,computer_wins,draws;
	char user_choice,trash;
	user_wins=computer_wins=draws=0;
	while(1)
	{
		computer_move = rand() % 3 + 1;
		printf("The computer is deciding it's move.");
		sleep(1);
		printf("\nThe computer has chosen it's move. Please enter 'R', 'P' or 'S':\t");
		scanf("%c", &user_choice);
		scanf("%c", &trash);
		if(user_choice == 'R')
		{
			user_move = 1;
		}
		else if(user_choice == 'P')
		{
			user_move = 2;
		}
		else
		{
			user_move = 3;
		}
		if(user_move > computer_move && !(user_move==3 && computer_move==1))
		{
			printf("You win.");
			user_wins++;
		}
		else if(user_move == computer_move)
		{
			printf("It's a draw.");
			draws++;
		}
		else
		{
			printf("You lose.");
			computer_wins++;
		}
		printf("\nYou have won %d, the computer has won %d and there have been %d draws.\n\n\n",user_wins,computer_wins,draws);
	}
	return 0;
}
