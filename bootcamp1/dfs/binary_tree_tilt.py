# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        
        def tilt(node):
            if not node:
                return (0,0)
            if node.left == node.right:
                return (0, node.val)
            
            left = tilt(node.left)
            right = tilt(node.right)
            
            tilt_val = abs(left[1] - right[1]) + left[0] + right[0]
            sub_tree_val = left[1] + right[1] + node.val
            
            return (tilt_val, sub_tree_val)
            
            
        return tilt(root)[0]
