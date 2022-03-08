class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        
        if n == 1:
            return ""
        
        for i in range(n):
            if n % 2 != 0 and  i == (n)//2:
                continue
                
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
            
            if i == n-1: 
                return palindrome[:i] + 'b' + palindrome[i+1:]
            
        
