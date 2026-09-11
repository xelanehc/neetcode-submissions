class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        n, m = len(s), len(p)

        def dfs(i, j):
            if j == m:
                return i == n
            if (i, j) in dp:
                return dp[(i, j)]
            
            res = i < n and (s[i] == p[j] or p[j] == '.')
            if j + 1 < m and p[j + 1] == '*':
                dp[(i, j)] = dfs(i, j + 2) or (res and dfs(i + 1, j))
                return dp[(i, j)]
            if res:
                dp[(i, j)] = dfs(i + 1, j + 1)
                return dp[(i, j)]
            dp[(i, j)] = False
            return False
        
        return dfs(0, 0)