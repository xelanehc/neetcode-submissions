class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0
        def dfs(i, cur):
            if i == len(nums):
                return cur == target
            
            res = dfs(i + 1, cur - nums[i]) + dfs(i + 1, cur + nums[i])

            return res

        return dfs(0, 0)