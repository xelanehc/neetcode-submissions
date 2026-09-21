class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            leftMax = max(height[l], leftMax)
            rightMax = max(height[r], rightMax)

            res += (leftMax - min(leftMax, height[l])) + (rightMax - min(rightMax, height[r]))

            if leftMax < rightMax:
                l += 1
            else:
                r -= 1
        
        return res