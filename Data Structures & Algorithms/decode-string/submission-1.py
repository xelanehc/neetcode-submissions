class Solution:
    def decodeString(self, s: str) -> str:
        strStack = []
        numStack = []
        cur = ""
        k = 0

        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == "[":
                strStack.append(cur)
                numStack.append(k)
                cur = ""
                k = 0
            elif c == "]":
                temp = cur
                cur = strStack.pop()
                tK = numStack.pop()
                cur += temp * tK
            else:
                cur += c
        
        return cur