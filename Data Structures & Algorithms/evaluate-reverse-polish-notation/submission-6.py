class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            compute = tokens[i]
            if tokens[i] == "+":
                n1 = int(stack.pop())
                n2 = int(stack.pop())
                compute = n1 + n2
            elif tokens[i] == "-":
                n1 = int(stack.pop())
                n2 = int(stack.pop())
                compute = n2 - n1
            if tokens[i] == "/":
                n1 = int(stack.pop())
                n2 = int(stack.pop())
                compute = n2 / n1
            if tokens[i] == "*":
                n1 = int(stack.pop())
                n2 = int(stack.pop())
                compute = n1 * n2
            print(compute)
            stack.append(compute)
        return int(stack[0])