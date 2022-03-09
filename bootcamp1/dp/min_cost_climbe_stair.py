class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def rec(idx,c):
            
            if idx in memo:
                return memo[idx]
            
            if idx == len(cost)-1:
                memo[idx] = c
            elif idx == len(cost)-2:
                memo[idx] = c
            else:
                memo[idx] = min(rec(idx+1,cost[idx+1]),rec(idx+2,cost[idx+2])) + c
            
            return memo[idx]
        
        memo = dict()
        
        return min(rec(0,cost[0]),rec(1,cost[1]))
            
            
