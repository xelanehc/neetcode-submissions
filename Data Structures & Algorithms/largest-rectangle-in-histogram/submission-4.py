class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i, h in enumerate(heights):
            leftMost = i
            while stack and stack[-1][1] >= h:
                curIndex, curHeight = stack.pop()
                res = max(res, curHeight * (i - curIndex))
                leftMost = curIndex
            stack.append((leftMost, h))
        
        for i, h in stack:
            res = max(res, h * (len(heights) - i))
        
        return res