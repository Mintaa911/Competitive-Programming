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
               
        
        
#         if len(heights) == 1:
#             return 0
#         min_ladder, max_brick = [], []
#         previous = 1000001
        
#         idx = 0
        
#         while idx < len(heights):
#             gap = heights[idx] - previous
            
#             if gap <= 0 :
#                 previous = heights[idx]
                
#             elif gap > 0 and gap <= bricks:
#                 bricks -= gap
#                 heappush(max_brick,-gap)
#                 previous = heights[idx] 
#             elif gap > 0 and ladders > 0:
#                 ladders -= 1
#                 heappush(min_ladder,gap)
#                 previous = heights[idx]                       
                
#             elif gap > 0 and max_brick and min_ladder:
#                 if ((-max_brick[0]) - min_ladder[0] >= gap):
#                     bricks += (-max_brick[0]) - min_ladder[0]
#                     remove_l = heappop(min_ladder)
#                     remove_b = -heappop(max_brick)
#                     heappush(min_ladder,remove_b)
#                     heappush(max_brick,remove_l)
#                     bricks -= gap
#                     previous = heights[idx]
#                 else:
#                     break
#             else:
#                 break
                
#             idx += 1
            
        # return idx -1
                
