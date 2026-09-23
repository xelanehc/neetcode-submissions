class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        strings = path.split("/")

        for s in strings:
            print(stack)
            if s == "" or s == ".":
                continue
            elif s == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(s)
        
        return "/" + "/".join(stack)

