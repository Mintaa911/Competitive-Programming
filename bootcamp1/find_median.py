from heapq import *
class MedianFinder:

    def __init__(self):
        self.size = 0   
        self.max_left, self.min_right  = [],[]

    def addNum(self, num: int) -> None:
        if self.size % 2 == 0:
            element = -heappushpop(self.min_right,num)
            heappush(self.max_left,element)
        else:
            element = -heappushpop(self.max_left,-num)
            heappush(self.min_right,element)
        self.size += 1
        
    def findMedian(self) -> float:
        if self.size % 2 != 0:
            return -self.max_left[0]
        else:
            m1 = -self.max_left[0]
            m2 = self.min_right[0]
            median = float( "{:.5f}".format( (m1+m2)/2 ) )
            
            return median
