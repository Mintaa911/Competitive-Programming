class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        def dfs(i,j,r,c):
            if i+r < 0 or j+c < 0 or i+r > (len(image) - 1) or j+c > (len(image[0]) - 1):
                return 
            
            if (i+r,j+c) in visited:
                return
            
            visited.add((i+r,j+c))
           
            
            if image[i+r][j+c] == image[i][j]:
                dfs(i+r,j+c,0,1)
                dfs(i+r,j+c,0,-1)
                dfs(i+r,j+c,1,0)
                dfs(i+r,j+c,-1,0)
            else:
                return 
                
            image[i+r][j+c] = newColor
            
            return
            
            
        visited = set()
        
        dfs(sr,sc,0,0)
        
        return image
