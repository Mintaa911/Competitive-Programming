def merge_sort(arr):
    if len(arr) == 1:
        return arr
    n = len(arr)
    arr1 = merge_sort(arr[0:n//2])
    arr2 = merge_sort(arr[n//2:n])
    return merge(arr1,arr2)

def merge(arr1,arr2):
    temp = []
    while arr1 and arr2 :
        if arr1[0] > arr2[0]:
            temp.append(arr2[0])
            arr2.pop(0)
        else:
            temp.append(arr1[0])
            arr1.pop(0)

    while arr1:
        temp.append(arr1[0])
        arr1.pop(0) 
    while arr2:
        temp.append(arr2[0])
        arr2.pop(0) 
    return temp

arr = merge_sort([3,-2,-1,0,2,4,1])
[print(s) for s in arr]

