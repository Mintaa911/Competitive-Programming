import math
class Solution:
    def evalRPN(tokens):
        operations = {"+":"+","-":"-","/":"/","*":"*"}
        stack = []

        for token in tokens:
            if token.startswith('-') and token[1:].isdigit():
                stack.append(token)
            elif token.isnumeric():
                stack.append(token)
            else: 

                a = stack.pop()
                b = stack.pop()
                result = eval(f'{b} {operations[token]} ({a})')
                if token == '/' and result > 0:
                    result = math.floor(result)
                else:
                    result =  math.ceil(result)
                    
                stack.append(result)
        return stack.pop()