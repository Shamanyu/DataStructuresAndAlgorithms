#include <stdio.h>

void main() 
{
  int i = 0;
  __int128 s = ((__int128)0x24A122 << 63) + 0x11b487f4d1e50a92;
  for (i=0; i<85; i+=5) printf("%c", 'A' + ((s >> i) & 0x1f));
  printf("\n");
} 
