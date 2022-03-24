# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = deque([])
        q.append(root)
        large_in_row = []
        
        while q:
            l = len(q)
            row_max = q[0].val
            for i in range(l):
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
                if node.val > row_max :
                    row_max  = node.val
                    
            large_in_row.append(row_max)
            
        return large_in_row
        
        
        
