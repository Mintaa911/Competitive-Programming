class Solution:
    def minimumDeletions(self, s: str) -> int:
        prefix_b = [0]*(len(s)+1)
        suffix_a = [0]*(len(s)+1)

        for i in range(1,len(s)+1):
            c = s[i-1]
            if c == 'b':
                prefix_b[i] = prefix_b[i-1] + 1 
            else:
                prefix_b[i] = prefix_b[i-1]
        

        for i in range(len(s)-1,-1,-1):
            c = s[i]
            if c == 'a':
                suffix_a[i] = suffix_a[i+1] + 1 
            else:
                suffix_a[i] = suffix_a[i+1]
         
            
        cnt = len(s)
        for i in range(0,len(s)):
            cnt = min(cnt,(prefix_b[i]+suffix_a[i+1]))
        return cnt

