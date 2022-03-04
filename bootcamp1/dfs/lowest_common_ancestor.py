# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        def dfs(node,depth):
            if not node:
                return (-1,None)
            if node.left == node.right:
                return (depth, node)
            
            left = dfs(node.left,depth+1)
            right = dfs(node.right,depth+1)
            
            if left[0] == right[0]:
                return (left[0],node)
            elif left[1] or right[1]:
                return max(left,right)
            
            
        
        return dfs(root,0)[1]
