#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # padding for even pages
    if n%2 == 0:
        n = n + 1
    if p%2 == 0:
        p = p + 1
        
    turns_right = int(p/2)
    turns_left = int((n-p)/2)
    return min(turns_right, turns_left)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
