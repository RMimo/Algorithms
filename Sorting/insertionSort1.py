# One common task for computers is to sort data. 
# For example, people might want to see all their files on a computer sorted by size. 
# Since sorting is a simple problem with many different possible solutions, 
# it is often used to introduce the study of algorithms.

# Insertion Sort is a simple and intuitive sorting algorithm. 
# We will first start with a nearly sorted list.

# Insert element into sorted list: 
# Given a sorted list with an unsorted number e in the rightmost cell, 
# how can we write some simple code to insert e into the array so that it remains sorted?

# For example: arr = [1,2,4,5,3]. We can use brute-force to sort it.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    rightmost = arr[-1]
    for i in reversed(range(1, n)):  # Start from 1 instead of 0
        if arr[i-1] >= rightmost:
            arr[i] = arr[i-1]
            print(*arr)
        else:
            arr[i] = rightmost
            print(*arr)
            break
    else:
        # If the loop didn't break, place the rightmost at the beginning
        arr[0] = rightmost
        print(*arr)
        
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
