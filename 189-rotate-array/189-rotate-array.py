class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        7,6,5,4,3,2,1
        """    
        def reverseFunc(nums):
            start,end = 0, k-1
    
            while start < end:
                nums[start],nums[end] = nums[end],nums[start]
                start += 1
                end -= 1
                
            start,end = k, len(nums)-1
 
            while start < end:
                nums[start],nums[end] = nums[end],nums[start]
                start += 1
                end -= 1
        
        
        if len(nums) > 1:
            k = k % len(nums)
            nums.reverse()
            reverseFunc(nums)
        
        
        