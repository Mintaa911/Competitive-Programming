class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def inverter(s1):
            s2 = '1'*len(s1)
            b = bin(int(s1,2)^int(s2,2))[2:]
            return b
        
        def helper(s,i):
            if i > n:
                return s
            
            Si = s + '1' + inverter(s)[::-1]
            i += 1
            return helper(Si,i)
    
        return helper('0',1)[k-1]