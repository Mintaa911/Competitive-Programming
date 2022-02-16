class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = dict()
        for i in range(len(nums)):
            if nums[i] == 0:
                if 0 not in zeros:
                    zeros[0] = i
                    
            elif 0 in zeros and nums[i] != 0:
                nums[zeros.get(0)],nums[i] = nums[i],nums[zeros.get(0)]
                zeros[0] += 1
         
                
            