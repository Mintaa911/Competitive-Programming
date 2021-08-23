#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumToys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER k
#

def maximumToys(prices, k):
    # Write your code here
    truncatedSortedArr = modified_selection_sort(prices,k)
    maxToy = 0
    totalPrice = 0
    
    for i in truncatedSortedArr:
        totalPrice += i
        if totalPrice > k:
            return maxToy
        maxToy += 1

    return maxToy

def modified_selection_sort(arr,k):
    arr2 = []
    balance = 0
    while len(arr) != 0:
        min_indx = 0
        min = arr[min_indx]
        for i in range(1,len(arr)):
            if arr[i] < min:
                min = arr[i]
                min_indx = i
        balance += min
        if balance > k:
            return arr2
        
        arr2.append(min)
        arr.pop(min_indx)
    return arr2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
