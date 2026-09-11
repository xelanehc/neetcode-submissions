class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '}':
                if not stack or stack.pop() != '{':
                    return False
                continue
            if c == ')':
                if not stack or stack.pop() != '(':
                    return False
                continue
            if c == ']':
                if not stack or stack.pop() != '[':
                    return False
                continue
            stack.append(c)
        return len(stack) == 0