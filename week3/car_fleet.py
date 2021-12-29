class Solution:
    def carFleet(self, target,position,speed):
        stack = []
        time_left = [(position[i],(target-position[i])/speed[i]) for i in range(len(speed))]
        time_left.sort(reverse=True)
        
        for p,tl in time_left:
            if len(stack) == 0:
                stack.append(tl)
            elif tl > stack[-1]:
                stack.append(tl)
        return len(stack)