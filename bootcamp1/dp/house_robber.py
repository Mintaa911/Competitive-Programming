class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = dict()
        
        def dp(idx,skip):
            nonlocal memo
            
            if (idx,skip) in memo:
                return memo[(idx,skip)]
            
            if idx == len(nums)-1:
                return nums[idx] if not skip else 0
            
            if skip:
                memo[(idx,skip)] = max(dp(idx+1, True), dp(idx+1, False))    
            else:
                memo[(idx,skip)] = dp(idx+1, True) + nums[idx]
                
            return memo[(idx,skip)]
                
        return max(dp(0,False), dp(0,True))
