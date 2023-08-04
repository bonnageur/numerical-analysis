#!/usr/bin/env python3

# convert binary s = 0.000110011001100110011(the last digits 0011 loops) 
# to decimal fraction in the form of m/n. but use 32s-2s, which is 32-bit
# precision. weill use the concept of infinite geometric series.
# the repeating part is a binary representation of 1/15. we can express it
# as a fraction m/n. then combining it with the non-repeating part.
# p. 10 Ex 1.2 6

def binary_fraction_to_fraction(binary_str):
    # step 1: identify the repeating pattern
    repeating_part = binary_str[-4:]         # the repeating part is "0011"

    # step 2: convert repeating pattern to a fraction (m/n)
    m = int(repeating_part, 2)               # m = 3 (decimal representation of the repeating part)
    n = 2**len(repeating_part) - 1           # n = 2^4 - 1 = 15

    # step 3: convert the non-repeating part of decimal (0.00011)
    non_repeating_part = binary_str[:-len(repeating_part)]         # the non-repeating part is "00011"
    non_repeating_decimal = 0.0
    for i, bit in enumerate(non_repeating_part):
        if bit == '1':
            non_repeating_decimal += 2**(-i-1)

    # step 4: combine both parts to get the final fraction (m/n)
    numerator = int ((n * non_repeating_decimal) + m)
    denominator = n

    return numerator, denominator

binary_fraction = "0.000110011001100110011"
#binary_fraction = "0.000110011001100110011"
numerator, denominator = binary_fraction_to_fraction(binary_fraction)
print("Fraction (m/n):", f"{int(numerator)}/{int(denominator)}")
