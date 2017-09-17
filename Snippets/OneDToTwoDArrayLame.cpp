#include<iostream>
#include<stdio.h>

#define MAX 100

int main()
{
    int oneD_array[MAX], twoD_array[MAX][MAX], number_of_entries, counter, counter1, counter2;

    std::cout << "Enter the number of entries: ";
    std::cin >> number_of_entries;

    for(counter=0; counter<number_of_entries; counter++)
    {
        std::cin >> oneD_array[counter];
    }
    
    for(counter1=0; counter1<number_of_entries; counter1++)
    {
        for(counter2=0; counter2<number_of_entries; counter2++)
        {
            if(counter1 >= counter2)
            {
                twoD_array[counter1][counter2] = oneD_array[counter2];
            }
            else
            {
                twoD_array[counter1][counter2] = 0;
            }
        }
    }
    std::cout << "\nThe twoD array derived is:\n";
    for(counter1=0; counter1<number_of_entries; counter1++)
    {
        for(counter2=0; counter2<number_of_entries; counter2++)
        {
            std::cout << twoD_array[counter1][counter2] << "\t";
        }
        std::cout << "\n";
    }

    return 0;
}
