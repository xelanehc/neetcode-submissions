class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lmax = rmax = 0
        res = 0
        while l < r:
            lmax = max(height[l], lmax)
            rmax = max(height[r], rmax)
            res += lmax - height[l]
            res += rmax - height[r]
            if lmax <= rmax:
                l += 1
            else:
                r -= 1
        return res