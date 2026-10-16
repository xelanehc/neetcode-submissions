class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], nums, [False] * len(nums))
        return self.res
    
    def backtrack(self, cur, nums, pick):
        if len(cur) == len(nums):
            self.res.append(cur.copy())
            return
        for i in range(len(nums)):
            if not pick[i]:
                cur.append(nums[i])
                pick[i] = True
                self.backtrack(cur, nums, pick)
                cur.pop()
                pick[i] = False