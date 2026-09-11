class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        res = float('inf')

        def isValid(eatingRate):
            hours = 0
            for p in piles:
                hours += math.ceil(p / eatingRate)
            return hours <= h

        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            if isValid(mid):
                res = min(res, mid)
                hi = mid - 1
            else:
                lo = mid + 1

        return res