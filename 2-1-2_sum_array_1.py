#!/usr/bin/env python3.11

# the Algorithm book Exercise 2.1-2
# SUM-ARRAY
# array: [1, 100]

# initialization: initialize a variable to hold the sum and an array to store numbers from 1 to 100
sum_total = 0
num_array = list(range(1, 101))

# maintenence: loop through each number in the array and add it to the sum
for num in num_array:
    sum_total += num

# termination: print the final sum
print("The sum of numbers from 1 to 100 is: ", sum_total)
