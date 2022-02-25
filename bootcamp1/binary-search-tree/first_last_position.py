class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left,right = 0,len(nums)-1
        best = ""
        first = False
        rng = []
        
        while left <= right:
            middle = (left + right)//2
            
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle-1
            else:
                best = middle
                right = middle - 1
                first = True
                
        if first:
            rng.append(best)
            left,right = 0,len(nums) - 1
            
            while left <= right:
                middle = (left + right)//2

                if nums[middle] < target:
                    left = middle + 1
                elif nums[middle] > target:
                    right = middle-1
                else:
                    best = middle
                    left = middle + 1
                    
            rng.append(best)
            return rng
        else:
            return [-1,-1]
        
