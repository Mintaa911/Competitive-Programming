class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        _sum = float('-inf')
        max_sum = float('-inf')
        for num in nums:
            _sum = max(_sum+num,num)
            max_sum = max(max_sum,_sum)
        return max_sum
            
