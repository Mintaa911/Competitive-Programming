class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        
        def dp(i,visited):
            if i in memo:
                return memo[i]
            
            if i in visited:
                return False
            if graph[i] == []:
                memo[i] = True
                return memo[i]
      
            visited.add(i)
            terminal = True
            for node in graph[i]:
                terminal = terminal and dp(node,visited)
                
            memo[i] = terminal
            return memo[i]
        
        safe = []
        memo = dict()
        for i in range(n):
            visited = set()
            val = False
        
            if i in memo:
                val = memo[i] 
                
            val = dp(i,visited)
            if val:
                safe.append(i)
                
        safe.sort()
        
        return safe
