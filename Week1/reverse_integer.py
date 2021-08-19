class Solution:
    def reverse(self, x: int) -> int:
        if x != 0:
            reverse = ""
            if x < 0:
                reverse = "-"
                x *= -1
          
            while(x != 0):
                reverse += str(x%10)
                x = x//10
            return int(reverse) if -2**31 <= int(reverse) <= (2**31)-1 else 0
        return 0
