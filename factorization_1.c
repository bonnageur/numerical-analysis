// factorizing an interger
// gcc-13

#include <stdio.h>

int main() {
    int number, i;

    // prompt the user for the input number
    printf("Enter a positive integer: ");
    scanf("%d", &number);

    // check if the number is positive
    if (number <= 0) {
        printf("Error: Please enter a positive integer.\n");
        return 1;
    }

    // factorize the number
    printf("Prime factors of %d are:\n", number);
    i = 2;
    while (i * i <= number) {
        if (number % i == 0) {
            printf("%d\n", i);
            number /= i;
        }
        else {
            i++;
        }
    }

    if (number > 1) {
        printf("%d\n", number);     // remaining prime factor (if any)
    }

    return 0;
}
