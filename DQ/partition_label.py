class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        partitions = []
        start_part = -1
        end_part = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[j] == s[i] and j > end_part:
                    end_part = j
                                   
            if end_part == i:
                partitions.append(end_part - start_part)
                start_part = end_part
                end_part = end_part + 1
        
            
        return partitions
