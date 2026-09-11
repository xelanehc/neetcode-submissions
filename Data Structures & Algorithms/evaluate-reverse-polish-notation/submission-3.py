class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            cur = tokens[i]
            if cur == "+":
                stack.append(stack.pop() + stack.pop())
            elif cur == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif cur == "*":
                stack.append(stack.pop() * stack.pop())
            elif cur == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(cur))
        return stack[0]