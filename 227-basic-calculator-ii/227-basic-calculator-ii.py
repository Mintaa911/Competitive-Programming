class Solution:
    def calc(self,num1,num2,operator):
        if operator == '/':
            result = num2//num1
        elif operator == '*':
            result = num2 * num1
        elif operator == '+':
            result = num2 + num1
        else:
            result = num2 - num1
        return result
        
    def calculate(self, s: str) -> int:
        op = {'*':2, '/':2, '+':1, '-':1}

        numbers = []
        operators = []
        t = 0
        while t < len(s):
            if s[t].isdigit():
                num = ''
                while t < len(s) and s[t].isdigit():
                    
                    num += s[t]
                    t += 1
                numbers.append(int(num))
            elif s[t] in "/*+-":
                if len(operators) == 0:
                    operators.append(s[t])

                elif op[operators[-1]] < op[s[t]]:
                    operators.append(s[t])
                    
                else:
                    while len(operators) > 0 and op[operators[-1]] >= op[s[t]]:
                        num1 = numbers.pop()
                        num2 = numbers.pop()

                        operator = operators.pop()
                        result = self.calc(num1,num2,operator)
                        numbers.append(result)

                    operators.append(s[t])
                t += 1
            else:
                t += 1
        if len(operators) == 0:
            return int(s)

        
        while len(operators) != 0:
            n1 = numbers.pop()
            n2 = numbers.pop()
            r = self.calc(n1,n2,operators.pop())
            numbers.append(r)
            
                    
        return numbers.pop()