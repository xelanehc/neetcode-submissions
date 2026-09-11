class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [n for n in nums]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
        return max(dp)