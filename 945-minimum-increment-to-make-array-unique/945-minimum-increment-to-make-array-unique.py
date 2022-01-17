class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        for i in range(len(nums)):
            if i == 0:
                continue
            d = nums[i-1] - nums[i]
            if d >= 0:
                nums[i] += d + 1
                moves += d +1
        return moves
            