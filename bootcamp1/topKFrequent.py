class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        countDict = dict()
        
        for num in nums:
            if num in countDict:
                countDict[num] += 1
            else:
                countDict[num] = 1
        
        for ky in countDict:
            heapq.heappush(heap,(-countDict[ky],ky))
        
        return [heapq.heappop(heap)[1] for i in range(k)]
