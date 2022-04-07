class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        
        
        d = dict()
        
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        stack = [s[0]]
        d[s[0]] -= 1
        for i in range(1,n):
            d[s[i]] -= 1
            
            if s[i] in stack:
                continue
            while stack and s[i] < stack[-1] and d[stack[-1]] > 0:
                
                stack.pop()
                
            stack.append(s[i])
            
        
        
        
        
        return "".join(stack)
 
            
                
        
