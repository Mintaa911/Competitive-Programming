class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        def validCell(r,c):
            return r >= 0 and r < m and c >= 0 and c < n 
        
        def dfs(r,c):
            
            for direction in directions:
                row,col = direction
                
                if validCell(r+row, c+col) and  grid[r+row][c+col] == 1:
                    grid[r+row][c+col] = 0
                    dfs(r+row, c+col)

        
        m = len(grid)
        n = len(grid[0])
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        
        
        for i in range(m):
            if grid[i][0] == 1:
                grid[i][0] = 0
                dfs(i,0)
                
        for i in range(m):
            if grid[i][n-1] == 1:
                grid[i][n-1] = 0
                dfs(i,n-1)
                
        for j in range(n):
            if grid[0][j] == 1:
                grid[0][j] = 0
                dfs(0,j)
                
        for j in range(n):
            if grid[m-1][j] == 1:
                grid[m-1][j] = 0
                dfs(m-1,j)
        
        
        land = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    land += 1
                    
                    
        return land
                
        
