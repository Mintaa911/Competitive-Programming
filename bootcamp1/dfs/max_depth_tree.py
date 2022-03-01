class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        
        def dfs(node):
            depth = 0
            for child in node.children:
                if child.children:
                    depth = max(dfs(child), depth)
                    
            return depth + 1
        
        if not root:
            return 0
        elif not root.children:
            return 1
        
        return dfs(root) + 1
