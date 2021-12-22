class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        answer = [0]*len(temperatures)
        
        for i in range(len(temperatures)):
            if len(stack) == 0:
                stack.append(i)
            elif temperatures[i] > temperatures[stack[-1]]:
                while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                    answer[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
                    
            else:
                stack.append(i)

            
        return answer