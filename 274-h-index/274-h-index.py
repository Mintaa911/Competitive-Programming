class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        if len(citations)==0:
            return 0
        for i in range(len(citations)):
            if citations[i]<=i+1:
                if citations[i]==i+1:
                    return i+1
                else:
                    return i
        return i+1        
