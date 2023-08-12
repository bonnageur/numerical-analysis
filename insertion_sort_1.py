#!/usr/bin/env python3.11

# Thomas H. Cormen, Charles E. Leiserson, Ronadl L. Rivest, Clifford Stein
# Introduction to Algorithm, Fourth Edition, 2022
# we weill call this book as just the Algorithm book from now on.
# Exercise 2-1
# insertion sort
# array = [31, 41, 59, 26, 41, 58]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# given arry
arr = [31, 41, 59, 26, 41, 58]

# calling insertion_sort function
insertion_sort(arr)

# display the sorted arry
print("Sorted array: ", arr)
