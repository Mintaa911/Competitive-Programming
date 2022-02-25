class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        
        for row in grid:
            left,right = 0,len(row)-1
            rng = []
            first = -1
            while left <= right:
                mid = (left + right)//2
                
                if row[mid] < 0:
                    right = mid -1
                    first = mid
                    
                    
                if row[mid] >= 0:
                    left = mid + 1
                
            left,right = 0,len(row)-1
          
            if first >= 0:
                rng.append(first)
                while  left <= right:
                    mid = (left + right)//2

                    if row[mid] < 0:
                        left = mid + 1
                    if row[mid] >= 0:
                        left = mid + 1
                        
                rng.append(left)
                
                count += (rng[1] - rng[0])

        return count
