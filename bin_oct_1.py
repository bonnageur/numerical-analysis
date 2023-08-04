#!/usr/bin/env python3

# convert binary to octal

def binary_to_octal(binary_str):
    # pad the binary string with leading zeros to make its length a multiple of 3
    padding_length = (3 - len(binary_str) % 3) % 3
    padded_binary_str = '0' * padding_length + binary_str

    # split the padded binary string into groups of 3 digits each
    binary_groups = [padded_binary_str[i:i+3] for i in range(0, len(padded_binary_str), 3)]

    # convert each binary group to its corresponding octal digit
    octal_digits = [int(group, 2) for group in binary_groups]

    # join the octal digits to form the final octal representation
    octal_str = ''.join(str(digit) for digit in octal_digits)

    return octal_str

# user input
binary_number = input("Enter a binary number: ")

# remove any leading/trailing whitespaces and validate the input
binary_number = binary_number.strip()
if not all(bit in('0', '1') for bit in binary_number):
    print("Invalid binary number. Please enter a string of 0s and 1s only.")
else:
    octal_number = binary_to_octal(binary_number)
    print("Binary:", binary_number)
    print("Octal:", octal_number)
