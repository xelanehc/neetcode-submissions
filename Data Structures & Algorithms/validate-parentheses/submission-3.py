class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if s == "":
            return True
        for i in range(len(s)):
            cur = s[i]
            if (cur == "]"):
                if not stack or stack.pop() != "[":
                    return False
            elif (cur == ")"):
                if not stack or stack.pop() != "(":
                    return False
            elif (cur == "}"):
                if not stack or stack.pop() != "{":
                    return False
            else:
                stack.append(cur)
        return len(stack) == 0