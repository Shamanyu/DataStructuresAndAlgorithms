#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main()
{
        unsigned long long int test_cases, L, R, count, counter, counter1, square_root_floor;
        double square_root;
        scanf("%llu", &test_cases);
        for(counter=0;counter<test_cases;counter++)
        {
                scanf("%llu", &L);
                scanf("%llu", &R);
                count=0;
                for(counter1=L;counter1<=R;counter1++)
                {
                        square_root=sqrt(counter1);
                        square_root_floor=square_root;
                        if(square_root==square_root_floor)
                        {
                                count++;
                        }
                }
                printf("%llu\n", count);
        }
        return 0;
}

