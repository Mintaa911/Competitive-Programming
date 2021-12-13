def majority(nums):
    setNum = set(nums)
    return [s for s in setNum if nums.count(s) > len(nums)/3]

