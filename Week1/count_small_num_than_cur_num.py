def count_smaller(nums):
    count_nums = [0 for i in range(max(nums)+1)]
    arr = [0 for i in range(len(nums))]
    
    for num in nums:
        count_nums[num] += 1
        
    for i in range(len(nums)):
        for j in range(len(count_nums)):
            if j < nums[i]:
                arr[i] += count_nums[j] 
            else:
                break
    return arr