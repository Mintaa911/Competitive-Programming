class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        s = self.countAndSay(n-1)
        left,right = 0,0
        new_say = ""
        
        if len(s) == 1:
            return "1"+s
        else:
            while right < len(s):
                if s[right] != s[left]:
                    new_say += str(right-left) + s[left]
                    left = right
                
                right += 1
                
            new_say += str(right-left) + s[left]
            
            return new_say