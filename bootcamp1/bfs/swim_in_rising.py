class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = dict()
        heap = [(grid[0][0], 0, 0)]
        
        heapify(heap)
        _min = grid[0][0]
        
        
        def isValid(i,j):
            return i >= 0 and i < n and j >= 0 and j < n and (i,j) not in visited
             
        
        while heap:
            v,r,c = heappop(heap)
            
            if v > _min:
                _min = v
            if r == (n-1) and c == (n-1):
                return _min
     
            if isValid(r, c+1):
                heappush(heap, (grid[r][c+1],r,c+1))
                visited[(r,c+1)] = 1
                
            if isValid(r, c-1):
                heappush(heap, (grid[r][c-1],r,c-1))
                visited[(r,c+1)] = 1
                
            if isValid(r+1, c):
                heappush(heap, (grid[r+1][c],r+1, c))
                visited[(r+1,c)] = 1

            if isValid(r-1, c):
                heappush(heap, (grid[r-1][c],r-1,c))
                visited[(r-1,c)] = 1

            
   
                
   
        
        
