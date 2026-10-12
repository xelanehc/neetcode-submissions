class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        memo = [[-1] * (amount + 1) for i in range(len(coins) + 1)]

        def dfs(i, amt):
            if amt == 0:
                return 1
            if i >= len(coins):
                return 0
            if memo[i][amt] != -1:
                return memo[i][amt]
            
            res = 0
            if amt >= coins[i]:
                res = dfs(i + 1, amt)
                res += dfs(i, amt - coins[i])
            
            memo[i][amt] = res
            return res
        
        return dfs(0, amount)