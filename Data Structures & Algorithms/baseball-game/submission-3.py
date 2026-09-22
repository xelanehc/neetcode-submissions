class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0

        for o in operations:
            if o == "+":
                t = stack[-1] + stack[-2]
                stack.append(t)
                res += t
            elif o == "C":
                res -= stack.pop()
            elif o == "D":
                t = 2 * stack[-1]
                stack.append(t)
                res += t
            else:
                stack.append(int(o))
                res += stack[-1]
        
        return res