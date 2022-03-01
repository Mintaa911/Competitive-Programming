class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        total_province = 0
        visited = set()
        n = len(isConnected)
        
        def dfs(city,idx):
            
            for i in range(n):
                if i not in visited and isConnected[city][i] == 1:
                    visited.add(i)
                    dfs(i,i+1)            
                
        for v in range(n):
            if v in visited:
                continue
                
            visited.add(v)
            dfs(v,v+1)
            total_province += 1
            
        return total_province
