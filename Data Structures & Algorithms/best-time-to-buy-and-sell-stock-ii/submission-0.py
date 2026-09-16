class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        d = {}

        def recurse(i, bought):
            if i == len(prices):
                return 0
            if (i, bought) in d:
                return d[(i, bought)]
            res = recurse(i + 1, bought)
            if bought:
                res = max(res, prices[i] + recurse(i + 1, False))
            else:
                res = max(res, -prices[i] + recurse(i + 1, True))
            d[(i, bought)] = res
            return res
            
        return recurse(0, False)