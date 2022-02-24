class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        
        for num in nums:
            heapq.heappush(heap,-num)
            
        largest = -10001
        for i in range(k):
            largest = heapq.heappop(heap)
            
        return -largest
