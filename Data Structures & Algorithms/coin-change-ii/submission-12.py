class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for i in range(len(coins) + 1)]
        coins.sort()
        for i in range(len(coins) + 1):
            dp[i][0] = 1
        
        for r in range(len(coins) - 1, -1, -1):
            for c in range(amount + 1):
                if c >= coins[r]:
                    dp[r][c] = dp[r + 1][c]
                    dp[r][c] += dp[r][c - coins[r]]
        
        return dp[0][amount]