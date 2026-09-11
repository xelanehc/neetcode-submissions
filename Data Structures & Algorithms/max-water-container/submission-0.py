class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights) - 1):
            for j in range(i + 1, len(heights)):
                amt = min(heights[i], heights[j]) * (j - i)
                res = max(amt, res)
        return res
