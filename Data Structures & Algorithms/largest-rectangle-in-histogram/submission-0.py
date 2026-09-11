class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        for h in heights:
            res = max(res, h)
        for i in range(1, res + 1):
            cmax = 0
            for h in heights:
                if h < i:
                    res = max(res, cmax)
                    cmax = 0
                    continue
                cmax += i
            res = max(res, cmax)
        return res