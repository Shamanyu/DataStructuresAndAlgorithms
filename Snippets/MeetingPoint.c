#include<stdio.h>
#include<stdlib.h>

#define MAX 100

typedef struct {
  int x;
  int y;
} POSITION;

int distances[MAX] = {0};

int get_shortest_path_length(POSITION p1, POSITION p2) {
  int x_difference = p1.x>=p2.x?p1.x-p2.x:p2.x-p1.x;
  int y_difference = p1.y>=p2.y?p1.y-p2.y:p2.y-p1.y;
  return x_difference>y_difference?x_difference:y_difference;
}

int main() {
  int number_of_houses, counter, counter1, counter2, minimum_distance;
  POSITION house[MAX];
  int meeting_point;
  printf("Enter number of houses: ");
  scanf("%d", &number_of_houses);
  for (counter=0; counter<number_of_houses; counter++) {
    printf("\nEnter x coordinate of %d house: ", counter+1);
    scanf("%d", &house[counter].x);
    printf("\nEnter y coordinate of %d house: ", counter+1);
    scanf("%d", &house[counter].y);
  }
  for(counter1=0; counter1<number_of_houses; counter1++) {
    for(counter2=0; counter2<number_of_houses; counter2++) {
      distances[counter1] += get_shortest_path_length(
        house[counter1], house[counter2]); 
    }
  }
  minimum_distance = -1;
  for(counter=0; counter<number_of_houses; counter++) {
    if(minimum_distance == -1 || distances[counter] < minimum_distance) {
      meeting_point = counter+1;
      minimum_distance = distances[counter];
    }
  }
  printf("\nHouse number %d situated at {%d, %d} should be chosen as the meeting point\n", meeting_point, house[meeting_point-1].x, house[meeting_point-1].y);
  return 0;
}