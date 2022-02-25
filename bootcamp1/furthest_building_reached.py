from heapq import *
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights)-1):
            gap = heights[i+1] - heights[i]
            
            if gap > 0:
                heappush(heap,gap)
            
            if len(heap) > ladders:
                bricks -= heappop(heap)
                
            if bricks < 0:
                return i
            
            
        return i+1
