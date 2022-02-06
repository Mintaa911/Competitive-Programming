class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum,prefix_sum,ptr = 0,0,0
        for num in nums:
            total_sum += num
            
        while ptr < len(nums):   
            if (total_sum - (prefix_sum + nums[ptr])) == prefix_sum:
                return ptr
            
            prefix_sum += nums[ptr]
            ptr += 1
            
        return -1
        
            