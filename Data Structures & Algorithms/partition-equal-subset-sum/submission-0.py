class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        n = len(nums)
        dp = [[-1] * (target + 1) for i in range(n)]

        def dfs(i, t):
            if t == 0:
                return True
            if i >= n or t < 0:
                return False
            if dp[i][t] != -1:
                return dp[i][t]
            dp[i][t] = (dfs(i + 1, t) or dfs(i + 1, t - nums[i]))
            return dp[i][t]
        return dfs(0, target)