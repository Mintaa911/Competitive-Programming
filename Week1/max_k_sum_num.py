from collections import Counter
def maxOperations(nums,k):
    nums.sort()
    kSum = 0
    dictNum = Counter(nums)
    
    for ky in dictNum:

        while k-ky in dictNum and dictNum[ky] > 0 and dictNum[k-ky] > 0:
            if ky == k-ky and dictNum[ky] == 1:
                break
            dictNum[ky] -= 1
            dictNum[k-ky] -= 1
            kSum += 1
    return kSum