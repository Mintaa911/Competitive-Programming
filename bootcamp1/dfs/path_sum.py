class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def pathSum(node,preSum):
            if not node:
                return False
            if node.left == node.right:
                return (preSum + node.val) == targetSum
            
            return pathSum(node.left,preSum+node.val) or pathSum(node.right, preSum+node.val)
                   
        if not root:
            return False
        
 
        
        return pathSum(root,0)
