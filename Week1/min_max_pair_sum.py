def minPairSum(nums):
    nums.sort()
    l = 0
    r = len(nums)-1
    pairSum = []
    
    for i in range(len(nums)//2):
        pairSum.append(nums[l]+nums[r])
        l += 1
        r -= 1
    return max(pairSum)