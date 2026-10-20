class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = defaultdict(int)

        def dfs(i, j):
            if i == len(nums):
                return 0
            if cache[(i, j)] != 0:
                return cache[(i, j)]
            
            res = dfs(i + 1, j)
            if j == -1 or nums[j] < nums[i]:
                res = max(res, 1 + dfs(i + 1, i))
            
            cache[(i, j)] = res
            return res
        return dfs(0, -1)