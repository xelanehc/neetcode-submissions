class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                    continue
                else:
                    return False
            if c == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                    continue
                else:
                    return False
            if c == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                    continue
                else:
                    return False
            stack.append(c)
        
        return len(stack) == 0