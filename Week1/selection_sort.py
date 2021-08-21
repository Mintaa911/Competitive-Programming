def selection_sort(arr):
    arr2 = []
    while len(arr) != 0:
        min_indx = 0
        min = arr[min_indx]
        for i in range(1,len(arr)):
            if arr[i] < min:
                min = arr[i]
                min_indx = i
        arr2.append(min)
        arr.pop(min_indx)
    return arr2