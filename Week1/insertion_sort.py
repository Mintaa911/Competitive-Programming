def insertion_sort(arr):
    for x in range(1,len(arr)):
        cur = arr[x]
        y = x
        while y > 0 and arr[y-1] > cur:
            arr[y] = arr[y-1] 
            y -= 1
        arr[y] = cur
    return arr
    
