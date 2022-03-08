class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        q = deque(list(senate))
        n = len(q)
        
        while q:
            popped = q.popleft()
            if popped == 0:
                
                continue
            
            idx = 0
            while idx < len(q) and (q[idx] == 0 or q[idx] == popped):
                idx += 1
            
            if idx < len(q):
                q[idx] = 0
                q.append(popped)
            else:
                q.appendleft(popped)
                break
   
        return "Radiant" if q[0] == "R" else "Dire"
       
    
                
                
            
            
