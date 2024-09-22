import math
import os
import random
import re
import sys

# To solve this problem, the goal is to sort an array of numeric strings based on their integer values. 
# The main challenge lies in the fact that these numbers can be extremely large, potentially up to 10^6 digits, 
# so we can't convert them to regular integers and compare them directly using typical numeric comparison 
# due to limitations in both space and time efficiency.

# The solution requires sorting the strings as if they were integers by:
# - Length Comparison: A longer string represents a larger number, so numbers with fewer digits are smaller.
# - Lexicographical Comparison for Same Length: If two numbers have the same length, we can compare them lexicographically as strings, which will yield the correct result since their digit values directly correspond to their numeric values.


def bigSorting(unsorted):
    # not efficient:
    # return list(map(str, sorted(map(int, unsorted)))) 
  
    # len(x) ensures that shorter strings (representing smaller numbers) come first.
    # x ensures that if two strings have the same length, they are sorted lexicographically (i.e., digit by digit).
    return sorted(unsorted, key=lambda x: (len(x), x))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
