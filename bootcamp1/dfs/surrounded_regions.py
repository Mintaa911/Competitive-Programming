class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead. 30min
        """
        def validCell(r,c):
            return r >= 0 and r < m and c >= 0 and c < n
        
        def dfs(r,c):  
            if not validCell(r,c):
                return         
            if board[r][c] != "O":
                return
            board[r][c] = -1
            
            up = dfs(r-1,c)
            bottom = dfs(r+1,c)
            left = dfs(r,c-1)
            right = dfs(r,c+1) 
            return

        m = len(board)
        n = len(board[0]) 
        for i in range(m):
            if board[i][0] == "O":
                dfs(i,0)       
        for i in range(m):
            if board[i][n-1] == "O":
                dfs(i,n-1)         
        for j in range(n):
            if board[0][j] == "O":
                dfs(0,j)
        for j in range(n):
            if board[m-1][j] == "O":
                dfs(m-1,j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == -1:
                    board[i][j] = "O"
        
