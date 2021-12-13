import math
def merge_interval(intervals):
    merged = merge_sort(intervals)
    i = 0
    while i < len(merged)-1:
        if merged[i][1] >= merged[i+1][0]:
            m = [merged[i][0],max(merged[i][1],merged[i+1][1])]
            merged.pop(i)
            merged.pop(i)
            merged.insert(i,m)
            i = 0
        else: 
            i += 1
    return merged

def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr)//2

    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    sorted = []
    while left and right:
        d1 = left[0][0]
        d2 = right[0][0]
        if d1 < d2 :
            sorted.append(left[0])
            left.pop(0)
        else:
            sorted.append(right[0])
            right.pop(0)
    if left:
        for num in left:
            sorted.append(num)
    else:
        for num in right:
            sorted.append(num)

    return sorted

