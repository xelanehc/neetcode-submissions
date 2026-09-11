class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ROWS, COLS = len(coins), amount
        coins.sort()
        dp = [[0] * (COLS + 1) for i in range(ROWS + 1)]
        for i in range(ROWS + 1):
            dp[i][0] = 1

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS + 1):
                if c >= coins[r]:
                    dp[r][c] = dp[r + 1][c]
                    dp[r][c] += dp[r][c - coins[r]]
        
        return dp[0][COLS]