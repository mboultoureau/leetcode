class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if len(tokens[i]) > 1 or tokens[i][0].isdigit():
                stack.append(int(tokens[i]))
            else:
                b = stack.pop()
                a = stack.pop()
                
                if tokens[i][0] == '+':
                    stack.append(a + b)
                elif tokens[i][0] == '-':
                    stack.append(a - b)
                elif tokens[i][0] == '*':
                    stack.append(a * b)
                elif tokens[i][0] == '/':
                    stack.append(int(a / b))

        return stack.pop()
