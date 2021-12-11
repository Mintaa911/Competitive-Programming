import math

def k_closest_point(points, k):
    sorted = merge_sort(points)
    return sorted[:k]


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
        d1 = math.sqrt(left[0][0]**2 + left[0][1]**2)
        d2 = math.sqrt(right[0][0]**2 + right[0][1]**2)
        if d1 < d2:
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


