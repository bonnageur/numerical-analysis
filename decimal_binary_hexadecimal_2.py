#!/usr/bin/env python3 

# bin() and hex() functions in python only take integer
# modify to able to input float

def decimal_to_binary(decimal_num):
    return bin(int(decimal_num))         # in python bin() requires integer input. convert float to int

def decimal_to_hexadecimal(decimal_num):
    return hex(int(decimal_num))         # in python hex() requires integer input. convert float to int

if __name__ == "__main__":
    try:
        decimal_num = float(input("Enter a decimal number: "))
        binary_num = decimal_to_binary(decimal_num)
        hexadecimal_num = decimal_to_hexadecimal(decimal_num)

        print(f"Binary representation: {binary_num}")
        print(f"Hexadecimal representation: {hexadecimal_num}")

    except ValueError:
        print("Invalid input. Please enter a valid decimal number.")
