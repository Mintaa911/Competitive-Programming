class Solution:
    def rob(self, nums: List[int]) -> int:
        old_max_sum, new_max_sum = 0,0
        
        for num in nums:   
            cur_sum = old_max_sum + num
            old_max_sum = max(old_max_sum, new_max_sum)
            new_max_sum = max(old_max_sum, cur_sum)
            
        return max(old_max_sum,new_max_sum)
        