def not_equal(nums):
    nums.sort()
    for i in range(0,len(nums)-2,2):
        nums[i+1],nums[i+2] = nums[i+2],nums[i+1]
    return nums
