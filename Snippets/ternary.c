#include<stdio.h>
#include<stdlib.h>

int main()  {
    float c;
    float commision;
    scanf("%f", &c);
    commision = c<5000?0:c<12000?3.0/100*c:c<22000?5.0/100*c:c<30000?10.0/100*c:15.0/100*c;
    printf("%f", commision);
    return 0;
}
