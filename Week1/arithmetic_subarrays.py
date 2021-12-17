def checkArithmeticSubarrays(nums,l,r):
    arithmetic = []
    for i in range(len(l)):
        sliced = nums[l[i]:r[i]+1]
        sliced.sort()
        d = sliced[1]-sliced[0]
        for j in range(1,len(sliced)-1):
            
            if sliced[j+1] - sliced[j] != d:
                d = sliced[j+1] - sliced[j]
                break
        if d == sliced[1]-sliced[0]:
            arithmetic.append(True)
        else:
            arithmetic.append(False)
            
    return arithmetic