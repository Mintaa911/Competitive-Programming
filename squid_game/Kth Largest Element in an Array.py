class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        k = (n-k)
        l,r = 0,n-1
        while True:
            idx = self.partition(l,r,nums)
            
            if idx < k:
                l = idx + 1
            elif idx > k:
                r = idx - 1
            else: return nums[idx]
                
                
    
    def partition(self,l,r,arr):
        idx = l
        for i in range(l,r):
            if arr[i] <= arr[r]:
                arr[i],arr[idx] = arr[idx],arr[i]
                idx += 1
                
        arr[idx],arr[r] = arr[r],arr[idx]
        return idx
                
        
