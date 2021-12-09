def quick_sort(arr,l,h):
    if l >= h:
        return 
    p = partition(arr,l,h)
    quick_sort(arr,l,p-1)
    quick_sort(arr,p+1,h)
    return arr

def partition(arr,l,h):
    pivot = arr[h]
    j = l -1
    for i in range(l,h):
        if arr[i] < pivot:
            j += 1
            arr[i],arr[j] = arr[j],arr[i]       
    arr[h],arr[j+1] = arr[j+1],arr[h]
    return j + 1

arr = [3,-2,-1,0,2,4,1]

[print(x) for x in quick_sort(arr,0,6)]