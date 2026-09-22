class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for o in operations:
            if o == "+":
                a, b = stack[-1], stack[-2]
                res = a + b
                stack.append(res)
                continue
            elif o == "C":
                stack.pop()
                continue
            elif o == "D":
                a = stack[-1]
                res = 2 * a
                stack.append(res)
            else:
                stack.append(int(o))
        
        return sum(stack)