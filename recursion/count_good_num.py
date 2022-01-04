class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def helper(a,n):
            if n == 1:
                return a
            elif n == 0:
                return 1
            elif n %2 == 0:
                x =helper(a,n//2)
                return x * x % mod
            else:
                x = helper(a,(n-1)//2)
                return x*x*a % mod
            
        mod = 10**9 + 7
        if n % 2 == 0:
            result = helper(20,n//2)
            return result % mod
        else:
            result = helper(5,n//2+1) * helper(4,n//2)
            return result % mod
        