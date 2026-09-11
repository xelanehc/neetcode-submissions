class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for i in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1
        def dfs(r, c):
            if r < 0 or r == m or c < 0 or c == n:
                return
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
            dfs(r + 1, c)
            dfs(r, c + 1)
            
        dfs(1, 1)
        return dp[m - 1][n - 1]