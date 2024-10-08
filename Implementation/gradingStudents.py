#!/bin/python3

import math
import os
import random
import re
import sys#

def gradingStudents(grades):
    rounded_grades = []
    for grade in grades:
        mults = grade//5
        if grade < 38:
            pass
        elif (mults+1)*5 - grade < 3:
            grade = (mults+1)*5
        rounded_grades.append(grade)
    return rounded_grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
