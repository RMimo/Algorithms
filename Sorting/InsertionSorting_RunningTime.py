# The running time of an algorithm for a specific input depends on the number of operations executed. The greater the number of operations, the longer the running time of an algorithm. We usually want to know how many operations an algorithm will execute in proportion to the size of its input, which we will call N.

# What is the ratio of the running time of Insertion Sort to the size of the input?
# For each element V in an array of N numbers, Insertion Sort compares the number to those to its left until it reaches a lower value element or the start. At that point it shifts everything to the right up one and inserts V into the array.

# How long does all that shifting take?
# In the best case, where the array was already sorted, no element will need to be moved, so the algorithm will just run through the array once and return the sorted array. The running time would be directly proportional to the size of the input, so we can say it will take N time. However, we usually focus on the worst-case running time (computer scientists are pretty pessimistic). The worst case for Insertion Sort occurs when the array is in reverse order. To insert each number, the algorithm will have to shift over that number to the beginning of the array. Sorting the entire array of N numbers will therefore take 1+2+...+(N-1) operations, which is N(N-1)/2 (almost N^2/2). 

# Computer scientists just round that up (pick the dominant term) to N^2 and say that Insertion Sort is an "N^2 time" algorithm.

import math
import os
import random
import re
import sys

def runningTime(arr):
    counter = 0
    for i in range(1, len(arr)):
        for j in reversed(range(i)):
            if arr[i] < arr[j]:
                counter += 1
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()




