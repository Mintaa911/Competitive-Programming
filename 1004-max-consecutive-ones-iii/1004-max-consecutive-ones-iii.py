class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left,right = 0,0
        zeros_queue, flip = collections.deque([]),k
        max_length = 0
        
        while right < len(nums):
            
            if nums[right] == 0 and flip > 0:
                flip -= 1
                zeros_queue.append(right)
            elif nums[right] == 0 and flip == 0:
                max_length = max(max_length,right-left)
                if zeros_queue:
                    left = zeros_queue.popleft() + 1
                    zeros_queue.append(right)       
                else:
                    left = right+1
            
            right += 1
            
        max_length = max(max_length,right-left)
        
        return max_length