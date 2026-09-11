class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []

        def dfs(i, s):
            if s == target:
                res.append(combination.copy())
                return
            if s > target or i == len(nums):
                return
            
            s += nums[i]
            combination.append(nums[i])
            dfs(i, s)
            s -= nums[i]
            combination.pop()
            dfs(i + 1, s)
        
        dfs(0, 0)
        return res