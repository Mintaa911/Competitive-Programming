#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    # Write your code here
    sortedArr = countingSort(arr)
    median = sortedArr[(len(sortedArr)//2)]
    return median

  
def countingSort(arr):
    countingArr = [0 for i in range(max(arr)+1)]
    for i in arr:
        countingArr[i] += 1
    for j in range(len(countingArr)):
        for x in range(countingArr[j]):
            arr.append(j)
            arr.pop(0)
    return arr 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
