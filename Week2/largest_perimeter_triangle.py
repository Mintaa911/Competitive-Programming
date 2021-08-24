class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            max_idx = i
            for j in range(i+1, len(nums)):
                if nums[j] > nums[max_idx]:
                    max_idx = j
            nums[i],nums[max_idx] = nums[max_idx],nums[i]
            
            x = 0
            while i > 1 and x <= i -2:  
                if nums[x] < nums[x+1] + nums[x+2]:
                    return nums[x] + nums[x+1] + nums[x+2]
                x += 1
        return 0
