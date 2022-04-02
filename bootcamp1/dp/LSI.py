class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = dict()
        longest = 1
        def dp(idx):
            local_max = 1
            
            if idx in memo:
                return memo[idx]
            
            for i in range(idx,n):
                if nums[i] > nums[idx]:
                    local_max = max(local_max,1 + dp(i))
                
            memo[idx] = local_max
            
            return memo[idx]
        
        
        for j in range(n):
            longest = max(longest, dp(j))
            
            
        return longest
