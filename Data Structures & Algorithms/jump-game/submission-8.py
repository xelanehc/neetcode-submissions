class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = {}
        def dfs(i):
            if i == len(nums) - 1:
                return True
            if i in cache:
                return cache[i]
            if nums[i] == 0:
                return False

            res = False
            j = 0
            while j < nums[i] and i + j + 1 < len(nums):
                res = res or dfs(i + j + 1)
                j += 1
            cache[i] = res
            return res
        
        return dfs(0)