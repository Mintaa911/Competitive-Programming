class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def dp(idx,buy):
            if (idx,buy) in memo:
                return memo[(idx,buy)]
            if idx >= len(prices):
                return 0
            else:
                if buy:
                    memo[(idx,buy)] = max(dp(idx+1,False) - prices[idx], dp(idx+1,True))
                else:
                    memo[(idx,buy)] = max(dp(idx+2,True) + prices[idx], dp(idx+1, False))
            
            return memo[(idx,buy)]
            
            
        memo = dict()
        return dp(0,True)
        
