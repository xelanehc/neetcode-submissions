class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = float('inf')
        res = 0

        for p in prices:
            m = min(p, m)
            res = max(res, p - m)
        
        return res