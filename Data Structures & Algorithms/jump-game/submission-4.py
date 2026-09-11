class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def dfs(i):
            if i >= len(nums) - 1:
                return True
            res = False
            for j in range(1, nums[i] + 1):
                res = res or dfs(i + j)
            return res
        return dfs(0)
