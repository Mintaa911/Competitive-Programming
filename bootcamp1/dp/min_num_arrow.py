class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        heap = points
        heapify(heap)
        
        rng = heappop(heap)
        merged = [[rng]]
    
        while heap:
            point = heappop(heap)
            
            if point[0] <= rng[1]:
                if merged:
                    merged.pop()
                merged.append([rng[0],min(point[1],rng[1])])
                rng = merged[-1]
            else:
                
                merged.append(point)
                rng = point
        
        return len(merged)
        
