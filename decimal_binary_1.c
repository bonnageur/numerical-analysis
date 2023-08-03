// convert decimal to binary in C programming language
// input in any form: int, float, or fraction in a/b form

#include <stdio.h>
#include <stdlib.h>

// Function to convert decimal fraction to binary
void decimal_fraction_to_binary(double decimal_fraction, int precision) {
    printf(".");
    while (precision > 0 && decimal_fraction > 0) {
        decimal_fraction *= 2;
        int bit = (int)decimal_fraction;
        printf("%d", bit);
        decimal_fraction -= bit;
        precision--;
    }
}

// Function to convert fraction to decimal fraction
double fraction_to_decimal(int numerator, int denominator) {
    return (double)numerator / denominator;
}

// Function to convert decimal number to binary
void decimal_to_binary(double num, int precision) {
    int int_part = (int)num;
    double fractional_part = num - int_part;

    // Convert integer part to binary
    int binary_int[32];
    int int_index = 0;
    while (int_part > 0) {
        binary_int[int_index++] = int_part % 2;
        int_part /= 2;
    }

    // Print binary representation of integer part in reverse order
    if (int_index == 0)
        printf("0"); // If integer part is 0, print '0'
    for (int i = int_index - 1; i >= 0; i--) {
        printf("%d", binary_int[i]);
    }

    // Convert fractional part to binary
    if (fractional_part > 0) {
        decimal_fraction_to_binary(fractional_part, precision);
    }
}

// Function to check if the input is a fraction
int is_fraction(const char* input) {
    int numerator, denominator;
    return sscanf(input, "%d/%d", &numerator, &denominator) == 2;
}

int main() {
    char input[100];
    double decimal_num;
    int precision = 20; // Specify the number of fractional digits to display

    printf("Enter a decimal number or a fraction in the form of 'a/b': ");
    scanf("%s", input);

    if (is_fraction(input)) {
        int numerator, denominator;
        sscanf(input, "%d/%d", &numerator, &denominator);
        decimal_num = fraction_to_decimal(numerator, denominator);
    } else {
        decimal_num = atof(input); // Convert input to a floating-point number
    }

    decimal_to_binary(decimal_num, precision);

    printf("\n");
    return 0;
}
