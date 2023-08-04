#!/usr/bin/env python3

# input float decimal base 10
# convert it to hexadecimal
# convert it to binary-coded decimal code
# p.10 Ex 1.2 5

# function to convert decimal (base 10) to hexadecimal
def decimal_to_hexadecimal(decimal):
    # convert the integer part of the decimal to hexadecimal
    integer_part = int(decimal)
    hexadecimal_integer = hex(integer_part)[2:]        # remove the "0x" prefix from the hex string

    # convert the fractional part to hexadecimal
    fractional_part = decimal - integer_part
    fractional_hexadecimal = ""
    while fractional_part > 0:
        fractional_part *= 16
        fractional_digit = int(fractional_part)
        fractional_hexadecimal += hex(fractional_digit)[2:]
        fractional_part -= fractional_digit

    # combine the integer and fractional parts to get the full hexadecimal representation
    hexadecimal = f"{hexadecimal_integer}.{fractional_hexadecimal}"

    return hexadecimal.upper()

# function to convert hexadecimal to binary-coded decimal (BCD) with spaces
def hexadecimal_to_bcd_with_spaces(hex_str):
    bcd_code = ""
    for digit in hex_str:
        # convert each hexadecimal digit to its corresponding 4-bit bcd representation
        bcd_digit = bin(int(digit, 16))[2:].zfill(4)
        bcd_code += bcd_digit + " "                    # add a space between every 4 bits
    return bcd_code.strip()                            # remove any trailing space

# step 1: input base 10 decimal in float
decimal_number = float(input("Enter a decimal number: "))

# step 2: convert to hexadecimal
hexadecimal_number = decimal_to_hexadecimal(decimal_number)
print("Hexadecimal:", hexadecimal_number)

# step 3: convert hexadecimal to binary-coded decimal (BCD) code
bcd_code = hexadecimal_to_bcd_with_spaces(hexadecimal_number.replace('.', ''))
print("BCD code:", bcd_code)
