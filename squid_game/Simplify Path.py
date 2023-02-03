class Solution:
    def simplifyPath(self, path: str) -> str:
        lst = path.split('/')
        while len(lst) > 1 and lst[-1] == '':
            lst.pop()
        stack = []
        
        for s in lst:
            
            if s != '' and s != '..' and s != '.':
                stack.append(s)
            elif stack and s == '..':
                stack.pop()

        ans = '/'+"/".join(stack)
        return ans
