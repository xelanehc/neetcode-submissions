class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height) - 1
        res = 0
        leftWall = height[l]
        rightWall = height[r]
        while l < r:
            if leftWall <= rightWall:
                l += 1
                leftWall = max(height[l], leftWall)
                res += leftWall - height[l]
            else:
                r -= 1
                rightWall = max(height[r], rightWall)
                res += rightWall - height[r]
        return res
            