#include<stdio.h>
#include<stdlib.h>

#define M 100
#define N 100

typedef enum {top, left} bool;

int matrix[M][N];
bool direction[M][N];

int* find_best_path(int row, int column) {
  int* best_path;
  int top_row = row - 1;
  int left_column = column - 1;
  if (top_row < 0 && left_column < 0) {
    return matrix[row][column];
  } else if (top_row >= 0) {
    return sort(find_best_path(top_row, column) + matrix[row][column]);
  } else if (left_column >= 0) {
    return sort(find_best_path(row, left_column) + matrix[row][column]);
  } else {
    return find_lexicographically_shorter_path(
      sort(find_best_path(top_row, column) + matrix[row][column]),
      sort(find_best_path(row, left_column) + matrix[row][column]));k
  }
}

int main() {
  int best_path[M+N];
  get_input();
  best_path = find_best_path(M-1, N-1);
  print_best+path(best_path);
}