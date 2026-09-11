class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 0, max(piles)
        ret = r
        while l <= r:
            k = (l + r) // 2
            total = 0
            if k == 0:
                break
            for p in piles:
                total += math.ceil(float(p) / k)
            if total > h:
                l = k + 1
            else:
                ret = k
                r = k - 1
        return ret
            