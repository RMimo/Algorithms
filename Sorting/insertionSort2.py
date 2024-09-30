# We will use the same approach of the insertionSort1 algorithm to sort an entire array.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    for i in range(1, n):
        idx = i
        for j in reversed(range(i)):
            if arr[i] < arr[j]:
                idx = j     
        cache = arr[idx:i]
        arr[idx] = arr[i]
        arr[idx+1:i+1] = cache
        print(*arr)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
