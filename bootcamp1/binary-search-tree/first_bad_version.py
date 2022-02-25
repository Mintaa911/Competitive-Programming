# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left,right = 1,n
        fistBad = None
        
        while left <= right:
            middle = (left + right)//2
        
            if isBadVersion(middle):
                right = middle -1
                firstBad = middle
            else:
                left = middle + 1
                
        return firstBad
