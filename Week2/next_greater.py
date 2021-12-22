class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        greatDict = dict()
        r = []
        
        for num in nums2:
            if len(stack) == 0:
                stack.append(num)
            elif num > stack[-1]:
                while len(stack) > 0 and num > stack[-1]:
                    greatDict[stack.pop()] = num
                stack.append(num)
            else:
                stack.append(num)
            
        for num in nums1:
            if num in greatDict:
                r.append(greatDict[num])
            else:
                r.append(-1)
        return r