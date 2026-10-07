class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        res = float('inf')
        l, r = max(weights), sum(weights)

        while l <= r:
            m = l + (r - l) // 2
            cur, cnt = 0, 1
            for w in weights:
                if cur + w > m:
                    cur = 0
                    cnt += 1
                cur += w

            if cnt <= days:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        
        return res
            