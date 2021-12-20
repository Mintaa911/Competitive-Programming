class Solution:
    def reverseParentheses(s): 
        stack = []
        for c in s:
            if c == ")":
                subS = []
                while stack[-1] != "(":
                    subS.append(stack.pop())

                stack.pop()
                for rc in subS:
                    stack.append(rc)
                    
            else:
                stack.append(c)
                
        return "".join(stack)