class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        
        for stone in stones:
            heapq.heappush(heap,-stone)
        
        while len(heap) > 1:
            
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            
            if x != y:           
                heapq.heappush(heap,-(y-x))
      
        if heap:
            return -heapq.heappop(heap)
        else:
            return 0
