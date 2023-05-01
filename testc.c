#include <stdio.h>

//#define PI 3.14159

int main ()
{
  double n1, n2, n3;
  printf("enter two numbers: ");
  scanf("%lf %lf",&n1,&n2);
  n3 = n1 + n2;
  printf("the sum of %lf and %lf is = %lf",n1,n2,n3);
  return 0;
}
