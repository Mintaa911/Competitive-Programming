class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n = len(equations)
        m = len(queries)
        relation = defaultdict(list)
        for i in range(n):
            a,b = equations[i]
            relation[a].append([b,values[i]])
            rvrs = 1/values[i]
            relation[b].append([a,rvrs])
            
        def dfs(c,d,visited):
            if c not in relation: return (False,0)
            if c in visited: return (False,0)
            visited.add(c)
            
            if c == d:
                return (True,1)
            
            for b,val in relation[c]:
                r = dfs(b,d,visited)
                
                if r[0]:
                    return (r[0], r[1]*val)
            visited.remove(c)
            return (False,0)
        
        ans = []
        for c,d in queries:
            res = dfs(c,d,set())
            if res[0]:
                ans.append(res[1])
            else:
                ans.append(-1.0)
        
        return ans
