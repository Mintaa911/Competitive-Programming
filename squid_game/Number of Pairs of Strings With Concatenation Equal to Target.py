class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        cnt = 0
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if i != j:
                    num = nums[i]+nums[j]
                    if num == target:
                        cnt += 1

        return cnt
