class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opearators = {'+','-','*','/'}
        for val in tokens:
            if val not in opearators:
                stack.append(val)
                continue
            val1 = stack.pop()
            val2 = stack.pop()
            val1, val2 = int(val1), int(val2)
            if val == '+':
                stack.append(val1+val2)
            elif val == '-':
                stack.append(val2-val1)
            elif val == '*':
                stack.append(val2*val1)
            else:
                stack.append(val2/val1)
        return int(stack[-1])
        