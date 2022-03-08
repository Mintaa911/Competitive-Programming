class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        def validIdx(idx):
            return (idx < len(flowerbed) and flowerbed[idx] == 0) or idx >= len(flowerbed)

        start = 0
        prev = False
        if len(flowerbed) == 1 and flowerbed[0] == 0 and n == 1:
            return True
        
        while n > 0 and start < len(flowerbed):
            if flowerbed[start] == 0:
                if prev:
                    prev = not prev
                    start += 1
                    continue
                if validIdx(start+1):
                    flowerbed[start] = 1
                    prev = True
                    n -= 1
                else:
                    prev = not prev
            else:
                prev = True
                    
            start += 1
   
        return True if n == 0 else False
            
        
