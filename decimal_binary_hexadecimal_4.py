#!/usr/bin/env python3

# convert decimal to binary and hexadecimal: float input and float output available 
# since bin(), hex() functions in python doesn't take float, write customized functions 
# to convert decimal to bin and hex.
# now input fraction is available.

def float_to_binary(decimal_num, num_digits=64):
    binary_representation = bin(int(decimal_num))[2:]
    fractional_part = decimal_num - int(decimal_num)
    binary_fractional_part = ""

    while fractional_part != 0 and len(binary_fractional_part) < num_digits:
        fractional_part *= 2
        bit = int(fractional_part)
        binary_fractional_part += str(bit)
        fractional_part -= bit

    return f"{binary_representation}.{binary_fractional_part}"

def float_to_hexadecimal(decimal_num, num_digits=16):
    hexadecimal_representation = hex(int(decimal_num))[2:]
    fractional_part = decimal_num - int(decimal_num)
    hexadecimal_fractional_part = ""

    while fractional_part != 0 and len(hexadecimal_fractional_part) < num_digits:
        fractional_part *= 16
        digit = int(fractional_part)
        hexadecimal_fractional_part += hex(digit)[2:]
        fractional_part -= digit

    return f"{hexadecimal_representation}.{hexadecimal_fractional_part}"

if __name__ == "__main__":
    try:
        decimal_num = eval(input("Enter a decimal number (e.g., 7/16): "))
        binary_num = float_to_binary(decimal_num)
        hexadecimal_num = float_to_hexadecimal(decimal_num)

        print(f"Binary representation: {binary_num}")
        print(f"Hexadecimal representation: {hexadecimal_num}")

    except (ValueError, ZeroDivisionError, SyntaxError):
        print("Invalid input. Please enter a valid decimal number.")
