class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0

        for o in operations:
            if o == "+":
                stack.append(stack[-1] + stack[-2])
                res += stack[-1] + stack[-2]
            elif o == "C":
                res -= stack.pop()
            elif o == "D":
                stack.append(2 * stack[-1])
                res += 2 * stack[-1]
            else:
                stack.append(int(o))
                res += stack[-1]
        
        return sum(stack)