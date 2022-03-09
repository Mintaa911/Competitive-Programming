class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        def dp(idx):
            if idx == len(prices)-1:
                memo[idx] = prices[idx]
            else:
                memo[idx] = max(dp(idx+1), prices[idx])
            return memo[idx]
        
        profit = 0
        memo = dict()
        for i in range(len(prices)):
            if i in memo:
                p = memo[i] - prices[i]
                profit = max(profit,p)
            else:
                p = dp(i) - prices[i]
                profit = max(profit,p)
            
            
        return profit
