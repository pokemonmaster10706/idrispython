#include<stdio.h>
#include<math.h>

int main(void){
  double x , sine;
  printf("enter a float number between 1 and 0: \n");
  scanf("%lf", &x);
  sine=sin(x);
  printf("the sine of %lf is %lf\n",x,sine);
  return 0;
}
