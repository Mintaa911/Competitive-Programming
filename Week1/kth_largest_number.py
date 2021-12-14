def kthLargestNumber(nums, k):
    sorted = merge(nums)
    return sorted[k-1]
        
def merge(nums):
    
    if len(nums) == 1:
        return nums
    
    m = len(nums)//2
    left = merge(nums[:m])
    right = merge(nums[m:])
    
    return merge_sort(left,right)
    
    
def merge_sort(self,left,right):
    merged = []
    while left and right:
        if int(left[0]) > int(right[0]):
            merged.append(left[0])
            left.pop(0)
        else:
            merged.append(right[0])
            right.pop(0)
            
    if left:
        return merged + left
    else:
        return merged + right