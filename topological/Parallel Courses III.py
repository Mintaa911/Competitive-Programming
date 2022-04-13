class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indegree = [0]*n
        
        dependency = defaultdict(list)
        
        for r in relations:
            indegree[r[1]-1] += 1
            dependency[r[0]].append(r[1])
        heap = []
        
        for i in range(n):
            if indegree[i] == 0:
                heappush(heap,(time[i],i+1))
                
        res = 0
        while heap:
            l = len(heap)
            _max = 0
            
            for i in range(l):
                c = heappop(heap)
                _max = max(_max, c[0])
                
                
                for d in dependency[c[1]]:
                    indegree[d-1] -= 1
                    if indegree[d-1] == 0:
                        time[d-1] += time[c[1]-1]
                        heappush(heap, (time[d-1], d))

                
            res = _max
            
        return res
            
