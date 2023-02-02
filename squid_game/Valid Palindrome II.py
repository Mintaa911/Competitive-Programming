class Solution:
    def validPalindrome(self, s: str) -> bool:
        start,end = 0,len(s)-1
        while start < end:
            if s[start] != s[end]:
                front = self.helper(s[start:end])
                back = self.helper(s[start+1:end+1])
                return front or back
            start += 1
            end -= 1
        return True

    def helper(self,s):
        start,end = 0,len(s)-1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1

        return True
        

