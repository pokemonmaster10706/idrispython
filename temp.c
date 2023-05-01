

#include <stdio.h>

int main(void)
{
  double farenheit, celsius;

  printf("please enter a farenhiet as an integer:");
  scanf("%lf", &farenheit);
  celsius = (farenheit - 32)/1.8; //note the conversion on this line
  printf("\n %lf farenheit is %lf celsius.\n",farenheit, celsius);
  return 0;
}
