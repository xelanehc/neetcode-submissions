class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = float('inf')
        nums = set(nums)

        for n in nums:
            if n < 0:
                continue
            j = 1
            while j in nums:
                j += 1
            res = min(res, j)

        return 1 if res == float('inf') else res