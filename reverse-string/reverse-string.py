class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(idx, s):
            if idx >= len(s):
                return
            
            curS = s[idx]
            helper(idx+1,s)
            l = len(s)
            s[l-idx-1] = curS   
        
        helper(0,s)