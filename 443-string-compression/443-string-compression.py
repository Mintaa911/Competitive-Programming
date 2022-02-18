class Solution:
    def compress(self, chars: List[str]) -> int:
        left,right,idx = 0,1,0
        
        while right < len(chars):
            if chars[right] != chars[left]:             
                chars[idx] = chars[left]
                idx += 1
                
                if right-left > 1:
                    for i in str(right-left):    
                        chars[idx] = i
                        idx += 1
                left = right
                
                
            right += 1
            
        if right - left == 1:
            chars[idx] = chars[left]
            idx += 1
        elif right - left > 1:
            chars[idx] = chars[left]
            idx += 1
            
            if right-left > 1:
                for i in str(right-left):    
                    chars[idx] = i
                    idx += 1
                    
        chars = chars[:idx]
        return len(chars)