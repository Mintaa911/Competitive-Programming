class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        left_ptr,right_ptr = 0,0
        
        while right_ptr < len(nums):
            
            if nums[left_ptr] < nums[right_ptr]:
                left_ptr += 1
                nums[left_ptr] = nums[right_ptr]
            
            right_ptr += 1
            
        return left_ptr + 1