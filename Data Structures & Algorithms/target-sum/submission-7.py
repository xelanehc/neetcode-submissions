class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0
        dp = {}

        def dfs(i, cur):
            if i == len(nums):
                return cur == target
            if (i, cur) in dp:
                return dp[(i, cur)]
            
            res = dfs(i + 1, cur - nums[i]) + dfs(i + 1, cur + nums[i])
            dp[(i, cur)] = res
            return res

        return dfs(0, 0)