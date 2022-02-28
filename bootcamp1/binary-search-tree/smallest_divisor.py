class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        left,right = 0,n-1
        nums.sort()
        result = 0
        
        while left <= right:
            mid = (left+right)//2
            result = (mid+1)
            
            for i in range(mid+1,n):
                result += math.ceil(nums[i]/nums[mid])

            if result > threshold:
                left = mid + 1
            elif result <= threshold:
                right = mid - 1
                
        small = nums[left]
        print(small)
        left,right = 1,nums[left]
      
        
        
        while left <= right:
            mid = (left+right)//2
            result = 0
            
            for num in nums:
                result += math.ceil(num/mid)
                
            if result > threshold:
                left = mid + 1
            elif result <= threshold:
                right = mid - 1  

        return min(small,left)
