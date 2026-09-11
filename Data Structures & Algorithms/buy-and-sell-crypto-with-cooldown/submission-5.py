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
                buy = dfs(i + 1, not buying) - prices[i]
                res = max(res, buy)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                res = max(res, sell)
            
            cache[(i, buying)] = res
            return res
        
        return dfs(0, True)