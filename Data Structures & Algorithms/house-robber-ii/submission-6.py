class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        cache = defaultdict(int)

        def dfs(i, flag):
            if i >= len(nums):
                return 0
            if i == len(nums) - 1 and flag:
                return 0
            if cache[(i, flag)] != 0:
                return cache[(i, flag)]

            cache[(i, flag)] = max(dfs(i + 1, flag), nums[i] + dfs(i + 2, flag))
            return cache[(i, flag)]
        
        return max(dfs(0, True), dfs(1, False))