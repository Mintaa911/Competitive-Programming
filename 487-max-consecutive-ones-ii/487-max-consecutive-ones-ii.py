class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left,right = 0,0
        zero_idx,flip = None,1
        max_length = 0
        
        while right < len(nums):
            
            if nums[right] == 0 and flip == 1:
                flip = 0
                zero_idx = right
            elif nums[right] == 0 and flip == 0:
                max_length = max(max_length,right - left)
                left = zero_idx + 1
                zero_idx = right
                
            right += 1
            
        max_length = max(max_length,right - left)
        
        return max_length
                
            
                
        
        