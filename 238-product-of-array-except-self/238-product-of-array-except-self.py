class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_product = [1 for i in range(len(nums))]
        suf_product = [1 for i in range(len(nums))]
        
        for i in range(1,len(nums)):
            pre_product[i] = pre_product[i-1] * nums[i-1]
            
        for j in range(len(nums)-2,-1,-1):
            suf_product[j] = suf_product[j+1] * nums[j+1]
            
        return [suf_product[idx] * pre_product[idx] for idx in range(len(nums))]