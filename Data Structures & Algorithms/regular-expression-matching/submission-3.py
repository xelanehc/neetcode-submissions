class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def dfs(i, j):
            if j == len(p):
                return i == len(s)
            
            match = i < len(s) and (p[j] == '.' or s[i] == p[j])

            if j + 1 < len(p) and p[j + 1] == '*':
                return dfs(i, j + 2) or (match and dfs(i + 1, j))
            
            if match:
                return dfs(i + 1, j + 1)
            return False
        
        return dfs(0, 0)