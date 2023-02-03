# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res, start_idx = defaultdict(list),0
        def helper(node,i,j):
            nonlocal res
            
            if not node: return             
            if node.left == node.right:
                heappush(res[j],(i,node.val))
                return
            heappush(res[j],(i,node.val))            
            helper(node.left,i+1,j-1)
            helper(node.right,i+1,j+1)
            
        helper(root,0,0)
        ans = []
        for k in sorted(res.keys()):
            col = res[k]
            temp = []
            while col:
                temp.append(heappop(col)[1])
            ans.append(temp)
    
        return ans
