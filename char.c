

#include <stdio.h>

int main(void)
{
  char ch;
  printf("\nenter a single char  ");
  scanf("%c",&ch);
  printf("\nchar is %c ",ch);
  printf("\nchar in ascii is %d", ch);
  printf("\nthree consecutive chars are %c %c %c", ch, ch+1 ,ch+2);
  return 0;
}
