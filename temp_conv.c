// The must read the second example, after "Hello, Wornd!\n" of the C book.
// this code will be used as subroutin of main code in python.

#include <stdio.h>

/* print Fahrenheit-Celsius table for fahr = 0, 20,..., 300;
   floating-point version */

int main(void) {
  float fahr, celsius;
  int lower, upper, step;

  lower = 0;
  upper = 300;
  step = 20;

  fahr = lower;
  while (fahr <= upper) {
    celsius = (5.0 / 9.0) * (fahr - 32.0);
    printf("%3.0f %6.2f\n", fahr, celsius);
    fahr = fahr + step;
  }
}
