/* convert decimal to hexadecimal
   input: int, float, fracntion(m/n) 
   tested in gcc versin 13
   $ gcc-13 -o dex_hex_1_c dex_hex_1.c
   */

#include <stdio.h>
#include <stdlib.h>

// function to convert a decimal value to hexadecimal
void decimal_to_hexadecimal(double decimal) {
    printf("Decimal: %lf\n", decimal);

    // separate integer and fractional parts
    int int_part = (int)decimal;
    double fractional_part = decimal - int_part;

    // convert and display the integer part in hexadecimal
    if (int_part > 0) {
        printf("Hexadecimal (Integer Part): %X\n", int_part);
    }

    // convert and display the integer part in hexadecimal
    if (fractional_part > 0) {
        printf("Hexadecimal (Fractional Part): 0.");

        while (fractional_part > 0 && fractional_part < 1) {
            fractional_part *= 16;
            int hex_digit = (int)fractional_part;
            printf("%X", hex_digit);
            fractional_part -= hex_digit;
        }

        printf("\n");
    }
}

int main() {
    char input_type;
    double decimal_value;

    // prompt the user for the input type: int, float, or fraction(m/n)
    printf("Enter the input type ('i' for integer, 'f' for float, 'r' for fraction m/n): ");
    scanf(" %c", &input_type);

    switch (input_type) {
        case 'i': {
            int integer_value;
            printf("Enter an integer: ");
            scanf("%d", &integer_value);
            decimal_value = (double)integer_value;
            break;
        }
        case 'f': {
            printf("Enter a float: ");
            scanf("%lf", &decimal_value);
            break;
        }
        case 'r': {
            int numerator, denominator;
            printf("Enter the fraction: ");
            scanf("%d/%d", &numerator, &denominator);

            decimal_value = (double)numerator / denominator;
            break;
        }
        default: {
            printf("Invalid input type. Please enter 'i', 'f', or 'r'.\n");
            return 1;
        }
    }
    // convert and display the decimal value in hexadecimal
    decimal_to_hexadecimal(decimal_value);

    return 0;
}
