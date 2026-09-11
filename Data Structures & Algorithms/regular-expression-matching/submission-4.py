class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}

        def dfs(i, j):
            if j == len(p):
                return i == len(s)
            if (i, j) in dp:
                return dp[(i, j)]
            
            match = i < len(s) and (p[j] == '.' or s[i] == p[j])

            if j + 1 < len(p) and p[j + 1] == '*':
                return dfs(i, j + 2) or (match and dfs(i + 1, j))
            
            if match:
                dp[(i, j)] = dfs(i + 1, j + 1)
                return dp[(i, j)]
            dp[(i, j)] = False
            return dp[(i, j)]
        
        return dfs(0, 0)