def largest_number(nums):
    
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            j1 = (str(nums[j]) * 9)[:9]
            j2 = (str(nums[j+1])*9)[:9]
            if j2 > j1:
                nums[j],nums[j+1] = nums[j+1],nums[j]
            elif j2 == j1 and nums[j+1] > nums[j]:
                nums[j],nums[j+1] = nums[j+1],nums[j]            
    for num in nums:
        if num != 0:
            return "".join([str(num) for num in nums])
    return "0"                   
