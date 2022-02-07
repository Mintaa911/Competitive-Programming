class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = dict()
        
        for i in range(len(nums)):
            d = target - nums[i]
            if d in myDict:
                return [myDict.get(d),i]
            
            myDict[nums[i]] = i