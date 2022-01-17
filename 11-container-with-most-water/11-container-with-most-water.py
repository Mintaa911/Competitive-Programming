class Solution:
    def maxArea(self, height: List[int]) -> int:
        front = 0
        rear = len(height)-1
        max_area = 0
        min_height = 0
        while(front != rear):
            width = rear - front
            
            if height[rear] > height[front]:
                min_height = height[front]
                front += 1
            else:
                min_height = height[rear]
                rear -= 1
            curr_area = width * min_height
                
            max_area = max(curr_area,max_area)
        
        return max_area
        