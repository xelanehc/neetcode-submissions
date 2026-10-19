class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = defaultdict(int)

        def dfs(a):
            if a == 0:
                return 0
            if cache[a] != 0:
                return cache[a]
            
            res = float('inf')
            for c in coins:
                if a - c >= 0:
                    res = min(res, 1 + dfs(a - c))
            cache[a] = res
            return res
        
        res = dfs(amount)
        return res if res != float('inf') else -1