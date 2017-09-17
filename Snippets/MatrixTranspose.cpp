#include<iostream>
#include<stdio.h>

#define ROWS 10
#define COLUMNS 10

int main()
{
    int matrix[ROWS][COLUMNS], transpose_matrix[COLUMNS][ROWS], rows, columns, row_counter, column_counter;
    std::cout << "Enter the number of rows: ";
    std::cin >> rows;
    std::cout << "Enter the number of columns: ";
    std::cin >> columns;
    for(row_counter=0; row_counter<rows; row_counter++)
    {
        for(column_counter=0; column_counter<columns; column_counter++)
        {
            std::cin >> matrix[row_counter][column_counter];
        }
    }
    std::cout << "\nThe original matrix is:\n";
    for(row_counter=0; row_counter<rows; row_counter++)
    {
        for(column_counter=0; column_counter<columns; column_counter++)
        {
            std::cout << matrix[row_counter][column_counter] << "\t";
        }
        std::cout << "\n";
    }
    std::cout << "\n";
    for(row_counter=0; row_counter<rows; row_counter++)
    {
        for(column_counter=0; column_counter<columns; column_counter++)
        {
            transpose_matrix[column_counter][row_counter] = matrix[row_counter][column_counter];
        }
    }
    std::cout << "\nThe transpose of the matrix is:\n";
    for(row_counter=0; row_counter<columns; row_counter++)
    {
        for(column_counter=0; column_counter<rows; column_counter++)
        {
            std::cout << transpose_matrix[row_counter][column_counter] << "\t";
        }
        std::cout << "\n";
    }
    std::cout << "\n";
    return 0;
}
    

