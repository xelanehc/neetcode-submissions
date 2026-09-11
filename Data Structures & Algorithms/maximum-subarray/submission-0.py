class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = 0
        res = max(nums)
        for n in nums:
            if prefix + n < 0:
                prefix = 0
                continue
            prefix += n
            res = max(res, prefix)
        return res