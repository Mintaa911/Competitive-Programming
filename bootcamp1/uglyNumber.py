class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglyDict = dict({1:1})
        uglyHeap = [1]
        heapq.heapify(uglyHeap)
        count = 0
        factors = [2,3,5]
        
        while count < n-1:
            poped = heapq.heappop(uglyHeap)
            lst = [poped * i for i in factors]
            
            for i in range(len(lst)):
                if lst[i] not in uglyDict:
                    uglyDict[lst[i]] = 1
                    heapq.heappush(uglyHeap,lst[i])
         
            count += 1
       
        return heapq.heappop(uglyHeap)
        
