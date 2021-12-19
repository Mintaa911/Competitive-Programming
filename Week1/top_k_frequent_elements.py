from collections import Counter
class Solution:
    def topKFrequent(nums, k) :
        dictNum = Counter(nums)
        topFrequent = dictNum.most_common(k)
        
        return [frq[0] for frq in topFrequent]