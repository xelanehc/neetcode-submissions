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

            j = 0
            while j < nums[i] and i + j + 1 < len(nums):
                if dfs(i + j + 1):
                    cache[i] = True
                    return True
                j += 1
            cache[i] = False
            return False
        
        return dfs(0)