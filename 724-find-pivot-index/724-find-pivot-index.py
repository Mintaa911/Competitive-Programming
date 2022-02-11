class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum,prefix_sum = sum(nums),0
        
            
        for i in range(len(nums)):
            if (total_sum - (prefix_sum + nums[i])) == prefix_sum:
                return i
            prefix_sum += nums[i]
            
        return -1
        
            