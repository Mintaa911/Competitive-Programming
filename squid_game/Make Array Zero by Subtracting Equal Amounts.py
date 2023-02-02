class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        heap = []
        for num in nums:
            if num > 0:
                heappush(heap,num)
        op = 0
        while heap and heap[0] > 0:
            num = heappop(heap)
            for i in range(len(heap)):
                heap[i] -= num
            while heap and heap[0] == 0:
                heappop(heap)
            op += 1

        return op
