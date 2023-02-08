class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        _set = set(nums)
        lst = list(_set)
        lst.sort()
        if len(lst) < 3:
            return lst[-1]
        else:
            return lst[-3]
