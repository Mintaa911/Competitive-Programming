
n = 10
arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
unsortedNum = arr[n-1]
currentIdx = n-1
for i in range(n-2,-1,-1):
    if unsortedNum < arr[i]:
        arr[currentIdx] = arr[i]
        currentIdx = i
        print(" ".join(str(num) for num in arr))
    else:
   
        arr[i+1] = unsortedNum
        print(" ".join(str(num) for num in arr))
        break
if currentIdx == 0:
    arr[0] = unsortedNum 
    print(" ".join(str(num) for num in arr))
    