#!/usr/bin/env python3

# calculate binary to hexadecimal

def binary_to_hex(binary_str):
    decimal_num = int(binary_str, 2)
    hex_str = hex(decimal_num)[2:]     # remove the "0x" prefix from hex string
    return hex_str.upper()             # convert to uppercase for standard hexadecimal form

binary_number = input("Enter a binary number: ")     # user input

binary_number = binary_number.strip()                # remove any leading/trailing whitespaces and validate the input
if not all(bit in ('0', '1') for bit in binary_number):
    print("Invalid binary number. Please enter a string of 0s and 1s only.")
else:
    hexadecimal_number = binary_to_hex(binary_number)
    print("Binary:", binary_number)
    print("Hexadecimal:", hexadecimal_number)
