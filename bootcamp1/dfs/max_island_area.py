class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        max_area = 0
        
        def dfs(r,c):
            if r < 0 or c < 0 or r >= m or c >= n:
                return 0
            
            if grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            
            top = dfs(r-1,c)
            bottom = dfs(r+1,c)
            left = dfs(r,c-1)
            right = dfs(r,c+1)
            
            
            return top + bottom + left + right + 1
            
            
        
        for row in range(m):
            for col in range(n):
                max_area = max(dfs(row,col), max_area)
        
          
    
        return max_area
   
