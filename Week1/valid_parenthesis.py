def isValid(str):
    stack = []
    dictBrackets = {"{":"}","[":"]","(":")"}
    for bracket in s:
        if len(stack) == 0:             
            stack.append(bracket)             
        elif stack[-1] in dictBrackets and dictBrackets[stack[-1]] == bracket:
            
            stack.pop()
        else:
            stack.append(bracket)
        

    return len(stack) == 0