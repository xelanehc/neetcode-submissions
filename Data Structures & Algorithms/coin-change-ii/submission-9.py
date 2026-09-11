class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = [[-1] * (amount + 1) for i in range(len(coins))]

        def dfs(i, cur):
            if cur == 0:
                return 1
            if i >= len(coins):
                return 0
            if dp[i][cur] != -1:
                return dp[i][cur]
            res = 0
            if cur >= coins[i]:
                res = dfs(i + 1, cur)
                res += dfs(i, cur - coins[i])
            dp[i][cur] = res
            return res
        
        return dfs(0, amount)