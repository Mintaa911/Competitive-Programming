class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        
        def counter(mid):
            count = 0
            
            for i in range(1,m+1):
                count += min(n,mid//i)
                
            return count
        
        left,right = 1,n*m
        
        while left < right:
            mid = (left + right)//2
            
            if counter(mid) < k:
                left = mid + 1
            else:
                right = mid
                
                
        return left
