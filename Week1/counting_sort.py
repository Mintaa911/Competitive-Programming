  
def countingSort(arr):
    countingArr = [0 for i in range(max(arr)+1)]
    for i in arr:
        countingArr[i] += 1
    for j in range(len(countingArr)):
        for x in range(countingArr[j]):
            arr.append(j)
            arr.pop(0)
    return arr 
