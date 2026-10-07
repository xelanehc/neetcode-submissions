class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l, r = 1, piles[-1]
        best = 0

        while l <= r:
            m = l + (r - l) // 2
            total = 0
            for p in piles:
                total += math.ceil(float(p) / m)
            if total <= h:
                best = m
                r = m - 1
            else:
                l = m + 1

        return best