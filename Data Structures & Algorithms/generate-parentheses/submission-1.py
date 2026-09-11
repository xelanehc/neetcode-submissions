class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def parentheses(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                parentheses(openN + 1, closeN)
                stack.pop()
            if closeN < openN:
                stack.append(")")
                parentheses(openN, closeN + 1)
                stack.pop()
        parentheses(0, 0)
        return res