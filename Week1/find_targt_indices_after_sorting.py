def find_target_indides(nums,target):
    count_nums = [0 for i in range(max(nums)+1)]
    for num in nums:
        count_nums[num] += 1
    nums = []
    for idx in range(len(count_nums)):
         for i in range(count_nums[idx]):
            nums.append(idx)
    return [i for i in range(len(nums)) if nums[i] == target]

