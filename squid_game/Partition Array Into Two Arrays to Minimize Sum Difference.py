class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        # abs(s - 2*i)
        # i <= s / 2
        def f(A):
            n = len(A)
            a = [set() for _ in range(n+1)]
            a[0].add(0)
            for i in A:
                for j in range(n,0,-1):
                    for v in a[j-1]:
                        a[j].add(v+i)
            return list(map(sorted, a))
        s = sum(nums)
        n = len(nums)
        a = f(nums[:n//2])
        b = f(nums[n//2:])
        res = float('inf')
        for i in range(n//2+1):
            j = len(b[n//2-i]) - 1
            for v in a[i]:
                while j >= 0 and v + b[n//2-i][j] > s // 2:
                    j -= 1
                if j >=0:
                    res = min(res, s - 2 * (v+b[n//2-i][j]))
        return res
