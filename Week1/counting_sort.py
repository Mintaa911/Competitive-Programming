  
def countingSort(arr):
    countingArr = [0 for i in range(max(arr)+1)]
    for i in arr:
        countingArr[i] += 1
    countingArr
