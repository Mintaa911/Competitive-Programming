# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        q = deque([root])
        
        while q:
            length_q = len(q)
            l,r = 0,length_q-1
            
            while l < r:
                if q[l] and not q[r] or not q[l] and q[r]:
                    return False
                if q[l] and q[r] and q[l].val != q[r].val:
                    return False
                r -= 1
                l +=1
                
            for i in range(length_q):
                cur_node = q.popleft()
                
                if not cur_node:
                    continue
                
                q.append(cur_node.left)
                q.append(cur_node.right)
                    
                
        return True
                
            
       
            
            
            
              
