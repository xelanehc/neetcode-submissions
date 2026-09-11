class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        cur = []
        nums.sort()

        def dfs(i):
            if i == len(nums):
                return
            cur.append(nums[i])
            if cur not in res:
                res.append(cur.copy())
            dfs(i + 1)
            cur.pop()
            dfs(i + 1)

        dfs(0)
        return res