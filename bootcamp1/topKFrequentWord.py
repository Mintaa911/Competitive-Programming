class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        countWords = dict()
        heap = []
        
        for word in words:
            if word in countWords:
                countWords[word] += 1
            else:
                countWords[word] = 1
        
        for word, count in countWords.items():
            heapq.heappush(heap,(-count,word))
        
        topFreq = [heapq.heappop(heap) for i in range(k)]
        
        heap = []
        for wordTp in topFreq:
            heapq.heappush(heap,wordTp)
        
        return [heapq.heappop(heap)[1] for i in range(len(heap))]
