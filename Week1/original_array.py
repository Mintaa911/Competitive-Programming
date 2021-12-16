from collections import Counter
def originalOfDouble(changed):
    original = []
    changed.sort()

    dictNum = Counter(changed)
    for k in dictNum:
        
        while k*2 in dictNum and dictNum[k] > 0:
            if dictNum[k*2] > 0:
                dictNum[k] -= 1
                dictNum[k*2] -= 1
                original.append(k)
            else:
                break
                
    for k in dictNum:
        if dictNum[k] != 0:
            return []

    return list(original)
   

 
    