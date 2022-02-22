class Solution:
    def frequencySort(self, s: str) -> str:
        countDict = dict()
        heap = []
        
        for c in s:
            if c in countDict:
                countDict[c] += 1
            else:
                countDict[c] = 1
        
        for ch,val in countDict.items():
            heapq.heappush(heap,(-val,ch))
            
        resString = ""
        
        while heap:
            node = heapq.heappop(heap)
            
            for i in range(-node[0]):
                resString += node[1]
                
        return resString
            
