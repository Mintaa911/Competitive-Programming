class Solution:
    def myPow(self, x, n):
        if n%2 == 1:
            return self.helper(x,n-1) * x
        else:
            return self.helper(x,n)
            
    
    def helper(self,x,n):
        if n == 0:
            return 1


        if n > 0:
            if n%2 == 1:
                v = self.helper(x,(n//2))
                return v * v * x
            else:
                v = self.helper(x,n//2)
                return v * v
        else:
            return 1/self.helper(x,-n)