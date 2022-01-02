class Solution:
    def PredictTheWinner(self,nums):
        p1,p2 = self.divideConquer(nums,0,len(nums)-1,1)
        
        return p1 >= p2
        
    def divideConquer(self,nums,s,e,p):
        p1,p2 = 0,0
        if(s == e):
            if p == 1:
                return nums[s],0
            else:
                return 0,nums[s]
        
        if p == 1:
            p1 = nums[s]
            tp1,tp2 = self.divideConquer(nums,s+1,e,2)
            curr1 = [p1+tp1,tp2]
            
            p1 = nums[e]
            tp1,tp2= self.divideConquer(nums,s,e-1,2)
            curr2 = [p1+tp1,tp2]

            if curr1[0] > curr2[0]:
                return curr1[0],curr1[1]
            else:
                return curr2[0],curr2[1]            
        else:
            p2 = nums[s]
            tp1,tp2 = self.divideConquer(nums,s+1,e,1)
            curr1 = [tp1,p2+tp2]

            p2 = nums[e]
            tp1,tp2= self.divideConquer(nums,s,e-1,1)
            curr2 = [tp1,p2+tp2]

            if curr1[1] > curr2[1]:
                return curr1[0],curr1[1]
            else:
                return curr2[0],curr2[1]

        