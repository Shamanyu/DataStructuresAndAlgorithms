#include<stdio.h>


int main()
{
	int number_of_temples,multiply_rate,donation_amount,initial_amount,final_amount;
	int X_term,constant_term;
	int counter,temp;
	scanf("%d", &number_of_temples);
	scanf("%d", &multiply_rate);
	scanf("%d", &donation_amount);
	scanf("%d", &final_amount);
	X_term=1;
	constant_term=0;
	for(counter=0;counter<number_of_temples;counter++)
	{
		X_term = X_term*multiply_rate;
		constant_term=constant_term*multiply_rate;
		constant_term=constant_term-donation_amount;
	}
	temp=final_amount-constant_term;
	initial_amount=temp/X_term;
	printf("%d",initial_amount);
	return 0;
}
