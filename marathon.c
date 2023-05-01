/* the distance of a marathon from miles and yeards
 to kilometers*/

#include <stdio.h>

int main(void)
{
  int miles, yards, kilometers;
  printf("please enter the miles and yards : ");
  scanf("%d %d",&miles,&yards);
  kilometers = 1.609 * (miles + yards / 1760.0);
  printf ("\nA marathon is %d kilometers.\n\n", kilometers);
  return 0;
}
