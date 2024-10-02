# Most sorting algorithms are comparison sorts, i.e. they sort a list just by comparing the elements to one another. A comparison sort algorithm cannot beat nlog(n) (worst-case) running time, since nlog(n) represents the minimum number of comparisons needed to know where to place each element.

# The counting sort algorithm does not require comparison. Instead, you create an integer array whose index range covers the entire range of values in your array to sort. Each time a value occurs in the original array, you increment the counter at that index. At the end, run through your counting array, printing the value of each non-zero valued index that number of times.

# Example: arr = [1,1,3,2,1]; counting_arr = [0,3,1,1] meaning 0 appearance of number 0, 3 appearances of number 1, and 1 appearance of numbers 2 and 3.

# For this exercise, always return a frequency array with 100 elements.

import math
import os
import random
import re
import sys

def countingSort(arr):
    count = [0] * 100
    for num in arr:
        count[num] += 1
    return counter
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
