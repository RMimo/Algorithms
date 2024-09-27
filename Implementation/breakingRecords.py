#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    broke_best = 0
    broke_worst = 0
    max_score = -1
    min_score = 10**8 + 1
    for score in scores:
        if score > max_score:
            max_score = score
            broke_best += 1
        if score < min_score:
            min_score = score
            broke_worst += 1
            
    return broke_best - 1, broke_worst - 1
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
