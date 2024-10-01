# We will cover a divide-and-conquer algorithm called Quicksort (also known as Partition Sort). This challenge is a modified version of the algorithm that only addresses partitioning. It is implemented as follows:

# Step 1: Divide
# Choose some pivot element, p, and partition your unsorted array, arr, into three smaller arrays: left, right, and equal, where each element in left < p, each element in right > p, and each element in equal = p.
# arr[0] is always the pivot element

import math
import os
import random
import re
import sys

def quickSort(arr):
    pivot = arr[0]
    left = [i for i in arr if i < pivot]
    right = [i for i in arr if i > pivot]
    equal = [i for i in arr if i == pivot]
    return left + equal + right

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
