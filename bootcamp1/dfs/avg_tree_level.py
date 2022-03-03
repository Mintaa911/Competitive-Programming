from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        avg = []
        q = deque([root])
        
        while q:
            q_length = len(q)
            layer_sum = 0
            for i in range(q_length):
                cur_node = q.popleft()
                
                layer_sum += cur_node.val
                
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
                    
            
            layer_avg = layer_sum/q_length
            
            avg.append(float(format(layer_avg,'.5f')))
                
                
        
        return avg
        
        
        
        
#         avg = [float(format(root.val,'.5f'))]

        
#         q = deque([root])
#         temp_q = deque([])
        
#         while q or temp_q:
            
#             if not q:
                
                
#                 layer_avg = 0
                
#                 while temp_q:
#                     popped = temp_q.popleft()
#                     q.append(popped)
#                     layer_avg += popped.val
                
                
#                 layer_avg /= len(q)
#                 avg.append(float(format(layer_avg,'.5f')))
            

#             cur_node = q.popleft()
            
#             if cur_node.left:
#                 temp_q.append(cur_node.left)
            
#             if cur_node.right:
#                 temp_q.append(cur_node.right)
            
#         return avg
            
            
      
        
            
            
