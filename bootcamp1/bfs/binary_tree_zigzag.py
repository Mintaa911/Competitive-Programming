# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        q = deque([root])
        
        reverse = False
        result = []
        while q:
            len_q = len(q)
            n_level = deque([])
            for i in range(len_q):
                popped = q.popleft()
                
                if not popped:
                    continue
                if reverse:
                    n_level.appendleft(popped.val)
                else:
                    n_level.append(popped.val)  
                
                if popped.left == popped.right:
                    continue
                
                q.append(popped.left)
                q.append(popped.right)
            
            reverse = not reverse 
            
            result.append(n_level)
            
        return result
