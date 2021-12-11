def select(arr, i):
        # code here 
        minimum = arr[i]
        for j in range(i,len(arr)):
            if arr[j] < minimum:
                minimum = arr[j]
        return minimum
        
def selectionSort(arr,n):
    #code here
    for j in range(n):
        minimum = select(arr,j)
        idx = arr[j:].index(minimum)
        arr[j],arr[j+idx] = arr[j+idx],arr[j]

    return arr

