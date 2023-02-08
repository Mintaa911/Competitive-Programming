class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        nei = defaultdict(int)
        for u,v in adjacentPairs:
            graph[v].append(u)
            graph[u].append(v)
            nei[u] += 1
            nei[v] += 1
        ends = []
        for ky,val in nei.items():
            if val == 1:
                ends.append(ky)
                
        
        res = self.helper(ends[0],ends[1],graph,set())

        return res

    def helper(self,node,end,graph,visited):
        if node == end:
            return deque([node])
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                r = self.helper(nei,end,graph,visited)
                r.appendleft(node)
        return r
