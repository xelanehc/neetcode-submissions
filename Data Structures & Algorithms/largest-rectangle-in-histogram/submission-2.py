class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        n = len(heights)
        for i, h in enumerate(heights):
            left = i
            while stack and stack[-1][1] >= heights[i]:
                index, height = stack.pop()
                res = max(res, height * (i - index))
                left = index
            stack.append((left, h))
        for i, h in stack:
            res = max(res, h * (len(heights) - i))
        return res