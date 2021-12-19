class Solution:
    def minSetSize(arr):
        dictNum = dict([])
        for a in arr:
            if a in dictNum:
                dictNum[a] += 1
            else:
                dictNum[a] = 1
        dictNum = dict(sorted(dictNum.items(), key=lambda x:x[1],reverse=True))
        
        n = len(arr)
        setSize = 0
        for k in dictNum:
            if n <= len(arr)//2:
                break
            for i in range(dictNum[k]):
                n -= 1
            setSize +=1
        return setSize