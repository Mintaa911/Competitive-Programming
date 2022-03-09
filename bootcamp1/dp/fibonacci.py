class Solution:
    def fib(self, n: int) -> int:
        
        
        def dp(n):
            if n == 0:
                memo[n] = 0
            elif n == 1:
                memo[n] = 1
                
            else:
                memo[n] = dp(n-1) + dp(n-2)
                
            return memo[n] 
        
        
        memo = dict()
        
        return dp(n)
