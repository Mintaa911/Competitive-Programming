def pancakeSort(arr):
    operations = []
    l,r = 0, len(arr)-1
    
    while l < r:
        if arr[r] == r+1:
            r -= 1
        elif arr[l] > arr[r]:
            sliced = arr[:l+1]
            
            for i in range(l+1):
                arr[l-i] = sliced[i]
                
            operations.append(l+1)
            sliced = arr[:r+1]
            for j in range(r+1):
                arr[r-j] = sliced[j]
                
            l = 0
            operations.append(r+1)
        else:

            l += 1                
            
    return operations