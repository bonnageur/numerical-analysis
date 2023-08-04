#!/usr/bin/env python3

# decimal fraction 1/10 is 0.0001100 in binary
# calculate error

def decimal_to_binary(decimal, num_bits):
    binary_rep = []
    for _ in range(num_bits):
        decimal *= 2
        if decimal >= 1:
            binary_rep.append(1)
            decimal -= 1
        else:
            binary_rep.append(0)
    return binary_rep

decimal_number = 1 / 10
num_bits = 20             # higher precision (can increase this value for more precision)

binary_representation = decimal_to_binary(decimal_number, num_bits)
binary_str = "0." + "".join(str(bit) for bit in binary_representation)

expected_binary_str = "0.00011001100110011001100110011001100110011001100110011"

print("Expected binary representation:", expected_binary_str)
print("Actual binary representation :", binary_str)

# calculate and display the error
error = abs(float(binary_str) - decimal_number)
print("Error:", error)
