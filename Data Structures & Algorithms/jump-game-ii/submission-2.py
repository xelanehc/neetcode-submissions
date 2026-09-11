class Solution:
    def jump(self, nums: List[int]) -> int:
        def dfs(i, jumps):
            if i >= len(nums) - 1:
                return jumps
            cur = float('inf')
            for j in range(1, nums[i] + 1):
                cur = min(cur, dfs(i + j, jumps + 1))
            return cur
        return dfs(0, 0)