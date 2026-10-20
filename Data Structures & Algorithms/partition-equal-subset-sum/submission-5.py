class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2

        cache = defaultdict(bool)

        def dfs(i, cur):
            if i == len(nums):
                return False
            
            if cur == target:
                return True
            if (i, cur) in cache:
                return cache[(i, cur)]
            
            res = dfs(i + 1, cur) or dfs(i + 1, cur + nums[i])
            cache[(i, cur)] = res
            return res
        
        return dfs(0, 0)