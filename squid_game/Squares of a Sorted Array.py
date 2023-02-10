class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        left,right = 0,len(nums)-1
        
        while left <= right:
            mid = (left+right)//2
            
            if nums[mid] < 0:
                left = mid + 1
            else:
                right = mid - 1
             
        nums = [num**2 for num in nums]
        x = left -1
        y = left
        
        r = []
        while x > -1 and y < len(nums):
            
            if nums[x] < nums[y]:
                r.append(nums[x])
                x -= 1
            else:
                r.append(nums[y])
                y += 1
            
            
        
        while x > -1:
            r.append(nums[x])
            x -= 1
        while y < len(nums):
            r.append(nums[y])
            y += 1
            
        return r
        
