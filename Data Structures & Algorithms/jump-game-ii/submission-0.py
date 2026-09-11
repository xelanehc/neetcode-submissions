class Solution:
    def jump(self, nums: List[int]) -> int:
        def dfs(i):
            if i >= len(nums) - 1:
                return 0
            m = float('inf')
            for jump in range(1, nums[i] + 1):
                m = min(m, 1 + dfs(i + jump))
            return m
        return dfs(0)