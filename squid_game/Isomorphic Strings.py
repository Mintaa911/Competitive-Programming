class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        n = len(s)
        _set = set()
        for i in range(n):
            if s[i] in d:
                if d[s[i]] == t[i]:
                    
                    continue
                else:
                    return False
            elif t[i] not in _set:
                d[s[i]] = t[i]
                _set.add(t[i])           
            else: return False
                
        return True
