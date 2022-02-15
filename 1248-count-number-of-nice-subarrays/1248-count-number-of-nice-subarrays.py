class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [0 if num % 2 == 0 else 1 for num in nums]
        p = {0:1}
        pre_sum,counter = 0,0
        
        for num in nums:
            pre_sum += num
            
            if pre_sum - k in p:
                counter +=  p[pre_sum-k]
            
            if pre_sum in p:
                p[pre_sum] += 1
            else:
                p[pre_sum] = 1
                
        return counter
        