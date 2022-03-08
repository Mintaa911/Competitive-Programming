class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        
        def validIdx(idx):
            return idx >= 0 and idx < len(arr) and idx not in visited
        
        
        n = len(arr)
        q = deque([])
        visited = set()
        q.append(start)
        
        while q:
            len_q = len(q)
            
            for i in range(len_q):
                popped = q.popleft()
                visited.add(popped)
                
                if arr[popped] == 0:
                    return True
                
                for j in [arr[popped],-arr[popped]]:
                    if not validIdx(popped + j):
                        continue
                        
                    q.append(popped + j)
                
                    
        return False       
                    
