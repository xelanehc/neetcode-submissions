class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in cache:
                return cache[(i, buying)]
            
            res = dfs(i + 1, buying)
            if buying:
                res = max(res, dfs(i + 1, not buying) - prices[i])
                cache[(i, buying)] = res
                return res
            else:
                res = max(res, dfs(i + 2, not buying) + prices[i])
                cache[(i, buying)] = res
                return res

        return dfs(0, True)