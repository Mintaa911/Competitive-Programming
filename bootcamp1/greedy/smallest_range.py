class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        min_range = max(nums) - min(nums)
        
        for i in range(n-1):
            _max = max(nums[i]+k, nums[-1]-k)
            _min = min(nums[0]+k, nums[i+1]-k)
            
            min_range = min((_max - _min),min_range)
            
        return min_range
            
            
            
            
            
            
