from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def willRot(r,c,m,n):
            return True if r >= 0 and r < m and c >= 0 and c < n and grid[r][c] == 1 else False
        
        
        m = len(grid)
        n = len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        max_minute = 0
        
        q = deque([])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j,2))
        
        while q:
            length_q = len(q)
            rotted = False
            for i in range(length_q):
                r,c,val = q.popleft()
                
                if val == 2:
                    for direction in directions:
                        row,col = direction

                        if willRot(row+r,col+c,m,n):
                            rotted = True
                            grid[row+r][col+c] = val
                            q.append((row + r, col + c,2))
        
            if rotted:
                max_minute += 1
            
            
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
                
        return max_minute
                            
                
                    
                
                
        
