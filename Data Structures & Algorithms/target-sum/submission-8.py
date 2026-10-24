class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def dfs(i, cur):
            if i == len(nums):
                return cur == target
            if (i, cur) in cache:
                return cache[(i, cur)]
            
            res = dfs(i + 1, cur + nums[i]) + dfs(i + 1, cur - nums[i])
            cache[(i, cur)] = res
            return res
        
        return dfs(0, 0)