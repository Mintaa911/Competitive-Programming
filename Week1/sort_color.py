def sortColors(nums):
    for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] > nums[i]:
                    nums[i],nums[j] = nums