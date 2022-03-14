class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        min_path = 2 ** 31
        
        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i == len(triangle) - 1:
                return triangle[i][j]
      
            stay = dfs(i+1, j)
            moved = dfs(i+1, j+1)

            memo[(i,j)] = min(stay,moved) + triangle[i][j]
           
            return memo[(i,j)]
            
            
            
        memo = dict()
        return dfs(0,0)
            
            
        
        
