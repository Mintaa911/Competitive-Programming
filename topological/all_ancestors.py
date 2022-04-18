class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        indegree = [0]*n
        dependency = defaultdict(list)
        
        for edge in edges:
            indegree[edge[1]] += 1
            dependency[edge[0]].append(edge[1])
            
        ans = [set() for i in range(n)]
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
                
        while q:
            node = q.popleft()
            for val in dependency[node]:
                indegree[val] -= 1
                ans[val].add(node)
                ans[val].update(ans[node])
                if indegree[val] == 0:
                    q.append(val)
                    
        
        for i in range(n):
            ans[i] = sorted(ans[i])
            
        return ans
