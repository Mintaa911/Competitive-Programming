class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum,counter,cur_sum = dict({0:1}),0,0
        
        for num in nums:
            cur_sum += num
            
            if (cur_sum - k) in pre_sum:
                counter += pre_sum[cur_sum - k]
            
            if cur_sum in pre_sum:
                pre_sum[cur_sum] += 1
            else:
                pre_sum[cur_sum] = 1
                
        return counter
            
            
        
        
#         counter = 0
#         for i in range(len(nums)):
#             cur_sum = nums[i]
#             if cur_sum == k:
#                 counter += 1
#                 continue
#             for j in range(i+1,len(nums)):
#                 cur_sum += nums[j]
                
#                 if cur_sum == k:
#                     counter += 1
            
            
#         return counter

        
        
            