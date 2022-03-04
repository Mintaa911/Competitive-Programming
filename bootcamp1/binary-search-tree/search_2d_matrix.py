class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def searchRow(r):
            left,right = 0,n-1
            
            while left <= right:
                mid = left + (right-left)//2
                
                if matrix[r][mid] == target:
                    return mid
                elif matrix[r][mid] > target:
                    right = mid -1
                else:
                    left = mid + 1
                    
            return -1
        
        
        
        
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            result = searchRow(i)
            if  result != -1:
                return True
        
        return False
