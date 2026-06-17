class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+','-','*','/']
        stack = []
        for char in tokens:
            if char in operators:
                num_1 = int(stack.pop())
                num_2 = int(stack.pop())
                if char == "+":
                    stack.append(num_1 + num_2)
                elif char == '-':
                    stack.append(num_2 - num_1)
                elif char == '*':
                    stack.append(num_2 * num_1)
                elif char == '/':
                    stack.append(int(num_2 / num_1))
            else: 
                stack.append(char)
        return int(stack[0])