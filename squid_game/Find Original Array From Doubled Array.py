class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        changed.sort()
        d = defaultdict(int)
        for num in changed:
            d[num] += 1
        original = []
        for num in changed:
            while d[num] > 0 and (d[num*2]) > 0:
                if num == 0 and d[num] < 2:
                    break
                d[num] -= 1
                d[num*2] -= 1
                original.append(num)
        
        return original if len(original) * 2 == n else []
                
