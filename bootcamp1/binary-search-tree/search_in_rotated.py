class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def searchTarget(left,right):
            while left <= right:
                mid = left + (right-left)//2
            
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid -1
                else:
                    left = mid + 1
                    
            return -1
            
    
        def findK():
            
            left,right = 0,len(nums)-1
            
            while left < right:
                mid = left + (right-left)//2
                
                if nums[mid] < nums[n-1]:
                    right = mid
                elif nums[mid] > nums[n-1]:
                    left = mid + 1
                    
            return n - left
            
            
            
        n = len(nums)
        k = findK()
        
        first = nums[:n-k]
        second = nums[n-k:]
        
        t1 = searchTarget(0,n-k-1)
        t2 = searchTarget(n-k,n-1)
        
        return max(t1,t2)
        
        
