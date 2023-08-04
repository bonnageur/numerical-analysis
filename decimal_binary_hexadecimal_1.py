#!/usr/bin/env python3 

# p.9 Ex. 1.3
# convert decimal to binary and hexadecimal

def decimal_to_binary(decimal_num):
    return bin(decimal_num)        

def decimal_to_hexadecimal(decimal_num):
    return hex(decimal_num)        

if __name__ == "__main__":
    try:
        decimal_num = int(input("Enter a decimal number: "))
        binary_num = decimal_to_binary(decimal_num)
        hexadecimal_num = decimal_to_hexadecimal(decimal_num)

        print(f"Binary representation: {binary_num}")
        print(f"Hexadecimal representation: {hexadecimal_num}")

    except ValueError:
        print("Invalid input. Please enter a valid decimal number.")
